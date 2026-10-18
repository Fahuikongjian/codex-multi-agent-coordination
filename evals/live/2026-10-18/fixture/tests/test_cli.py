"""Integration coverage for the ledger command's file and standard I/O."""

import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest


PROJECT_ROOT = Path(__file__).resolve().parents[1]
CLI_PATH = PROJECT_ROOT / "cli.py"
TEMP_ROOT = PROJECT_ROOT / "tmp" / "T2"


class LedgerCLIIntegrationTests(unittest.TestCase):
    def setUp(self):
        TEMP_ROOT.mkdir(parents=True, exist_ok=True)
        self.temp_directory = tempfile.TemporaryDirectory(prefix="cli-", dir=TEMP_ROOT)
        self.addCleanup(self.temp_directory.cleanup)
        self.case_directory = Path(self.temp_directory.name)

    def run_cli(self, *arguments, stdin=None):
        environment = os.environ.copy()
        environment["PYTHONDONTWRITEBYTECODE"] = "1"
        environment["PYTHONIOENCODING"] = "utf-8"
        return subprocess.run(
            [sys.executable, "-B", str(CLI_PATH), *map(str, arguments)],
            cwd=PROJECT_ROOT,
            input=stdin,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            encoding="utf-8",
            env=environment,
            timeout=10,
            check=False,
        )

    def write_csv(self, text, *, encoding="utf-8"):
        path = self.case_directory / "orders with spaces.csv"
        path.write_text(text, encoding=encoding)
        return path

    def assert_success(self, result, expected):
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(result.stderr, "")
        self.assertTrue(result.stdout.endswith("\n"), repr(result.stdout))
        self.assertEqual(len(result.stdout.splitlines()), 1, repr(result.stdout))
        payload = json.loads(result.stdout)
        self.assertIs(type(payload), dict)
        self.assertEqual(set(payload), {"order_count", "total_cents"})
        for value in payload.values():
            self.assertIs(type(value), int)
        self.assertEqual(payload, expected)

    def assert_data_error(self, result):
        self.assertEqual(result.returncode, 2, result.stderr)
        self.assertEqual(result.stdout, "", "Errors must not emit partial JSON")
        self.assertTrue(result.stderr.startswith("error: "), repr(result.stderr))
        self.assertTrue(result.stderr[len("error: "):].strip())
        self.assertNotIn("Traceback", result.stderr)

    def test_file_input_emits_one_json_object_with_exact_integer_total(self):
        path = self.write_csv(
            'unit_price,order_id,quantity\n'
            ' 12.30 ," invoice, \"\"A\"\" ", 2 \n'
            '0.07,second,3\n'
        )
        self.assert_success(
            self.run_cli(path), {"order_count": 2, "total_cents": 2481}
        )

    def test_stdin_input_emits_json(self):
        self.assert_success(
            self.run_cli(
                "-", stdin="order_id,quantity,unit_price\nfirst,3,1.25\nsecond,1,2\n"
            ),
            {"order_count": 2, "total_cents": 575},
        )

    def test_utf8_bom_file_is_read_successfully(self):
        path = self.write_csv(
            "order_id,quantity,unit_price\ncaf\u00e9,2,0.10\n", encoding="utf-8-sig"
        )
        self.assert_success(
            self.run_cli(path), {"order_count": 1, "total_cents": 20}
        )

    def test_header_only_stdin_emits_zero_totals(self):
        self.assert_success(
            self.run_cli("-", stdin="order_id,quantity,unit_price\n"),
            {"order_count": 0, "total_cents": 0},
        )

    def test_missing_file_reports_error_without_stdout(self):
        missing_path = self.case_directory / "missing-orders.csv"
        result = self.run_cli(missing_path)
        self.assert_data_error(result)
        self.assertIn(missing_path.name, result.stderr)

    def test_invalid_amount_reports_error_after_a_valid_row_without_stdout(self):
        for amount in ("1.234", "NaN", "1e2", "-0.10", "not-money"):
            with self.subTest(amount=amount):
                result = self.run_cli(
                    "-",
                    stdin=(
                        "order_id,quantity,unit_price\n"
                        "valid,1,1.25\n"
                        f"invalid,1,{amount}\n"
                    ),
                )
                self.assert_data_error(result)
                self.assertRegex(result.stderr.lower(), r"price|amount")

    def test_missing_or_extra_row_cells_report_error_without_stdout(self):
        for row in ("invalid,1", "invalid,1,2.00,extra"):
            with self.subTest(row=row):
                path = self.write_csv(
                    "order_id,quantity,unit_price\nvalid,1,1.25\n" + row + "\n"
                )
                result = self.run_cli(path)
                self.assert_data_error(result)
                self.assertRegex(result.stderr.lower(), r"row|column|cell|field")

    def test_no_arguments_reports_usage_and_exits_two_without_stdout(self):
        result = self.run_cli()
        self.assertEqual(result.returncode, 2, result.stderr)
        self.assertEqual(result.stdout, "")
        self.assertIn("usage:", result.stderr.lower())
        self.assertIn("input", result.stderr.lower())
        self.assertIn("required", result.stderr.lower())
        self.assertNotIn("Traceback", result.stderr)


if __name__ == "__main__":
    unittest.main()

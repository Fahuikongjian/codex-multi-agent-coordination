import os
from pathlib import Path
import subprocess
import sys
import unittest

class LargeNumberCliRegression(unittest.TestCase):
    def test_large_input_is_validation_error_not_traceback(self):
        root = Path(__file__).resolve().parents[1]
        text = "order_id,quantity,unit_price\na," + "9" * 2200 + "," + "9" * 2200 + ".99\n"
        result = subprocess.run([sys.executable, "-B", str(root / "cli.py"), "-"], input=text, capture_output=True, text=True, cwd=root, timeout=10, env={**os.environ, "PYTHONDONTWRITEBYTECODE": "1"})
        self.assertEqual(result.returncode, 2, result.stderr)
        self.assertEqual(result.stdout, "")
        self.assertTrue(result.stderr.startswith("error:"), result.stderr)
        self.assertIn("quantity", result.stderr)
        self.assertNotIn("Traceback", result.stderr)

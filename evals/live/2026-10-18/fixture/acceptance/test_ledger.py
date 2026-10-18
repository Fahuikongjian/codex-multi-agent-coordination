import unittest
from ledger import summarize_orders

HEADER = "order_id,quantity,unit_price\n"

class LedgerAcceptance(unittest.TestCase):
    def test_header_only_is_empty(self):
        self.assertEqual(summarize_orders(HEADER), {"order_count": 0, "total_cents": 0})

    def test_exact_decimal_total(self):
        self.assertEqual(summarize_orders(HEADER + "a,1,0.10\nb,1,0.20\n"), {"order_count": 2, "total_cents": 30})

    def test_quantity_and_cell_whitespace(self):
        self.assertEqual(summarize_orders(HEADER + " a , 3 , 1.25 \n")["total_cents"], 375)

    def test_large_price_without_float_loss(self):
        self.assertEqual(summarize_orders(HEADER + "a,3,1000000000000000.01\n")["total_cents"], 300000000000000003)

    def test_bom(self):
        self.assertEqual(summarize_orders("\ufeff" + HEADER + "a,1,2.5\n")["total_cents"], 250)

    def test_quoted_identifier(self):
        self.assertEqual(summarize_orders(HEADER + '"a,b",2,1.01\n')["total_cents"], 202)

    def test_reordered_header(self):
        self.assertEqual(summarize_orders("quantity,unit_price,order_id\n2,1.50,a\n"), {"order_count": 1, "total_cents": 300})

    def test_bad_headers(self):
        for text in ("", "order_id,quantity\n", "order_id,quantity,unit_price,extra\n", "order_id,quantity,quantity\n"):
            with self.subTest(text=text), self.assertRaises(ValueError):
                summarize_orders(text)

    def test_invalid_quantities(self):
        for value in ("0", "1.5", "x", "+1", "", "-0"):
            with self.subTest(value=value), self.assertRaises(ValueError):
                summarize_orders(HEADER + f"a,{value},1.00\n")

    def test_invalid_prices(self):
        for value in ("-1", "NaN", "Infinity", "1.234", "1e2", "", "+1.00"):
            with self.subTest(value=value), self.assertRaises(ValueError):
                summarize_orders(HEADER + f"a,1,{value}\n")

    def test_missing_or_extra_cells(self):
        for row in ("a,1\n", "a,1,1.00,extra\n"):
            with self.subTest(row=row), self.assertRaises(ValueError):
                summarize_orders(HEADER + row)

    def test_duplicate_ids(self):
        with self.assertRaises(ValueError):
            summarize_orders(HEADER + "a,1,1.00\n a ,2,2.00\n")

    def test_blank_identifier(self):
        with self.assertRaises(ValueError):
            summarize_orders(HEADER + " ,1,1.00\n")

    def test_empty_lines(self):
        self.assertEqual(summarize_orders(HEADER + "\na,1,1\n\n"), {"order_count": 1, "total_cents": 100})

    def test_refunds_reduce_net_total(self):
        self.assertEqual(summarize_orders(HEADER + "sale,2,1.20\nrefund,-1,1.20\n"), {"order_count": 2, "total_cents": 120})

    def test_all_refund_ledger(self):
        self.assertEqual(summarize_orders(HEADER + "refund,-3,0.10\n"), {"order_count": 1, "total_cents": -30})

    def test_refund_preserves_integer_schema(self):
        result = summarize_orders(HEADER + "refund,-2,2.50\n")
        self.assertEqual(set(result), {"order_count", "total_cents"})
        self.assertIs(type(result["total_cents"]), int)
        self.assertEqual(result["total_cents"], -500)

    def test_supported_numeric_boundaries(self):
        quantity = "9" * 18
        price_whole = "9" * 30
        expected = int(quantity) * (int(price_whole) * 100 + 99)
        self.assertEqual(summarize_orders(HEADER + f"edge,{quantity},{price_whole}.99\n"), {"order_count": 1, "total_cents": expected})

    def test_oversized_quantity_is_field_validation(self):
        for digits in (19, 4301):
            with self.subTest(digits=digits), self.assertRaisesRegex(ValueError, "quantity"):
                summarize_orders(HEADER + "oversize," + "9" * digits + ",1.00\n")

    def test_oversized_price_is_field_validation(self):
        for digits in (31, 4301):
            with self.subTest(digits=digits), self.assertRaisesRegex(ValueError, "unit_price"):
                summarize_orders(HEADER + "oversize,1," + "9" * digits + ".99\n")

    def test_parser_field_limit_remains_validation_error(self):
        import csv
        overlong = "9" * (csv.field_size_limit() + 1)
        for row in ("large," + overlong + ",1.00\n", "large,1," + overlong + ".99\n"):
            with self.subTest(column=row[:12]), self.assertRaisesRegex(ValueError, "invalid CSV"):
                summarize_orders(HEADER + row)

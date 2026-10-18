# Offline CSV ledger CLI - acceptance contract D3, revision 3

Implement ledger.summarize_orders(csv_text: str) -> dict[str, int].
Return exactly {"order_count": number_of_data_rows, "total_cents": integer_total}.
Every row has a unique nonblank order_id, quantity, unit_price.
Required headers are exactly order_id,quantity,unit_price, in any order; duplicate or extra headers are invalid.
Strip surrounding whitespace in data cells. Accept a UTF-8 BOM before the first header and properly quoted CSV identifiers.
Skip ordinary empty lines as CSV does; header-only input is valid and totals zero.
Quantity is an ASCII decimal integer written as -?[0-9]+, revision 2 permits negative quantities for refunds but rejects zero. Each refund remains a data row counted in order_count; total_cents is the signed net total. The public JSON schema must not change.
Price is an unsigned ASCII decimal matching [0-9]+(?:\.[0-9]{1,2})?; reject exponents, NaN, infinity, negatives, and excess decimal places.
Use exact integer cents; no floating-point rounding, even for large prices.
Reject invalid data, duplicate IDs, missing cells or extra row cells with ValueError and an informative message.
CLI is already supplied: python cli.py INPUT or python cli.py -; stdout is one JSON object plus newline, errors go to stderr and exit 2 without partial stdout.
Use only Python standard library. No network, dependencies, background processes or global configuration changes.

D3 supported numeric bounds: quantity has at most 18 ASCII decimal digits excluding its optional minus sign; unit_price has at most 30 digits in its whole part plus the already permitted 0-2 fraction digits. Leading zeros count toward these bounds. Reject oversized fields before integer conversion with an informative ValueError naming the field. CLI must return exit 2, informative stderr, and no stdout for oversized input. Do not change global or interpreter integer conversion security limits. Refund handling, exact money and JSON schema stay unchanged.

D4 parser boundary: retain the standard-library CSV field-size limit. Parser-level malformed/oversized CSV errors may identify the line and CSV condition rather than a specific field, because no complete row is available. Field-specific D3 diagnostics apply after successful CSV tokenization. Such parser errors must still become ValueError and CLI exit 2 without partial output or traceback.

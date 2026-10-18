"""Summarize an offline CSV ledger from a file or standard input."""
import argparse
import json
from pathlib import Path
import sys
from ledger import summarize_orders


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", help="CSV path, or - for stdin")
    args = parser.parse_args(argv)
    try:
        text = sys.stdin.read() if args.input == "-" else Path(args.input).read_text(encoding="utf-8-sig")
        result = summarize_orders(text)
    except (ValueError, OSError) as error:
        print(f"error: {error}", file=sys.stderr)
        return 2
    print(json.dumps(result, ensure_ascii=False, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

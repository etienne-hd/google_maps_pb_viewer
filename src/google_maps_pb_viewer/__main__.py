import argparse


def get_parsed_pb(part: str) -> tuple[str, str, str]:
    for i, c in enumerate(part):
        if c.isalpha():
            return part[:i], part[i], part[i + 1 :]


def print_pb(parts: list[str], indent: int = 4, depth: int = 0, n: int = -1) -> int:
    indent_length = indent * depth

    i = 0
    while i < len(parts) and (n == -1 or i < n):
        part = parts[i]
        i += 1
        field, pb_type, value = get_parsed_pb(part)
        print(indent_length * " ", f"{field}: ", sep="", end="")
        if pb_type == "m":
            print("{")
            i += print_pb(parts=parts[i:], indent=indent, depth=depth + 1, n=int(value))
            print(indent_length * " ", "}", sep="")
        elif pb_type == "b":
            print("true" if value == "1" else "false")
        else:
            print(value)
    return i


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Decode and pretty-print a Google Maps encoded protobuf string."
    )

    parser.add_argument(
        "pb", type=str, help="Encoded Google Maps protobuf string (starting with '!')."
    )

    parser.add_argument(
        "-i",
        "--indent",
        type=int,
        default=4,
        help="Number of spaces used for output indentation (default: 4).",
    )

    args = parser.parse_args()
    parts = args.pb.split("!")[1:]
    print_pb(parts=parts, indent=args.indent)

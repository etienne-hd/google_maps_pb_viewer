import argparse

def get_parsed_pb(pb: str) -> tuple[str, str, str]:
	for i, c in enumerate(pb):
		if c.isalpha():
			return pb[:i], pb[i], pb[i + 1:]

def print_pb(pb: list[str], indent: int = 4, depth: int = 0, n: int = -1) -> int:
	indent_length = indent * depth

	i = 0
	while i < len(pb) and (n == -1 or i < n):
		current_pb = pb[i]
		i += 1
		field, pb_type, value = get_parsed_pb(current_pb)
		print(indent_length * " ", f"{field}: ", sep="", end="")
		if pb_type == "m":
			print("{")
			i += print_pb(pb=pb[i:], indent=indent, depth=depth + 1, n=int(value))
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
        "pb",
        type=str,
        help="Encoded Google Maps protobuf string (starting with '!')."
    )

    parser.add_argument(
        "-i",
        "--indent",
        type=int,
        default=4,
        help="Number of spaces used for output indentation (default: 4)."
    )

    args = parser.parse_args()

    pb = args.pb.split("!")[1:]
    print_pb(pb=pb, indent=args.indent)
import argparse
from pathlib import Path

from Cython import Tempita


def process_tempita(input_file, output_dir):
    with open(input_file, encoding="utf-8") as f:
        tmpl = f.read()
    pyxcontent = Tempita.sub(tmpl)

    output_file = Path(output_dir) / input_file.stem
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(pyxcontent)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("input_file", type=Path, help="Path to the input file")
    parser.add_argument("-o", "--output_dir", type=Path, help="Path to the output directory")
    args = parser.parse_args()

    if args.input_file.suffix != ".in":
        raise ValueError(f"Unexpected extension: {args.input_file}")

    process_tempita(args.input_file, args.output_dir)


if __name__ == "__main__":
    main()

import argparse
from oqhcli.args import arguments_setup
import oqhlib
from oqhlib import build, categories, indexes
import sys

def arguments_read(values):
    return {}

def main():
    parser = argparse.ArgumentParser(prog='oqh')
    arguments_setup(parser)
    args = parser.parse_args()

    if len(sys.argv) == 1:
        parser.print_help(sys.stderr)
        sys.exit(1)
        
    if "version" in args and args.version:
        print(f"oqh v{oqhlib.version}")
        sys.exit(0)

    if "command" not in args:
        parser.print_help(sys.stderr)
        sys.exit(1)

    if args.command == "help":
        parser.print_help(sys.stderr)
        sys.exit(1)
        
    if args.command == "build":
        input_filenames = build.get_input_filenames(args.inputs)

        errors_list = []
        build.split_files(input_filenames, args, errors_list)
        for err in errors_list:
            print(err)

        if args.list == False:
            categories.ensure_categories()
            indexes.generate_indexes()

if __name__ == '__main__':
    main()

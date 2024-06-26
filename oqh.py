import argparse
from oqhcli.args import arguments_setup
import oqhlib
from oqhlib import build, categories, indexes, list_items
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
            indexes.clear_indexes()
            indexes.delete_empty_dirs()
            indexes.generate_indexes()

    if args.command == "list":
        input_filenames = build.get_input_filenames(args.inputs)
        if args.orphaned == True:
            for x in list_items.list_files_orphaned(input_filenames):
                print(x)

if __name__ == '__main__':
    main()

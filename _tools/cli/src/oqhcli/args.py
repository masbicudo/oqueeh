import argparse

from oqhlib import build
from oqhlib import list_items


def arguments_setup(parser : argparse.ArgumentParser):
    parser.add_argument("-v", "--version", action='store_true')
    
    subparsers = parser.add_subparsers(help='sub-command help')

    # build sub-command
    parser_build = subparsers.add_parser(
            'build',
            help='build markdown pages from inputs',
            aliases=["b"]
        )
    parser_build.set_defaults(command="build")
    build.arguments_setup(parser_build)

    # list sub-command
    parser_list = subparsers.add_parser(
            'list',
            help='lists objects in the site',
            aliases=["l"]
        )
    parser_list.set_defaults(command="list")
    list_items.arguments_setup(parser_list)

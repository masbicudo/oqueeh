import argparse

from oqhlib import build


def arguments_setup(parser : argparse.ArgumentParser):
    parser.add_argument("-v", "--version", action='store_true')
    
    subparsers = parser.add_subparsers(help='sub-command help')

    # generate sub-command
    parser_generate = subparsers.add_parser(
            'build',
            help='build markdown pages from inputs',
            aliases=["b"]
        )
    parser_generate.set_defaults(command="build")
    build.arguments_setup(parser_generate)

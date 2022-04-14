import argparse

from helpers import setup_arg_parser

if __name__ == "__main__":
    parser = setup_arg_parser(argparse.ArgumentParser())
    args = vars(parser.parse_args())
    pass
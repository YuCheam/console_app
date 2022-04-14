import argparse
import pytest

from src.helpers import setup_arg_parser

def test_numeric_sorting():
    pass

def test_alpha_sorting():
    pass

def test_alpha_and_numeric_sorting():
    pass

def test_csv_parsing():
    pass

def test_arg_parser_error_on_nonexistant_file():
    parser = setup_arg_parser(argparse.ArgumentParser())

    with pytest.raises(SystemExit):
        parser.parse_args('./fake_file.csv alpha ascending'.split())

def test_arg_parser_error_on_invalid_args():
    parser = setup_arg_parser(argparse.ArgumentParser())

    with pytest.raises(SystemExit):
        parser.parse_args('ascending'.split())
        parser.parse_args('./data/test_file.csv ascending'.split())
import argparse
import pytest

from src.arg_parser import setup_arg_parser
from src.models.sorter import Sorter

@pytest.fixture
def test_values_1():
    return ['1','4','6','7','3','2','1.5']

@pytest.fixture
def test_values_2():
    return ['11', '12', '1e10', "'c'", 'b', "'a'", '15', '21', "'50'"]

def test_numeric_sorting_ascending(test_values_1, test_values_2):
    sorter = Sorter(test_values_1)
    sorter.set_filter('numeric')
    sorter.set_sort_order('ascending')
    result = sorter.execute()
    assert result == "1,1.5,2,3,4,6,7".split(",")

    sorter.values = test_values_2
    result = sorter.execute()
    assert result == "11,12,15,21,1e10".split(",")


def test_numeric_sorting_descending(test_values_1, test_values_2):
    sorter = Sorter(test_values_1)
    sorter.set_filter('numeric')
    sorter.set_sort_order('descending')
    result = sorter.execute()
    assert result == "7,6,4,3,2,1.5,1".split(",")

    sorter.values = test_values_2
    result = sorter.execute()
    assert result == "1e10,21,15,12,11".split(",")


def test_alpha_sorting_ascending(test_values_1, test_values_2):
    sorter = Sorter(test_values_1)
    sorter.set_filter('alpha')
    sorter.set_sort_order('ascending')
    result = sorter.execute()
    assert result == []

    sorter.values = test_values_2
    result = sorter.execute()
    assert result == "'50','a',b,'c'".split(",")

def test_alpha_sorting_descending(test_values_1, test_values_2):
    sorter = Sorter(test_values_1)
    sorter.set_filter('alpha')
    sorter.set_sort_order('descending')
    result = sorter.execute()
    assert result == []

    sorter.values = test_values_2
    result = sorter.execute()
    assert result == "'c',b,'a','50'".split(",")

def test_alpha_and_numeric_sorting_ascending(test_values_1, test_values_2):
    sorter = Sorter(test_values_1)
    sorter.set_filter('both')
    sorter.set_sort_order('ascending')
    result = sorter.execute()
    assert result == "1,1.5,2,3,4,6,7".split(",")

    sorter.values = test_values_2
    result = sorter.execute()
    assert result == "11,12,15,21,1e10,'50','a',b,'c'".split(",")

def test_alpha_and_numeric_sorting_descending(test_values_1, test_values_2):
    sorter = Sorter(test_values_1)
    sorter.set_filter('both')
    sorter.set_sort_order('descending')
    result = sorter.execute()
    assert result == "7,6,4,3,2,1.5,1".split(",")

    sorter.values = test_values_2
    result = sorter.execute()
    assert result == "'c',b,'a','50',1e10,21,15,12,11".split(",")

def test_arg_parser_error_on_nonexistant_file():
    parser = setup_arg_parser(argparse.ArgumentParser())

    with pytest.raises(SystemExit):
        parser.parse_args('./fake_file.csv alpha ascending'.split())

def test_arg_parser_error_on_invalid_args():
    parser = setup_arg_parser(argparse.ArgumentParser())

    with pytest.raises(SystemExit):
        parser.parse_args('ascending'.split())
        parser.parse_args('./data/test_file.csv ascending'.split())
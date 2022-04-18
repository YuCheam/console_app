import pytest
from src.models.sorter import Sorter


@pytest.fixture
def test_values_1():
    return ['1','4','6','7','3','2','1.5']

@pytest.fixture
def test_values_2():
    return ['11', '12', '1e10', "'c'", 'b', "'a'", '15', '21', "'50'"]

def test_sorter_setters_on_invalid_value(test_values_1):
    invalid_sort_order = 'invalid_sort'
    invalid_filter_type = 'invalid_filter'
    
    with pytest.raises(ValueError):
        Sorter(test_values_1, filter_type=invalid_filter_type, sort_order=invalid_sort_order)

        sorter = Sorter(test_values_1)
        sorter.set_filter(invalid_filter_type)
        sorter.set_filter(invalid_sort_order)

def test_numeric_sorting_ascending(test_values_1, test_values_2):
    sorter = Sorter(test_values_1)
    sorter.set_filter('numeric')
    sorter.set_sort_order('ascending')
    result = sorter.sort()
    assert result == "1,1.5,2,3,4,6,7".split(",")

    sorter.values = test_values_2
    result = sorter.sort()
    assert result == "11,12,15,21,1e10".split(",")


def test_numeric_sorting_descending(test_values_1, test_values_2):
    sorter = Sorter(test_values_1)
    sorter.set_filter('numeric')
    sorter.set_sort_order('descending')
    result = sorter.sort()
    assert result == "7,6,4,3,2,1.5,1".split(",")

    sorter.values = test_values_2
    result = sorter.sort()
    assert result == "1e10,21,15,12,11".split(",")


def test_alpha_sorting_ascending(test_values_1, test_values_2):
    sorter = Sorter(test_values_1)
    sorter.set_filter('alpha')
    sorter.set_sort_order('ascending')
    result = sorter.sort()
    assert result == []

    sorter.values = test_values_2
    result = sorter.sort()
    assert result == "'50','a',b,'c'".split(",")

def test_alpha_sorting_descending(test_values_1, test_values_2):
    sorter = Sorter(test_values_1)
    sorter.set_filter('alpha')
    sorter.set_sort_order('descending')
    result = sorter.sort()
    assert result == []

    sorter.values = test_values_2
    result = sorter.sort()
    assert result == "'c',b,'a','50'".split(",")

def test_alpha_and_numeric_sorting_ascending(test_values_1, test_values_2):
    sorter = Sorter(test_values_1)
    sorter.set_filter('both')
    sorter.set_sort_order('ascending')
    result = sorter.sort()
    assert result == "1,1.5,2,3,4,6,7".split(",")

    sorter.values = test_values_2
    result = sorter.sort()
    assert result == "11,12,15,21,1e10,'50','a',b,'c'".split(",")

def test_alpha_and_numeric_sorting_descending(test_values_1, test_values_2):
    sorter = Sorter(test_values_1)
    sorter.set_filter('both')
    sorter.set_sort_order('descending')
    result = sorter.sort()
    assert result == "7,6,4,3,2,1.5,1".split(",")

    sorter.values = test_values_2
    result = sorter.sort()
    assert result == "'c',b,'a','50',1e10,21,15,12,11".split(",")
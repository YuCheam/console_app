import pytest
from src.models.value import Value, AlphaValue, NumericValue

@pytest.fixture
def alpha_value():
    return AlphaValue('b')

def test_value_is_instance(alpha_value):
    assert Value._is_instance(alpha_value) == True
    assert Value._is_instance(NumericValue('10')) == True

    assert Value._is_instance(10) == False
    assert Value._is_instance(['d']) == False

def test_is_valid_value():
    assert NumericValue.is_valid_value('10e5') == True
    assert NumericValue.is_valid_value('1') == True
    assert NumericValue.is_valid_value('0.4') == True

    assert NumericValue.is_valid_value('a') == False
    assert NumericValue.is_valid_value("'10'") == False
    
    assert AlphaValue.is_valid_value("'a'") == True
    assert AlphaValue.is_valid_value("'ab") == True
    assert AlphaValue.is_valid_value("C") == True
    assert AlphaValue.is_valid_value("'10") == True
    assert AlphaValue.is_valid_value("'@'") == True
    
    assert AlphaValue.is_valid_value('!') == False
    assert AlphaValue.is_valid_value('10') == False

def test_sorting_of_values():
    
    assert NumericValue('8') == NumericValue('8')
    assert NumericValue('8') != NumericValue('1.5')
    assert NumericValue('20') < NumericValue('10e1000')

    assert AlphaValue("'10'") < AlphaValue("a")
    assert AlphaValue("'a'") < AlphaValue("b")
    assert AlphaValue("b") == AlphaValue("b")
    assert AlphaValue("b") != AlphaValue("c")
    
    assert NumericValue('8') < AlphaValue('b')
    assert NumericValue('10') != AlphaValue('b')
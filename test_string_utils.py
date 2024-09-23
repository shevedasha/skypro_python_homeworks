import pytest
from String_Utils import StringUtils

utils = StringUtils()

"""capitalize"""

def test_capitalize():
#Positive
    assert utils.capitilize("dasha") == "Dasha"
    assert utils.capitilize("даша") == "Даша"
    assert utils.capitilize("dasha sheveleva") == "Dasha sheveleva"
#Negativ
    assert utils.capitilize("1987") == "1987"
    assert utils.capitilize(" ") == " "
    assert utils.capitilize("***") == "***"


"""trim"""

def test_trim():
#Positive
    assert utils.trim(" Dasha ") == "Dasha"
    assert utils.trim(" Dasha Sheveleva") == "Dasha Sheveleva"
#Negativ
    assert utils.trim(" Dasha ") == "Dasha "
    assert utils.trim("  ") == "  "
    assert utils.trim(" 123") == " 123"


"""to_list"""
#Positive
@pytest.mark.parametrize('string, delimeter, result', [

    ("Dasha,Sasha,Kate", ",", ["Dasha", "Sasha", "Kate"]),
    ("1987,1981,1983", ",", ["1987", "1981", "1983"]),
#Negativ
    ("Dasha, Sasha, Kate", None, ["Dasha", "Sasha", "Kate"]),
    ("1987,1981,1983", "/", ["1987", "1981", "1983"]),
])

def test_to_list(string, delimeter, result):
    if delimeter is None:
        res = utils.to_list(string)
    else:
        res = utils.to_list(string, delimeter)
    assert res == result


"""contains"""
#Positive
@pytest.mark.parametrize('string, symbol, result', [

    ("Dasha", "s", True),
    ("Sasha", "D", False),
    ("Kate", "e", True),
#Negative
    ("Dasha", "s", False),
    ("Sasha", "D", True),
    ("", "s", True),
])

def test_contains(string, symbol, result):
    res = utils.contains(string, symbol)
    assert res == result


"""delete_symbol"""
#Positive
@pytest.mark.parametrize('string, symbol, result', [

    ("Dasha Sheveleva", "Sheveleva", "Dasha "),
    ("Sasha", "s", "Saha"),
    ("Kate from London", "from", "Kate  London"),
#Negativ
    ("Dasha", "Kate", "Daha"),
    ("Sasha in London", "  in", "Sasha London"),
    ("", "in", "",)    
])
def test_delete_symbol(string, symbol, result):
    res = utils.delete_symbol(string, symbol)
    assert res == result


"""starts_with"""
#Positive
@pytest.mark.parametrize('string, symbol, result', [

    ("Dasha", "D", True),
    ("1987", "1", True),
    ("Sasha", "K", False),
#Negativ
    ("Kate", "D", True),
    ("", "D", True),
    ("Sasha", "S", False),
])

def test_starts_with(string, symbol, result):
    res = utils.starts_with(string, symbol)
    assert res == result


"""end_wit"""
#Positive
@pytest.mark.parametrize('string, symbol, result', [

    ("Dasha", "a", True),
    ("SASHA", "A", True),
    ("Kate 1987", "7", True),
    ("DashA", "a", False),
#Negativ
     ("Dasha", "", True),
     ("Sasha", "S", True),
     ("Kate", "e", False),
])
def test_end_with(string, symbol, result):
    res = utils.end_with(string, symbol)
    assert res == result


"""is_empty"""
#Positive
@pytest.mark.parametrize('string, result', [

    ("", True),
    ("", True),
    ("Dasha", False),
#Negativ
    ("Dasha", True),
    ("", False),
])

def test_is_empty(string, result):
    res = utils.is_empty(string)
    assert res == result


"""list_to_stri"""
#Positive
@pytest.mark.parametrize('lst, joiner, result', [

    (["D", "a", "s", "h", "a"], "", "Dasha"),
    (["Dasha", "Sheveleva"], "-", "Dasha-Sheveleva"),
    (["Sasha", "in", "London"], None, "Sasha, in, London"),
#Negativ
     (["Kate", "from", "Moscow"], None, "Kate from Moscow"),
     (["Dasha", "dogs", ""]),
     (["1", "2", "3"], "/", "1/2,3"),
])
def test_list_to_string(lst, joiner, result):
    if joiner == None:
        res = utils.list_to_string(lst)
    else:
        res = utils.list_to_string(lst, joiner)
    assert res == result

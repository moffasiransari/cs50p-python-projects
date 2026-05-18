from fuel import convert,gauge
import pytest

def test_convert_whole():
    assert convert("100/100")== 100
    assert convert("1/2")== 50

def test_convert_valueerror():
    with pytest.raises(ValueError):
        convert("cat/cat")

def test_convert_negtvx():
    with pytest.raises(ValueError):
        convert("-1/2")

def test_convert_ngtvy():
    with pytest.raises(ValueError):
        convert("1/-2")

def test_convert_x_greater_y():
    with pytest.raises(ValueError):
        convert("2/1")

def test_convert_zeroerror():
    with pytest.raises(ZeroDivisionError):
        convert("2/0")

def test_gauge():
    assert gauge(1)=="E"
    assert gauge(99)=="F"
    assert gauge(23)=="23%"
test_convert_whole()

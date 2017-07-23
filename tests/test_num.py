import pgtk.num
import pytest

def test_droot_ok():
    assert pgtk.num.droot(124) == 7

def test_droot_ok2():
    assert pgtk.num.droot(1399) == 4

def test_droot_string():
    assert pgtk.num.droot('24525') == 9

def test_droot_invalid_string():
    with pytest.raises(ValueError):
        pgtk.num.droot("0O$4")

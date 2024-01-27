import pytest
from peek import utils

def test_EmptyStringIsRejected():
    assert utils.validateURL('') == False

def test_BadUrlIsRejected():
    assert utils.validateURL('notgood//notgood.url') == False

def test_BadUrlIsRejected2():
    assert utils.validateURL('notgood') == False

def test_BadUrlIsRejected3():
    assert utils.validateURL('.//.2.url') == False
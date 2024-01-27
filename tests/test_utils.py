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

def test_GoodUrlIsAccepted():
    assert utils.validateURL('http://good.com')

def test_GoodUrlIsAccepted2():
    assert utils.validateURL('https://whotube.somerandomdomtld')

def test_GoodUrlIsAccepted3():
    assert utils.validateURL('obscureprotocol://www.good.com')
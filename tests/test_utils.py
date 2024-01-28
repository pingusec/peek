import pytest
from peek import utils
from peek.utils import UrlStatus

def test_EmptyStringIsRejected():
    assert utils.validateURL('') == UrlStatus.BADLY_FORMED

def test_BadUrlIsRejected():
    assert utils.validateURL('notgood//notgood.url') == UrlStatus.BADLY_FORMED

def test_BadUrlIsRejected2():
    assert utils.validateURL('notgood') == UrlStatus.BADLY_FORMED

def test_BadUrlIsRejected3():
    assert utils.validateURL('.//.2.url') == UrlStatus.BADLY_FORMED

def test_DownUrlIsRejected():
    assert utils.validateURL('https://surely.thisisnotarejected.domain') == UrlStatus.UNREACHABLE

def test_GoodUrlIsAccepted():
    assert utils.validateURL('http://www.good.com')

def test_GoodUrlIsAccepted2():
    assert utils.validateURL('https://whotube.somerandomdomtld')

def test_GoodUrlIsAccepted3():
    assert utils.validateURL('obscureprotocol://www.good.com')
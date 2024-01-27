import pytest
from peek import utils

def test_EmptyStringIsRejected():
    assert utils.validateURL('') == False
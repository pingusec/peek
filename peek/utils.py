import os
import re
import requests
from enum import Enum

class UrlStatus(Enum):
    UP = 'up'
    UNREACHABLE = 'unreachable'
    BADLY_FORMED = 'badly forrmed',


def validateURL(test_url: str):
    """Checks if the supplied URL is valid and notifies caller on URL status"""
    if re.match(r'^.+://.+\..+', test_url) == None:
        return UrlStatus.BADLY_FORMED
    
    try:
        response = requests.head(test_url, timeout=1)

    except Exception as err:
            return UrlStatus.UNREACHABLE
    
    return UrlStatus.UP

def getScriptLocation():
    return os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))
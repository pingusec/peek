import re

def validateURL(test_url: str):
    """Checks if the supplied URL is valid"""
    if test_url == '':
        return False
    
    if re.match(r'^.+://.+\..+', test_url):
        return True
    return False

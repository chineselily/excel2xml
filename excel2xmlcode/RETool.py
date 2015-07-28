__author__ = 'Administrator'
import re

def excludeNumbers(scontent):
    result=re.match(r"[^0-9]+",scontent)
    return result.group(0)

def getNumnbers(scontent):
    result=re.match(r"[0-9]+",scontent)
    return result.group(0)
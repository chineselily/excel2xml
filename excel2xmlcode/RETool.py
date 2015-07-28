__author__ = 'Administrator'
import re

def excludeNumbers(scontent):
    result=re.search(r"[^0-9]+",scontent)
    if(result==None):
        return""
    return result.group(0)

def getNumnbers(scontent):
    result=re.search(r"[0-9]+",scontent)
    if(result==None):
        return""
    return result.group(0)
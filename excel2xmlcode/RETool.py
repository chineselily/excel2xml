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

def xmlEscape(strXml):
    pt=re.compile('".*?"',re.M|re.S)
    arrT = re.findall(pt,strXml)
    arrR=[]
    for i,v in enumerate(arrT):
        vr=v.replace("&", "&amp;")
        vr=vr.replace(">", "&gt;")
        vr=vr.replace("<", "&lt;")
        arrR.append(vr)
    for i,v in enumerate(arrR):
        strXml = strXml.replace(arrT[i],v)
    #print(strXml)
    return strXml
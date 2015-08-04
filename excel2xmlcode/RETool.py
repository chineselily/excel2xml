__author__ = 'Administrator'
import re
from excel2xmlcode import readConfig

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

def excludeWhite(scontent):
    result=re.search(r"[a-zA-Z0-9_,]+",scontent)
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
        vr=vr.replace("\n",readConfig.newlineescape)
        #tr = vr.decode(encoding='utf-8')##utf-8 string to unicode
        #tr=vr.encode(encoding='utf-8')##unicode to utf-8 string
        #print(tr)
        arrR.append(vr)
    for i,v in enumerate(arrR):
        strXml = strXml.replace(arrT[i],v)
    #print(strXml)
    return strXml

def splitStr(strr,rlen=100):
    rstr,istart,iend="",0,rlen
    while(len(rstr)<len(strr)):
        if(len(strr)-istart>rlen):
            iend=istart+rlen
        else:
            iend=len(strr)
        rstr+=strr[istart:iend]+"\n"
        istart=iend
    return rstr

def splitStrArr(arrstr,rlen=6):
     rstr,istart,iend,isplit="",0,rlen,0
     while(isplit<len(arrstr)):
        if(len(arrstr)-istart>rlen):
            iend=istart+rlen
        else:
            iend=len(arrstr)
        for i in range(istart,iend):
            rstr+=arrstr[i]+","
        rstr+="\n"
        isplit+=iend-istart
        istart=iend
     return rstr
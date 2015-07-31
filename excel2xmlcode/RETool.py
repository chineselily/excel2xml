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
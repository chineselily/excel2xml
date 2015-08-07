__author__ = 'Administrator'
from excel2xmlcode import readConfig
from excel2xmlcode import RETool
import functools
import xml.etree.ElementTree as ET
from xml.etree import ElementTree

def writeXml(spath, topelem, scode="utf-8"):
    try:
        strinit="<?xml version='1.0' encoding='UTF-8'?>"
        strinit=strinit+parseXmlToString(topelem)
        strinit=strinit.replace(readConfig.newlineescape,"\n")
        file = open(file=spath,mode='w',encoding=scode)
        file.write(strinit)
        file.close()
    except Exception as detaile:
        print(detaile)
def parseXmlToString(root,newline='\n',indent='\t'):
    return parseTreeElement(root,0,newline,indent)

def parseTreeElement(ele, hierarchy,newline,indent):
    startnamestr=newline+hierarchy*indent+'<'+ele.tag
    attribstr=parseElementAttri(ele,hierarchy,newline,indent)
    childstr=parseElementChildren(ele,hierarchy,newline,indent)
    if(len(attribstr)<=0 and len(childstr)<=0):
        return startnamestr+'/>'
    elif(len(attribstr)<=0):
        return startnamestr+'>'+childstr+newline+hierarchy*indent+'</'+ele.tag+'>'
    elif(len(childstr)<=0):
        return startnamestr+attribstr+'/>'
    else:
        return startnamestr+attribstr+'>'+childstr+newline+hierarchy*indent+'</'+ele.tag+'>'

def parseElementChildren(ele,hierarchy,newline,indent):
    arrexclude,tempr,dictag,strr,arrtags=[],[],{},"",[]
    for eles in ele:
        eletag=eles.tag
        arrtags.append(eletag)
        if(len(RETool.getNumnbers(eletag))>0):#get date tag
            tempr=dictag.get(RETool.excludeNumbers(eletag),[])
            tempr.append(eletag)
            dictag[RETool.excludeNumbers(eletag)]=tempr
    for i,v in enumerate(dictag):
        tempr=dictag[v]
        tempr.sort(reverse=True)
        arrexclude.extend(tempr[3:])#exclude old dates，同样的字段，最多只保留3个，比如persontarget20150720 persontarget20150729 persontarget20150829 persontarget20150910，只保留后三个

    arrtags.sort()# children的输出顺序进行排序
    for i,v in enumerate(arrtags):
        if(v in arrexclude):
            continue
        strr+=parseTreeElement(ele.find(v),hierarchy+1,newline,indent)
    return strr

def parseElementAttri(ele, hierarchy, newline, indent):
    strb=""
    arrkey=ele.keys()
    arrkey.sort(key=functools.cmp_to_key(strCmp))# 属性输出顺序进行排序
    for i,v in enumerate(arrkey):
        if(i==0):
            strb+=' '
        else:
            strb+=newline+hierarchy*indent+(len(ele.tag)+2)*' '
        strb+=str(v)+'='+'"'+str(ele.get(v))+'"'
    return strb

def strCmp(str1,str2):
    if(len(str1)-len(str2)==0):
        return[-1,1][str1>str2]
    return len(str1)-len(str2)
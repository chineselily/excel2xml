__author__ = 'Administrator'
from excel2xmlcode import readConfig

def writeXml(spath, topelem, scode="utf-8"):
    strinit="<?xml version='1.0' encoding='UTF-8'?>"
    strinit=strinit+writeXmlImp(topelem,"")
    strinit=strinit.replace(readConfig.newlineescape,"\n")
    file = open(file=spath,mode='w',encoding=scode)
    file.write(strinit)
    file.close()
def writeXmlImp(topelem, strenter):
    strai,stra,strcral=" ","",""
    #解析元素的属性，组合成字符串
    for i,v in enumerate(topelem.attrib):
        stra+=strai+str(v)+"="+'"'+str(topelem.get(v))+'"'+"\n"+strenter+strai
    #组合元素的头
    strr="\n"+strenter+"<"+topelem.tag+stra
    #递归组合元素的子元素
    for child in topelem:
        strcr=writeXmlImp(child,strenter+"\t")
        strcral+=strcr+strenter
    #组合元素的尾
    if(len(strcral)>0):
        strr+=">"+strcral+"\n"+strenter+"</"+topelem.tag+">"
    else:
        strr+="/>"
    return strr
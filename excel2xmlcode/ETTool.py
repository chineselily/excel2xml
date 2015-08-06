__author__ = 'Administrator'
import xml.etree.ElementTree as ET
from xml.etree import ElementTree
from xml.dom import minidom
from excel2xmlcode import RETool
from excel2xmlcode import log
from excel2xmlcode import readConfig

#原始的文件写操作
# top2 = prettify(topelem)
# file = open(file=spath,mode='w',encoding=scode)
# file.write(top2.decode(scode))
# file.close()
def prettify(elem, scode="utf-8"):
    """Return a pretty-printed XML string for the Element.
    """
    rough_string = ElementTree.tostring(elem,scode)
    reparsed = minidom.parseString(rough_string)
    return reparsed.toprettyxml(indent="\t", newl="\n", encoding=scode)

def createETRoot(rootname="root"):
    return ET.Element(rootname)

def readETRoot(spath):
    # etree=ET.parse(spath)
    # return etree.getroot()
    try:
        file=open(file=spath,mode='r',encoding="utf-8")
        str1=file.read()
        file.close()
        str2=RETool.xmlEscape(str1)
        tree = ET.ElementTree(ET.fromstring(str2))
        return tree.getroot()
    except Exception as detaile:
        log.logF("ETTool.py","readETRoot","error path="+str(spath)+" detaile="+str(detaile))
        return None

def addElement(parentelm,subtagname,attrib={}):
    return ET.SubElement(parentelm,subtagname,attrib)

def getElement(parentelm,subtagname):
    arrA=parentelm.findall(".//"+subtagname)
    if(arrA==None or len(arrA)<=0):
        arrA=[]
        arrA.append(addElement(parentelm,subtagname))
    return arrA[0]

def getAllElementNames(topelm):
    arrR=[]
    for ele in topelm:
        arrR.append(ele.tag)
    return arrR

def getElementAttri(parentelm, subtagname):
    elemt = getElement(parentelm, subtagname)
    if(elemt!=None):
        return elemt.attrib
    return None

def getElementAttriByName(parentelm, subtagname, attriname):
    elemt = getElement(parentelm, subtagname)
    return getElementAttriValue(elemt,attriname)

def getElementAttriValue(elemt, attriname):
    if(elemt!=None):
        return elemt.get(attriname)
    return None

def getElementAllAttri(parentelm,subgtagname):
    arrR=[]
    arrA=parentelm.findall(".//"+subgtagname)
    for i,v in enumerate(arrA):
        arrR.extend(v.keys())
    return arrR

def getAllParentTags(parentelm, attriname):
    arrR=[]
    strp=".//*"+"[@"+attriname+"]"+".."
    arrA=parentelm.findall(strp)
    for i,v in enumerate(arrA):
        arrR.append(v.tag)
    return arrR

def getSubElementByTag(parentelm, tagname):
    strp=".//"+tagname
    return parentelm.findall(strp)

def getParentElementByTag(topelem, tagname):
    strp=".//"+tagname+".."
    return topelem.findall(strp)

def setAttribValue(elem, attriname, attrivalue):
    if(elem!=None):
        elem.set(attriname,attrivalue)

def setElementAttriByName(parentelm,subtagname,attriname, attrivalue):
    elemt = getElement(parentelm, subtagname)
    if(elemt!=None):
        elemt.set(attriname,attrivalue)



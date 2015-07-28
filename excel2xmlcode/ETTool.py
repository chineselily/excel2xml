__author__ = 'Administrator'
import xml.etree.ElementTree as ET
from xml.etree import ElementTree
from xml.dom import minidom

def writeXml(spath, topelem, scode="utf-8"):
    top2 = prettify(topelem)
    file = open(file=spath,mode='w',encoding=scode)
    file.write(top2.decode(scode))
    file.close()

def prettify(elem, scode="utf-8"):
    """Return a pretty-printed XML string for the Element.
    """
    rough_string = ElementTree.tostring(elem,scode)
    reparsed = minidom.parseString(rough_string)
    return reparsed.toprettyxml(indent="\t", newl="\n", encoding=scode)

def createETRoot(rootname="root"):
    return ET.Element(rootname)

def readETRoot(spath):
    etree=ET.parse(spath)
    return etree.getroot()

def addElement(parentelm,subtagname):
    return ET.SubElement(parentelm,subtagname)

def appendElement(parentelm, subelm):
    parentelm.append(subelm)

def getElement(parentelm,subtagname):
    et=parentelm.find(subtagname)
    if(et==None):
        et=addElement(parentelm,subtagname)
    return et

def getAllElementNames(topelm):
    arrR=[]
    for ele in topelm:
        arrR.append(ele.tag)
    return arrR

def getElementByAttrib(parentelm, subtagname,attribname,attribvalue):
    arrElem=parentelm.findall(subtagname)
    for ele in arrElem:
        if(ele.get(attribname)==attribvalue):
            return ele
    return None

def getElementText(parentelm, subtagname):
    elemt = getElement(parentelm,subtagname)
    if(elemt!=None):
        return elemt.text
    return None

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

def getElementAllAttriByName(parentelm,subgtagname, arrtriname):
    arrR=[]
    arrElem=parentelm.findall(subgtagname)
    for ele in arrElem:
        arrR.append(ele.get(arrtriname))
    return arrR

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

def setElementAttriByName(parentelm,subtagname,attriname, attrivalue):
    elemt = getElement(parentelm, subtagname)
    if(elemt!=None):
        elemt.set(attriname,attrivalue)

def getXmlElemDescribe(self,elem):
    str1 = " tag=",elem.tag," attrib=",elem.attrib," text=",elem.text
    return str1

def splitstr(strt,sep=','):
    if(strt!=None):
        return strt.rsplit(sep)
    return []


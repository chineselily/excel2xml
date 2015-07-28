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

def createETRoot(rootname):
    return ET.Element(rootname)

def addElement(parentelm,subtagname):
    return ET.SubElement(parentelm,subtagname)

def getElement(parentelm,subtagname):
    et=parentelm.find(subtagname)
    if(et==None):
        et=addElement(parentelm,subtagname)
    return et

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
    if(elemt!=None):
        return elemt.get(attriname)
    return None

def getElementAllAttriByName(parentelm,subgtagname, arrtriname):
    arrR=[]
    arrElem=parentelm.findall(subgtagname)
    for ele in arrElem:
        arrR.append(ele.get(arrtriname))
    return arrR

def setElementAttriByName(parentelm,subtagname,attriname, attrivalue):
    elemt = getElement(parentelm, subtagname)
    if(elemt!=None):
        elemt.set(attriname,attrivalue)

def splitstr(strt,sep=','):
    if(strt!=None):
        return strt.rsplit(sep)
    return []


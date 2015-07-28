__author__ = 'Administrator'
import xml.etree.ElementTree as ET
from excel2xmlcode import log
import excel2xmlcode.ETTool as ETTool

class ToolConfig:

    configtree=None

    def readConfig(self,spath):
        ToolConfig.configtree = ET.parse(spath)

    def logType(self):
        rv=ETTool.getElementText(ToolConfig.configtree.getroot(),"logout")
        if(rv==None):
            return 1
        return rv

    def keyColumn(self):
        rv=ETTool.getElementText(ToolConfig.configtree.getroot(),"keyColumn")
        if(rv==None):
            return "Key"
        return rv
    def defaultTagName(self):
        rv=ETTool.getElementText(ToolConfig.configtree.getroot(),"defaultTag")
        if(rv==None):
            return "Base"
        return rv

    def defaultKeyName(self):
        return "info"

    def arrActivityFileName(self):
        rv=ETTool.getElementAttriByName(ToolConfig.configtree.getroot(),"activityFileName","fileName")
        return ETTool.splitstr(rv)

    def arrLanguageName(self):
        rv=ETTool.getElementAllAttriByName(ETTool.getElement(ToolConfig.configtree.getroot(),"languagefile"),"item","lanuage")
        str1="all valid languages="+str(rv)
        log.logF("readConfig.py","arrLanguageName",str1)
        return rv

    def arrLanguageFileName(self, slanguage):
        rv=ETTool.getElementByAttrib(ETTool.getElement(ToolConfig.configtree.getroot(),"languagefile"),"item","lanuage",slanguage)
        if(rv!=None):
            return ETTool.splitstr(rv)
        return None
# def readActivityFileName(self, ele):
#     for child in ele:
#         log.logF("readConfig.py","readActivityFileName",self.getXmlElemDescribe(child))
#         self.arrActivityFileName.append(child.attrib["fileName"])
#     str1="output="+str(self.arrActivityFileName)
#     log.logF("readConfig.py","readActivityFileName",str1)

# def readFileName(self, ele):
#     for child in ele:
#         log.logF("readConfig.py","readFileName",self.getXmlElemDescribe(child))
#         self.dictLanguage2File.setdefault(child.attrib['lanuage'],child.attrib['folder'])
#     # str1="  output="
#     # str1+=dictLanguage2File["French"]
#     str1 = str(self.dictLanguage2File.keys())
#     str1+="   "+str(self.dictLanguage2File.values())
#     log.logF("readConfig.py","readFileName",str1)
    def getXmlElemDescribe(self,elem):
        str1 = " tag=",elem.tag," attrib=",elem.attrib," text=",elem.text
        return str1
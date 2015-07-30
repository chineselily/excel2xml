__author__ = 'Administrator'
import xml.etree.ElementTree as ET
from excel2xmlcode import log
import excel2xmlcode.ETTool as ETTool

class ToolConfig:

    configroot=None
    #excelpath="languageinput/[Flower Shop] Multi-Language Translation Sentence Form.xlsx"
    xmlpath="languageoutput/"

    def readConfig(self,spath):
        ToolConfig.configroot = ETTool.readETRoot(spath)

    def logType(self):
        rv=ETTool.getElementText(ToolConfig.configroot,"logout")
        if(rv==None):
            return 1
        return rv

    def keyColumn(self):
        rv=ETTool.getElementText(ToolConfig.configroot,"keyColumn")
        if(rv==None):
            return "Key"
        return rv
    def defaultTagName(self):
        rv=ETTool.getElementText(ToolConfig.configroot,"defaultTag")
        if(rv==None):
            return "base"
        return rv

    def defaultKeyName(self):
        return "info"

    def arrActivityFileName(self):
        rv=ETTool.getElementAttriByName(ToolConfig.configroot,"activityFileName","fileName")
        return ETTool.splitstr(rv)

    def arrLanguageName(self):
        rv=ETTool.getElementAllAttriByName(ETTool.getElement(ToolConfig.configroot,"languagefile"),"item","lanuage")
        str1="all valid languages="+str(rv)
        log.logF("readConfig.py","arrLanguageName",str1)
        return rv

    def arrLanguageFileName(self, slanguage):
        rv=ETTool.getElementByAttrib(ETTool.getElement(ToolConfig.configroot,"languagefile"),"item","lanuage",slanguage)
        astr=ETTool.getElementAttriValue(rv,"folder")
        if(astr!=None):
            return ETTool.splitstr(astr)
        return None

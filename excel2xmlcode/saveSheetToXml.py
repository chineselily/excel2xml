__author__ = 'Administrator'
from excel2xmlcode.readXlsx import LanguageSheet
from excel2xmlcode import RETool
from excel2xmlcode import ETTool
from excel2xmlcode.readConfig import ToolConfig
import os.path

class SaveSheet:
    toolc=ToolConfig()
    sheet=None
    def save(self, sheet):
        self.sheet=sheet
        filename=RETool.excludeNumbers(sheet.stitle)
        languageNames=ETTool.getAllElementNames(sheet.lstree)
        print("filename="+filename+"  languageNames=",str(languageNames))

        for i,v in enumerate(languageNames):
           arrLangFile=SaveSheet.toolc.arrLanguageFileName(v)
           for j,k in enumerate(arrLangFile):
            xfilename=SaveSheet.toolc.xmlpath+k+"/"+filename+".xml"
            langmentr=ETTool.getElement(sheet.lstree,v)
            if(os.path.isfile(xfilename)):
                self.mergeOneLanguage(xfilename,langmentr[0])
            else:
                rroot=ETTool.createETRoot()
                ETTool.appendElement(rroot,langmentr[0])
                self.writeOneLanguage(xfilename,rroot)

    def mergeOneLanguage(self, spath,sheet):
        oldxmlroot=ETTool.readETRoot(spath)
        allkeys=ETTool.getElementAllAttri(sheet,SaveSheet.toolc.defaultKeyName())
        alltags=ETTool.getAllParentTags(oldxmlroot,allkeys[0])
        self.appendXmlElement(oldxmlroot,alltags)

    def appendXmlElement(self, oldxmlroot, alltags):
        righttag1=RETool.excludeNumbers(alltags[0])
        rightag2=RETool.getNumnbers(self.sheet.stitle)
        righttag=righttag1+rightag2
        if(alltags.count(righttag)>0):
            return
        ele=ETTool.getSubElementByTag(oldxmlroot,alltags[0])[0]
        arrpele=ETTool.getParentElementByTag(oldxmlroot,alltags[0])
        pele=None
        if(len(arrpele)>0):
            pele=arrpele[0]
        else:
            pele=oldxmlroot
        ele.tag=righttag
        ETTool.appendElement(pele,ele)
        ETTool.writeXml(self.toolc.xmlpath+"ceshi.xml",oldxmlroot)
    def writeOneLanguage(self,spath,rroot):
        ETTool.writeXml(spath,rroot)

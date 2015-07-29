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
       #遍历语言
        for i,v in enumerate(languageNames):
           arrLangFile=SaveSheet.toolc.arrLanguageFileName(v)
           for j,k in enumerate(arrLangFile):#遍历语言的对应文件
            xfilename=SaveSheet.toolc.xmlpath+k+"/"+filename+".xml"#保存的文件名字
            langmentr=ETTool.getElement(sheet.lstree,v)#对应语言的文字配置
            rroot=None
            if(os.path.isfile(xfilename)):#如果存在则合并
                rroot=ETTool.readETRoot(xfilename)
                self.mergeOneLanguage(rroot,langmentr[0])
            else:#不存在则新建
                rroot=ETTool.createETRoot()
                ETTool.appendElement(rroot,langmentr[0])
                break
            self.writeOneLanguage(xfilename,rroot)

    def mergeOneLanguage(self, oldxmlroot,sheet):
        allkeys=ETTool.getElementAllAttri(sheet,SaveSheet.toolc.defaultKeyName())
        for i,v in enumerate(allkeys):
            elem=self.appendElementToXml(oldxmlroot,v,sheet.tag)[0]
            eleminfo=ETTool.getElement(elem,SaveSheet.toolc.defaultKeyName())
            ETTool.setAttribValue(eleminfo,v,ETTool.getAttriValue(sheet,v)[0])

    def appendElementToXml(self,oldxmlroot,keyname,oldTagName):
        alltags=ETTool.getAllParentTags(oldxmlroot,keyname)
        if(len(alltags)>0):
            tagname=RETool.excludeNumbers(alltags[0])+RETool.getNumnbers(self.sheet.stitle)
        else:
            tagname=oldTagName
        if(alltags.count(tagname)<=0):#存在则不创建
            ele=ETTool.getSubElementByTag(oldxmlroot,alltags[0])[0]
            arrpele=ETTool.getParentElementByTag(oldxmlroot,alltags[0])
            pele=None
            if(len(arrpele)>0):
                pele=arrpele[0]
            else:
                pele=oldxmlroot
            #ele.tag=tagname
            pmy=ETTool.addElement(pele,tagname)
            ETTool.addElement(pmy,SaveSheet.toolc.defaultKeyName(),ETTool.getElementAttri(ele,SaveSheet.toolc.defaultKeyName()))
        return ETTool.getSubElementByTag(oldxmlroot,tagname)

    def writeOneLanguage(self,spath,rroot):
        ETTool.writeXml(spath,rroot)

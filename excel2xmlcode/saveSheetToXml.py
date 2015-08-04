__author__ = 'Administrator'
from excel2xmlcode.readXlsx import LanguageSheet
from excel2xmlcode import RETool
from excel2xmlcode import ETTool
from excel2xmlcode import readConfig
import os.path

class SaveSheet:
    sheet,arrErrorFile,arrNewFile=None,[],[]
    #将表格保存到各个语言对应的文件目录中
    def save(self, sheet):
        self.sheet=sheet
        filename=RETool.excludeNumbers(sheet.stitle)
        languageNames=ETTool.getAllElementNames(sheet.lstree)#解析出这个表格中配置了多少个语言的文字
       #遍历语言
        for i,v in enumerate(languageNames):
           arrLangFile=readConfig.arrLanguageFileName(v)
           for j,k in enumerate(arrLangFile):#遍历语言的对应文件
            xfilename=readConfig.xmlpath+k+"/"+filename+".xml"#保存的文件名字
            langmentr=ETTool.getElement(sheet.lstree,v)#对应语言的文字配置
            rroot=None
            if(os.path.isfile(xfilename)):#如果存在则合并
                rroot=ETTool.readETRoot(xfilename)
                if(rroot==None):
                    self.arrErrorFile.append(filename)
                    continue
                self.mergeOneLanguage(rroot,langmentr[0])
            else:#不存在则新建
                rroot=ETTool.createETRoot()
                ETTool.appendElement(rroot,langmentr[0])
                self.arrNewFile.append(filename)
            self.writeOneLanguage(xfilename,rroot)
    #将表格中的文字合并到.xml中
    def mergeOneLanguage(self, oldxmlroot,sheet):
        allkeys=ETTool.getElementAllAttri(sheet,readConfig.defaultKeyName)
        for i,v in enumerate(allkeys):
            elem=self.appendElementToXml(oldxmlroot,v,sheet.tag)[0]
            eleminfo=ETTool.getElement(elem,readConfig.defaultKeyName)
            ETTool.setAttribValue(eleminfo,v,ETTool.getAttriValue(sheet,v)[0])
    #判断表格中的语言配置对应的树是否存在，不存在则创建，存在则返回所对应的树结果
    def appendElementToXml(self,oldxmlroot,keyname,oldTagName):
        alltags=ETTool.getAllParentTags(oldxmlroot,keyname)
        if(len(alltags)>0):
            tagname=RETool.excludeNumbers(alltags[0])+RETool.getNumnbers(self.sheet.stitle)
        else:
            tagname=oldTagName
        if((tagname not in alltags) and len(alltags)>0):#有相同的属性关键字，但是没有相应tagname的标签值
            ele=ETTool.getSubElementByTag(oldxmlroot,alltags[0])[0]
            arrpele=ETTool.getParentElementByTag(oldxmlroot,alltags[0])
            pele=None
            if(len(arrpele)>0):
                pele=arrpele[0]
            else:
                pele=oldxmlroot
            #ele.tag=tagname
            pmy=ETTool.addElement(pele,tagname)
            ETTool.addElement(pmy,readConfig.defaultKeyName,ETTool.getElementAttri(ele,readConfig.defaultKeyName))
        elif(len(ETTool.getSubElementByTag(oldxmlroot,tagname))<=0):#没有有这个标签
            ETTool.addElement(oldxmlroot,tagname)

        return ETTool.getSubElementByTag(oldxmlroot,tagname)

    def writeOneLanguage(self,spath,rroot):
        ETTool.writeXml(spath,rroot)

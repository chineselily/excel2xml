__author__ = 'Administrator'

from excel2xmlcode.savesheet.getSheetInfos import *
from excel2xmlcode.savesheet import writeXml

class SaveSheet:
    arrErrorFile,arrNewFile,arrSuccFile=[],[],[]
    #将表格保存到各个语言对应的文件目录中
    def save(self,arrfiles):
        for i,v in enumerate(arrfiles):
            self.saveone(v[0],v[1])

    def saveone(self, filename, lstree):
        arrinfo=getSheetInfos(filename,lstree)#[filename,datename,arrerrorfiles,arrsuccessfiles,arrnewfiles,arrsheetlanguage,arrtreeinfo]
        self.arrErrorFile.extend(list(set(arrinfo[2])))
        self.arrNewFile.extend(list(set(arrinfo[4])))
        self.arrSuccFile.extend(list(set(arrinfo[3])))
        self.datetime=arrinfo[1]
        #merge the two xml tree
        for i,v in enumerate(arrinfo[5]):# v -> every language
            for k,m in enumerate(v.arroldtree): # m->language files, for example, french has fr_fr, fr_se
                self.mergeXmls(m,v.googletree)
                writeXml.writeXml(v.arrfilepath[k],m)
    #合并2个xml数据结构
    def mergeXmls(self,oldxmlroot,sheet):
        alltags=ETTool.getAllElementNames(sheet)
        for i, v in enumerate(alltags):#every tag
            allkeys=ETTool.getElementAllAttri(ETTool.getElement(sheet,v),readConfig.defaultKeyName)
            for k,m in enumerate(allkeys):#every key
                self.mergeOneKeyToXmltree(oldxmlroot,v,m,ETTool.getElementAttriByName(ETTool.getElement(sheet,v),readConfig.defaultKeyName,m))
    #合并一个属性到xml数据结构中
    def mergeOneKeyToXmltree(self,tree,tagname,keyname,keyvalue):
        newtagname=tagname
        if(tagname==readConfig.defaultTagName):
            newtagname=self.guessTag(tree,keyname,tagname)
        parenttree=self.guessParent(tree,keyname,tagname,newtagname)
        if(keyname.find(',')==-1):#single key
             ETTool.setAttribValue(ETTool.getElement(parenttree,readConfig.defaultKeyName),keyname,keyvalue)
        else:# 多个key值
            infotree=ETTool.addElement(parenttree,readConfig.defaultKeyName)
            arrkey=keyname.split(',')
            ETTool.setAttribValue(infotree,arrkey[0],keyvalue)
            for i in range(1,len(arrkey)):
                arrdic=arrkey[i].split('=')
                ETTool.setAttribValue(infotree,arrdic[0],arrdic[1])
    #猜测属性对应的TAG名
    def guessTag(self,tree,keyname,tagname):
        alltags=ETTool.getAllParentTags(tree,keyname)
        if(len(alltags)>0):
            tagname=RETool.excludeNumbers(alltags[0])+self.datetime
        return tagname
    #猜测属性对应的父
    def guessParent(self,tree,keyname,oldtagname,newtagname):
        alltags=[]
        if(oldtagname==readConfig.defaultTagName):
            alltags=ETTool.getAllParentTags(tree,keyname)
        if((newtagname not in alltags) and len(alltags)>0):#有相同的属性关键字，但是没有相应tagname的标签值
            ele=ETTool.getSubElementByTag(tree,alltags[0])[0]
            arrpele=ETTool.getParentElementByTag(tree,alltags[0])
            if(len(arrpele)>0):
                pele=arrpele[0]
            else:
                pele=tree
            #ele.tag=tagname
            pmy=ETTool.addElement(pele,newtagname)
            ETTool.addElement(pmy,readConfig.defaultKeyName,ETTool.getElementAttri(ele,readConfig.defaultKeyName))
        elif(len(ETTool.getSubElementByTag(tree,newtagname))<=0):#没有有这个标签
            ETTool.addElement(tree,newtagname)
        return ETTool.getSubElementByTag(tree,newtagname)[0]



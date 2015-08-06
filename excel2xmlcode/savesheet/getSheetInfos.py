__author__ = 'Administrator'

from excel2xmlcode import RETool
from excel2xmlcode import ETTool
from excel2xmlcode import readConfig
import os

def getSheetInfos(sheettitle,sheettree):
    arrerrorfiles,arrnewfiles,arrsuccessfiles,arrtreeinfo=[],[],[],[]
    filename=RETool.excludeNumbers(sheettitle)#文件名字可带日期
    datename=RETool.getNumnbers(sheettitle)#文件名对应的日期
    languageNames=ETTool.getAllElementNames(sheettree)#解析出这个表格中配置了多少个语言的文字
   #遍历语言
    for i,v in enumerate(languageNames):
       arrLangFile,arrfilepath,arroldtree=readConfig.arrLanguageFileName(v),[],[]
       for j,k in enumerate(arrLangFile):#遍历语言的对应文件，像法语French就对应着两个文件夹fr_fr,fr_se
            xfilename=readConfig.getOutputPath()+k+"/"+filename+".xml"#保存的文件名字
            hintfilename=k+"/"+filename
            if(False==os.path.isdir(readConfig.getOutputPath()+k)):#不存在目录
                arrerrorfiles.append(hintfilename)
                continue
            elif(os.path.isfile(xfilename)):#存在
                rroot=ETTool.readETRoot(xfilename)
                if(rroot==None):#存在的.xml文件出现错误
                    arrerrorfiles.append(hintfilename)
                    continue
                arrsuccessfiles.append(hintfilename)
            else:#不存在则新建
               rroot=ETTool.createETRoot()
               arrnewfiles.append(hintfilename)
            arrfilepath.append(xfilename)
            arroldtree.append(rroot)
       arrtreeinfo.append(sheetLanguageInfo(v,ETTool.getElement(sheettree,v),arrfilepath,arroldtree))
    return [filename,datename,arrerrorfiles,arrsuccessfiles,arrnewfiles,arrtreeinfo]

class sheetLanguageInfo:
    def __init__(self,language,googletree, arrfilepath,arroldtree):
        self.language=language
        self.googletree=googletree
        self.arrfilepath=arrfilepath
        self.arroldtree=arroldtree


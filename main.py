__author__ = 'Administrator'
from excel2xmlcode import readXlsx
from excel2xmlcode import readConfig
from excel2xmlcode import saveSheetToXml
# read config
config = readConfig.ToolConfig()
config.readConfig("languageinput/config.xml")

# read excel
readExcel = readXlsx.LanguageExcel()
arrSheetNames=readExcel.readLanguageExcel(config.excelpath)

# read each sheet
lsheet = readXlsx.LanguageSheet()
ssheet=saveSheetToXml.SaveSheet()
for i,v in enumerate(arrSheetNames):
    lsheet.readSheet(v)
    ssheet.save(lsheet)


#writeXlsx.writeSimpleXlsx()
# from xml.sax.saxutils import escape
# from excel2xmlcode import ETTool
# from excel2xmlcode import RETool
# def testRead(spath):
#     file=open(file=spath,mode='r',encoding="utf-8")
#     str1=file.read()
#     str2=escape(str1)
#     RETool.xmlEscape(str1)
#     # print(str1)
#     # print(str2)
#     # ETTool.readETRoot(str2)
#
# testRead("languageoutput/ru_ru/persontarget.xml")
# #testRead("languageoutput/zh_tw/flowerExpo.xml")
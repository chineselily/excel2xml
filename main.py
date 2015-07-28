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
    #lsheet.writeSheetToXMl()
#writeXlsx.writeSimpleXlsx()
__author__ = 'Administrator'
from excel2xmlcode import readXlsx
from excel2xmlcode import readConfig
# read config
config = readConfig.ToolConfig()
config.readConfig("languageinput/config.xml")

# read excel
readExcel = readXlsx.LanguageExcel()
arrSheetNames=readExcel.readLanguageExcel("languageinput/[Flower Shop] Multi-Language Translation Sentence Form.xlsx")

# read each sheet
dicSheet=dict()
for i,v in enumerate(arrSheetNames):
    lsheet=readXlsx.LanguageSheet()
    lsheet.readSheet(v)
    lsheet.writeSheetToXMl()
    dicSheet[lsheet.stitle]=lsheet
#writeXlsx.writeSimpleXlsx()
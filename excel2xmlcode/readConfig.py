__author__ = 'Administrator'

from excel2xmlcode.utils.app.AppData import AppData

xmlpath="languageoutput/"
keyColumn="Key"
tagColumn="TagName"
fileColumn="FileName"
defaultTagName="base"
defaultKeyName="info"
arrLanguageName=["Chinese","English","German","Dutch","French","Spanish","Portuguese","Italian","Russian"]
dicLanguageFiles={"Chinese":["zh_tw"],"English":["en_us"],"German":["de_de","de_se"],
                  "Dutch":["nl_nl","nl_se"],"French":["fr_fr","fr_se"],"Spanish":["es_es"],
                  "Portuguese":["pt_pt"],"Italian":["it_it"],"Russian":["ru_ru"]}
newlineescape="newlineescape"

appd=AppData()

def arrLanguageFileName(slanguage):
    return dicLanguageFiles.get(slanguage,[])

def getExcelPath():
    return appd.getAppData("excelpath")

def getExcelName():
    path=getExcelPath()
    arrfiles=path.split('/')
    if(len(arrfiles)<=1):
        arrfiles=path.split('//')
    if(len(arrfiles)>=1):
        return arrfiles[len(arrfiles)-1]
    return ""

def saveExcelPath(spath):
    appd.saveAppData("excelpath",spath)

def getOutputPath():
    return appd.getAppData("outputpath")

def saveOutputPath(spath):
    appd.saveAppData("outputpath",spath)




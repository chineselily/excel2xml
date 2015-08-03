__author__ = 'Administrator'
from excel2xmlcode import log
import excel2xmlcode.ETTool as ETTool

xmlpath="languageoutput/"
keyColumn="Key"
defaultTagName="base"
defaultKeyName="info"
arrLanguageName=["Chinese","English","German","Dutch","French","Spanish","Portuguese","Italian","Russian"]
dicLanguageFiles={"Chinese":["zh_tw"],"English":["en_us"],"German":["de_de","de_se"],
                  "Dutch":["nl_nl","nl_se"],"French":["fr_fr","fr_se"],"Spanish":["es_es"],
                  "Portuguese":["pt_pt"],"Italian":["it_it"],"Russian":["ru_ru"]}

def arrLanguageFileName(slanguage):
    return dicLanguageFiles[slanguage]



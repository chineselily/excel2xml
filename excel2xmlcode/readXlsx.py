__author__ = 'Administrator'
import datetime
from openpyxl import load_workbook
from excel2xmlcode import log

class LanguageExcel:
    wb,arr_sheet_names=None,[]

    def readLanguageExcel(self, spath):
        time1=datetime.datetime.now()
        self.wb = load_workbook(spath,True)
        self.arr_sheet_names=self.wb.get_sheet_names()
        time2=datetime.datetime.now()
        str1="read "+spath+" file taken "+ str(time2-time1)+" 秒"
        log.logF("readXlsx.py","readLanguageExcel",str1)
    #获取需要解析的sheet
    def getNeedParseSheets(self, arrSheetNames):
        arrR=[]
        for i,v in enumerate(arrSheetNames):
            if(v in self.arr_sheet_names):
                   arrR.append(self.wb.get_sheet_by_name(v))
        return arrR

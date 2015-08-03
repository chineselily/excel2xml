__author__ = 'Administrator'
import datetime
from openpyxl import load_workbook
from excel2xmlcode import log
from excel2xmlcode import readConfig
import excel2xmlcode.ETTool as ETTool

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

class LanguageSheet:
    lsws,ls_max_column,ls_max_row,lstree,stitle,ckey_colunm,ckey_row=None,1,1,None,"",None,None
    arrColumnSign=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

    def readSheet(self, tws):
        self.lsws=tws
        self.stitle=self.lsws.title
        self.ls_max_column=self.lsws.max_column
        self.ls_max_row=self.lsws.max_row
        self.lstree=ETTool.createETRoot("root")
        #解析表格
        self.rowDirectionRead()

    #横向的形式读取表格,将表格中文字配置解析成XML。首先以语言划分，然后再以TAG,Key,attribute划分存储
    def rowDirectionRead(self):
        strend=str(self.last_column_sign)+str(self.ls_max_row)
        strend='A1:'+strend
        time1=datetime.datetime.now()
        for row in self.lsws.iter_rows(strend):
            for cell in row:
                self.getKeyColumn(cell)
                if(self.isValidRow(cell)==False):
                    break
                if(self.isValidCell(cell)==False):
                    continue
                languageN=self.getLanguageName(cell)
                keyN=self.getKeyName(cell)
                if(keyN==None or languageN==None):
                    continue
                let=ETTool.getElement(self.lstree,languageN)
                taget=ETTool.getElement(let,self.getTagName(cell))
                ETTool.setElementAttriByName(taget,readConfig.defaultKeyName,keyN,cell.value)
                str1="value="+str(cell.value)+" column="+str(cell.column)+" row="+str(cell.row)
                log.logF("readXlsx.py","rowDirectionRead",str1)
        time2=datetime.datetime.now()
        str1="read "+self.stitle+" sheet taken "+ str(time2-time1)+" 秒"
        log.logF("readXlsx.py","rowDirectionRead",str1)

    def getLanguageName(self,cell):
        if(cell.column==None or cell.row==None or self.ckey_row==None or self.ckey_colunm==None):
            return None
        difc=self.get_column_sign_to_int(cell.column)-self.get_column_sign_to_int(self.ckey_colunm)-1
        if(difc%2 !=0 ):#要求语言的描述配置项有一定的规则：key ,Chinse,clen,English,clen,German....
            return None
        cellL=self.lsws.cell(self.changeCoordinate(self.ckey_row,cell.column))
        return cellL.value

    def getTagName(self,cell):
        keyindex=self.arrColumnSign.index(self.ckey_colunm)
        if(keyindex<=0):
            return readConfig.defaultTagName
        cellt=self.lsws.cell(self.changeCoordinate(cell.row,self.arrColumnSign[keyindex-1]))
        if(cellt.value==None):
            return readConfig.defaultTagName
        return cellt.value

    def getKeyName(self,cell):
        cellk=self.lsws.cell(self.changeCoordinate(cell.row,self.ckey_colunm))
        return cellk.value

    def getKeyColumn(self,cell):
        if(self.ckey_colunm==None and cell.value==readConfig.keyColumn):
            self.ckey_colunm=cell.column
            self.ckey_row=cell.row

    def isValidRow(self,cell):
        if(self.ckey_colunm==None or
        (cell.column==self.ckey_colunm and (cell.value==None or cell.value==readConfig.keyColumn))):
            return False
        return True

    def isValidCell(self,cell):
        if(cell.column==None or cell.row==None or cell.value==None or cell.value==readConfig.keyColumn or cell.column==self.ckey_colunm):#没有内容不解析此cell
            return False
        return True

    def changeCoordinate(self,row,column):
        strR=str(column)+str(row)
        return strR
    @property
    def first_column_sign(self):
        return 'A'
    @property
    def last_column_sign(self):
        return self.get_column_sign_by_arr_index(self.ls_max_column)
    # 现在只支持column从A-ZZ，一共26！个列数目
    def get_column_sign_by_arr_index(self,ilen):
        imt=ilen // len(self.arrColumnSign)
        # too big i have to make it shortter
        if(imt>1):
            imt=1
        irt=int(ilen % len(self.arrColumnSign))
        cct=self.arrColumnSign[irt-1]
        if(imt>0):
            cct=self.arrColumnSign[imt-1]+cct
        return cct

    def get_column_sign_to_int(self,ccolum):
        if(len(ccolum)>1):
            return 26*(self.arrColumnSign.index(ccolum[1])+1)+self.arrColumnSign.index(ccolum[0])+1
        else:
            return self.arrColumnSign.index(ccolum[0])+1
     #纵向的形式读取表格
    def colDirectionRead(self):
        #这里大概要做3次循环,
        # 第一次是循环有多个列 title_txt对应一个纵行，desc_txt 对应一个纵行
        # 第二次，第三次循环就对应着和rowDirectionRead一样的循环范围
        # 范围的计算要根据语言个数，假设有7个语言，就是A1-A7，B1-B7，C1-C7........
        print()
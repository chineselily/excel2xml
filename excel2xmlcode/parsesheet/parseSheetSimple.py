__author__ = 'Administrator'
from openpyxl.utils import *
from excel2xmlcode import readConfig
import excel2xmlcode.ETTool as ETTool
from excel2xmlcode.savesheet import writeXml
import datetime

def parseSimpleSheet(sheet, minrow, maxrow, mincol, maxcol, keycol,keyrow,lstree,tagname=readConfig.defaultTagName):
    if(lstree==None):
        lstree=ETTool.createETRoot("root")
    for row in sheet.get_squared_range(mincol,minrow,maxcol,maxrow):
        for cell in row:
            if(cell.column==None or cell.row==None or cell.value==None):#not valid cell
                continue
            if((column_index_from_string(cell.column) - keycol)%2==0 or (column_index_from_string(cell.column)==keycol)):# 语言配置项所在的col和key所在的col相差是有规律的
                continue
            keyname=sheet.cell(row=cell.row,column=keycol).value
            lanuagename=sheet.cell(row=keyrow,column=column_index_from_string(cell.column)).value
            if(keyname==None or lanuagename==None): #没有语言项 或 没有键值
                continue
            let=ETTool.getElement(lstree,lanuagename)
            taget=ETTool.getElement(let,tagname)
            ETTool.setElementAttriByName(taget,readConfig.defaultKeyName,keyname,cell.value)
    writeXml.writeXml("languageoutput/xoutput.xml",lstree)
    return lstree
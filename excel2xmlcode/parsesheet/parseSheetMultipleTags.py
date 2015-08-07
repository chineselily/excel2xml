__author__ = 'Administrator'
import excel2xmlcode.ETTool as ETTool
from excel2xmlcode.savesheet import writeXml
from excel2xmlcode.parsesheet import parseSheetSimple

def parseMultipleTagsSheet(sheet, minrow, maxrow, mincol, maxcol, keycol,keyrow):
    lstree,dictag,lasttag,endtag=ETTool.createETRoot("root"),{},None,None
    for tagrow in range(minrow,maxrow):#查找表格有多少个TAG，并且记录每个TAG的起始minrow,maxrow
        arrtag=[]
        try:
            cell = sheet.cell(row=tagrow,column=mincol-1)
            cellkey=sheet.cell(row=tagrow,column=mincol)
        except Exception as detaile:
            print(detaile)
            continue
        if(cell.column==None or cell.row==None or cell.value==None or cellkey.column==None or cellkey.row==None or cellkey.value==None):
            continue
        if(dictag.get(cell.value)!=None):
            continue
        if(lasttag==None or lasttag!=cell.value):#first one  or different one
            arrtag.extend([cell.value,cell.row])
            dictag[cell.value]=arrtag
            if(lasttag!=None):
                arrlasttag=dictag[lasttag]
                arrlasttag.extend([cell.row-1])
            lasttag=cell.value
        endtag=cell.value
    if(endtag!=None):
        arrlasttag=dictag[endtag]
        arrlasttag.extend([maxrow])

    for i,v in enumerate(dictag):
        arrtag=dictag[v]
        parseSheetSimple.parseSimpleSheet(sheet,arrtag[1],arrtag[2],mincol,maxcol,keycol,keyrow,lstree,v)
    writeXml.writeXml("languageoutput/xmtagoutput.xml",lstree)
    return lstree
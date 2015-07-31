__author__ = 'Administrator'

from excel2xmlcode import readXlsx
from excel2xmlcode import saveSheetToXml
from excel2xmlcode import readConfig
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import askdirectory
from tkinter import *

class ToolUI:
    arrMergeSheets=[]

    def __init__(self):
        self.root = Tk()
        self.root.title('合并google excel到多语言包')    #定义窗体标题
        self.root.geometry('760x650')
        self.chooseexcel=textAndButton(self.root,"选择需要转换的excel",self.getExcelFile)
        self.chooseoutput=textAndButton(self.root,"选择导出的目录",self.getOutPutDirectory)
        self.root.mainloop()

    def getExcelFile(self):
        tk=Tk()
        tk.withdraw() # we don't want a full GUI, so keep the root window from appearing
        options = {}
        options['defaultextension'] = '.xlsx'
        options['filetypes'] = [('excel files', '.xlsx')]
        options['initialdir'] = 'D:\\'
        options['initialfile'] = 'language.xlsx'
        #options['parent'] = root
        options['title'] = '选择转换的excel'
        self.excelpath = askopenfilename(**options) # show an "Open" dialog box and return the path to the selected file
        self.chooseexcel.setText(self.excelpath)
        tk.destroy()

    def getOutPutDirectory(self):
        tk=Tk()
        tk.withdraw() # we don't want a full GUI, so keep the root window from appearing
        options = {}
        options['initialdir'] = 'D:\\'
        options['title'] = '选择多语言文字导出目录'
        self.filedirctory=askdirectory(**options)
        self.chooseoutput.setText(self.filedirctory)
        readConfig.ToolConfig.xmlpath=self.filedirctory+"/"
        tk.destroy()
        #read excel
        self.readExcel = readXlsx.LanguageExcel()
        self.readExcel.readLanguageExcel(self.excelpath)
        self.getNeedChangeFiles(self.readExcel.arr_sheet_names)

    def getNeedChangeFiles(self, arrFiles):
        self.selectexcelhint=Label(self.root,text="请选择需要导出的表格").pack(side=TOP)
        self.excelbar=Checkbar(self.root,arrFiles)
        self.mergebtn=Button(self.root,text="开始导出已选择的表格",fg="red",command=self.startMerge).pack(side=TOP)

    def startMerge(self):
        arrselectnames=self.excelbar.getStates()
        arrselectnames=self.selectNeedMergeFiles(arrselectnames)
        arrSheetNames=self.readExcel.getNeedParseSheets(arrselectnames)
        if(len(arrSheetNames)<=0):
            return
        lsheet = readXlsx.LanguageSheet()
        ssheet=saveSheetToXml.SaveSheet()
        for i,v in enumerate(arrSheetNames):
            lsheet.readSheet(v)
            ssheet.save(lsheet)
        self.doneHint(ssheet.arrErrorFile,ssheet.arrNewFile, arrselectnames)

    def doneHint(self,arrError,arrNew, arrMergeAll):
        strd=""
        if(len(arrError)>0):
            strd+="加载出现错误的文件："+"\n"
        for i,v in enumerate(arrError):
            strd+=v+", "

        if(len(arrNew)>0):
            strd+="\n"+"找不到合并文件，新创建的文件有："+"\n"
        for i,v in enumerate(arrNew):
            strd+=v+", "

        strd+="\n合并完成文件有："+"\n"
        for i,v in enumerate(arrMergeAll):
            if(v not in arrNew):
                strd+=v+", "

        donelabel=Label(self.root,text=strd).pack(side=TOP)

        ceshi=Label(self.root,text="左下").pack(side=BOTTOM and LEFT)

    def selectNeedMergeFiles(self,arruserselects):
        arrR=[]
        for i,v in enumerate(arruserselects):
            if(v not in self.arrMergeSheets):
                arrR.append(v)
        self.arrMergeSheets.extend(arrR)
        return arrR
class textAndButton:
    def __init__(self, master, btntext, clickfunction):
        #构造函数里传入一个父组件(master),创建一个Frame组件并显示
        self.root=master
        self.fm = Frame(master)

        self.fm1 = Frame(self.fm)
        button = Button(self.fm1, text=btntext, fg="red", command=clickfunction).pack(side=TOP, anchor=W, expand=NO) #此处side为LEFT表示将其放置 到frame剩余空间的最左方
        self.fm1.pack(side=LEFT, fill=BOTH, expand=NO)

        self.fm2 = Frame(self.fm)
        label=Label(self.fm2,fg="red",text="").pack(side=TOP, anchor=W, expand=NO)
        self.fm2.pack(side=LEFT,  fill=BOTH)

        self.fm.pack(side=TOP,fill=BOTH)
    def setText(self,textstr):
        for i,v in enumerate(self.fm2.children):
            self.fm2.children[v].pack_forget()

        label=Label(self.fm2,fg="red",text=textstr).pack(side=TOP, anchor=W, expand=NO)
        self.fm2.pack(side=LEFT,  fill=BOTH)

class Checkbar:
    def __init__(self, master, arrfiles):
        self.fm = Frame(master)
        self.vars,self.names,arrfm,icol,icolnum = [],arrfiles,[],0,4

        while(icol<len(arrfiles)//icolnum+1):
            fmk = Frame(self.fm)
            arrfm.append(fmk)
            icol+=1

        for i,v in enumerate(self.names):
             fmk=arrfm[i//icolnum]
             var = IntVar()
             chk = Checkbutton(fmk, text=v, variable=var)
             chk.pack(side=LEFT, anchor=W, expand=NO)
             self.vars.append(var)

        for i,v in enumerate(arrfm):
             v.pack(side=TOP,fill=BOTH)

        self.fm.pack(side=TOP,fill=BOTH)

    def getStates(self):
        arrR=[]
        for i,v in enumerate(self.vars):
            if(v.get()==1):
                arrR.append(self.names[i])
        return arrR

    def destroy(self):
        self.fm.destroy()
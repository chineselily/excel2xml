__author__ = 'Administrator'

from excel2xmlcode import readXlsx
from excel2xmlcode import saveSheetToXml
from excel2xmlcode import readConfig
from excel2xmlcode import RETool
from excel2xmlcode.UI.scrollFrame import VerticalScrolledFrame
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import askdirectory
from tkinter import *

class ToolUI:
    arrMergeSheets=[]

    def __init__(self):
        self.root = Tk()
        self.root.title('合并google excel到多语言包')    #定义窗体标题
        self.root.geometry('760x650')
        self.topselectframe=topFrame(self.root,self.readExcel)
        self.midformframe=midFormFrame(self.root,self.startMerge)
        self.bottomframe=bottomHintFrame(self.root)
        self.root.mainloop()
    #解析已选择的excel
    def readExcel(self):
        #read excel
        self.readExcel = readXlsx.LanguageExcel()
        self.readExcel.readLanguageExcel(self.topselectframe.excelpath)
        #将解析完的表格输出
        self.midformframe.freshForms(self.readExcel.arr_sheet_names)
        readConfig.saveExcelPath(self.topselectframe.excelpath)
        readConfig.saveOutputPath(self.topselectframe.filedirctory)
    #将excel合并到导出目录的xml中
    def startMerge(self):
        arrselectnames=self.selectNeedMergeFiles(self.midformframe.selectnames)
        arrSheetNames=self.readExcel.getNeedParseSheets(arrselectnames)
        if(len(arrSheetNames)<=0):
            return
        lsheet = readXlsx.LanguageSheet()
        ssheet=saveSheetToXml.SaveSheet()
        for i,v in enumerate(arrSheetNames):
            lsheet.readSheet(v)
            ssheet.save(lsheet)
        self.bottomframe.flesh(ssheet.arrErrorFile,ssheet.arrNewFile,ssheet.arrSuccFile)

    def selectNeedMergeFiles(self,arruserselects):
        arrR=[]
        for i,v in enumerate(arruserselects):
            if(v not in self.arrMergeSheets):
                arrR.append(v)
        self.arrMergeSheets.extend(arrR)
        return arrR

class topFrame:
    def __init__(self,master, allselectedcommand):
        self.master=master
        self.allselectedcommand=allselectedcommand
        #选择需要转换的表格
        eframe=Frame(master,name="excelselectframe")# excel select frame
        b1=Button(eframe, text="选择需要转换的excel", fg="red", command=self.b1click, name="selectexcelbtn").pack(side=LEFT, anchor=W, expand=NO) #此处side为LEFT表示将其放置 到frame剩余空间的最左方
        l1=Label(eframe,text="",fg="red",name="selectexcellabel").pack(side=LEFT,anchor=W,expand=YES)
        eframe.pack(side=TOP,fill=BOTH)
        #选择需要输出的目录
        oframe=Frame(master,name="outputselectframe")# output select frame
        b2=Button(oframe, text="选择导出的目录", fg="red", command=self.b2click, name="selectdirbtn").pack(side=TOP and LEFT, anchor=W, expand=NO) #此处side为LEFT表示将其放置 到frame剩余空间的最左方
        l2=Label(oframe,text="",fg="red",name="selectdirlabel").pack(side=LEFT,anchor=W)
        oframe.pack(side=TOP,fill=BOTH)

    def b1click(self):
        tk=Tk()
        tk.withdraw() # we don't want a full GUI, so keep the root window from appearing
        options = {}
        options['defaultextension'] = '.xlsx'
        options['filetypes'] = [('excel files', '.xlsx')]
        options['initialdir'] = readConfig.getExcelPath()
        options['initialfile'] = 'language.xlsx'
        #options['parent'] = root
        options['title'] = '选择转换的excel'
        self.excelpath = askopenfilename(**options) # show an "Open" dialog box and return the path to the selected file
        self.master.children["excelselectframe"].children["selectexcellabel"]['text']=self.excelpath
        tk.destroy()
    def b2click(self):
        tk=Tk()
        tk.withdraw() # we don't want a full GUI, so keep the root window from appearing
        options = {}
        options['initialdir'] = readConfig.getOutputPath()
        options['title'] = '选择多语言文字导出目录'
        self.filedirctory=askdirectory(**options)
        self.master.children["outputselectframe"].children["selectdirlabel"]['text']=self.filedirctory
        self.filedirctory+="/"
        tk.destroy()
        self.allselectedcommand()
class midFormFrame:
    def __init__(self,master,mergefun):
        self.master=master
        self.vars,self.varnames,self.selectnames=[],[],[]
        self.mergefun=mergefun
        allframe=Frame(master,name="midFormFrameAll")

        formframe=Frame(allframe,name="formframe")
        self.scrollformframe=VerticalScrolledFrame(formframe)
        self.scrollformframe.pack()
        formframe.pack(side=LEFT,anchor=W)

        hintframe=Frame(allframe,name="hintframe")
        lht=Label(hintframe,text="请到滚动列表中选择表格",fg="red").pack(side=TOP)
        lh=Label(hintframe,text="被选中的表格中的内容将被\n导出到'选择导出的目录'\n相应的文件中\n比如选中了persontarget表格\n将会被导出到persontarget.xml\n如果找不到persontaget.xml\n则会新建一个persontarget.xml文件")\
            .pack(side=TOP,anchor=W,expand=YES)
        lb=Button(hintframe,text="开始导出",fg="red",command=self.startMerge).pack(side=TOP)
        hintframe.pack(side=LEFT,anchor=W,expand=YES,padx=150)

        allframe.pack(side=TOP)
        lselect=Label(master,fg="red",name="selectformhint",text="").pack(side=TOP)

    def freshForms(self,arrforms):
        for i,v in enumerate(arrforms):
             var = IntVar()
             chk = Checkbutton(self.scrollformframe.interior, text=v, variable=var,command=self.checkBtnClick)
             chk.pack(side=TOP, anchor=W, expand=NO)
             self.vars.append(var)
             self.varnames.append(v)
    def checkBtnClick(self):
        self.selectnames=[]
        for i,v in enumerate(self.vars):
            if(v.get()==1):
                self.selectnames.append(self.varnames[i])
        self.master.children["selectformhint"]["text"]="已选择的表格："+RETool.splitStrArr(self.selectnames,5)

    def startMerge(self):
        self.mergefun()
class bottomHintFrame:
    def __init__(self,master):
        self.master=master
        self.langdic={}
        ballframe=Frame(master,name="bottomHintFrameAllFrame")

        leftframe=Frame(ballframe,name="leftframe")
        Label(leftframe,text="以下是语言对应的导出目录(可编辑)",fg="red").pack(side=TOP)
        formframe=Frame(leftframe)
        self.scrollformframe=VerticalScrolledFrame(formframe)
        for i,v in enumerate(readConfig.arrLanguageName):
            ed=editLabel(self.scrollformframe.interior,v, ','.join([str(x) for x in readConfig.arrLanguageFileName(v)]))
            self.langdic[v]=ed.entry()

        self.scrollformframe.pack()
        formframe.pack(side=TOP)
        leftframe.pack(side=LEFT,fill=BOTH)#不 fill=BOTH简直没有办法左对齐

        rightframe=Frame(ballframe,name="rightframe")
        Label(rightframe,text="导出结果：",name="hinttext").pack(side=TOP,fill=X)
        rightframe.pack(side=LEFT,fill=BOTH)

        ballframe.pack(side=TOP,fill=BOTH)

    def flesh(self,arrerror,arrnew,arrall):
        arrmerge=[]
        for i,v in enumerate(arrall):
            if((v not in arrnew) and(v not in arrerror)):
                arrmerge.append(v)
        str="导出完成："+"\n"
        str+=self.getStr(arrerror,".xml文件导出错误：")
        str+=self.getStr(arrnew,"成功新建.xml文件：")
        str+=self.getStr(arrmerge,"成功导出.xml文件：")
        self.master.children["bottomHintFrameAllFrame"].children['rightframe'].children['hinttext']['text']=str

    def getStr(self,arrfiles,shint):
        rstr=""
        if(len(arrfiles)>0):
            rstr+=shint+"\n"+RETool.splitStrArr(arrfiles,4)+"\n"
        return rstr

    def getLangFiles(self):
        rdic={}
        for i,v in enumerate(self.langdic):
            rdic[v]=self.langdic[v].get()
        return rdic
class editLabel:
    def __init__(self, master,ltext,etext=""):
        self.master=master
        self.frame=Frame(master)
        Label(self.frame, text=ltext).grid(row=0,column=0)
        self.e1 = Entry(self.frame)
        self.e1.insert(0,etext)
        self.e1.grid(row=0, column=1)
        self.frame.pack(side=TOP)
    def entry(self):
        return self.e1
__author__ = 'Administrator'
from tkinter import Tk
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import askdirectory

def getExcelFile():
    Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
    options = {}
    options['defaultextension'] = '.xlsx'
    options['filetypes'] = [('excel files', '.xlsx')]
    options['initialdir'] = 'D:\\'
    options['initialfile'] = 'language.xlsx'
    #options['parent'] = root
    options['title'] = '选择转换的excel'
    filename = askopenfilename(**options) # show an "Open" dialog box and return the path to the selected file
    print(filename)

def getOutPutDirectory():
    options = {}
    options['initialdir'] = 'D:\\'
    options['title'] = '选择输出目录'
    filedirctory=askdirectory(**options)
    print(filedirctory)

#tkMessageBox.showerror("Open Source File", "Failed to read file \n'%s'"%filename)
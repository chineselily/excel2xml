'''
Created on 2015年7月29日

@author: Vector
'''
import json
from excel2xmlcode.utils.file.FileUtil import readFile


class AppConfig(object):
    '''
    app 的静态配置数据，通常是不需要修改的配置
    dataPath: 配置文件路径
    '''
    def __init__(self,dataPath="appdata/appdata.json"):
        self.app_data = None;
        self.data_path = dataPath;
    
    def getAppData(self, prop):
        '''
            read property from save file
        '''
        self.readData();
        try:
            return self.app_data[prop];
        except:
            return None;    
        
        
    def readData(self):
        if None==self.app_data:
            content = readFile(self.data_path);
            if None==content:
                self.app_data = {};
            else:
                self.app_data = json.loads(content);
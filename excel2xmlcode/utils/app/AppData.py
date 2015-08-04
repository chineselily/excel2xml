import json
from excel2xmlcode.utils.app.AppConfig import AppConfig
from excel2xmlcode.utils.file.FileUtil import writeFile

class AppData(AppConfig):
    '''
    app 的数据文件，通常是可以修改更新的文件
    dataPath: 配置文件路径
    '''
        
    def saveAppData(self, prop, value, saveNow=True, compress=False):
        '''
        save data
        prop: property
        value: string , number, boolean, object...
        saveNow: save config file immediately
        compress: compress file
        '''
        self.readData();
        self.app_data[prop] = value;
        if True==saveNow:
            writeFile(self.data_path,json.dumps(self.app_data, indent=1), compress=compress)
    
import codecs
from zipfile import zlib


def readFile(file_path,encoding="utf-8",compress=None):
    try:
        if True==compress:
            f = open(file=file_path, mode="rb");
            s = f.read();
            s = zlib.decompress(s);
            s = s.decode(encoding).encode(encoding);
        else:
            f = open(file=file_path, mode="r", encoding=encoding);
            s = f.read();
        f.close();
    except:
        s = None;
    if None!=s:
        if codecs.BOM_UTF8==s[:3]:
            s=s[3:];
    return s;

def writeFile(file_path,content,encoding="utf-8",compress=None):
    #try:
        if True==compress:
            f = open(file=file_path, mode="wb");
            bytes_content = bytes(content.encode(encoding));
            bytes_content = zlib.compress(bytes_content)
            f.write(bytes_content);
        else:
            try:
                f = open(file=file_path, mode="w", encoding=encoding);
            except:
                f = open(file=file_path, mode="x", encoding=encoding);
            content = bytes(content.encode(encoding)).decode(encoding) #tr = vr.decode(encoding='utf-8')##utf-8 string to unicode
            f.write(content);
        f.close();
    #except:
        print("");
        
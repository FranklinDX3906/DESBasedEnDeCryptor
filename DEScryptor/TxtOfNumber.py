# coding:UTF-8

import CryptorOfNumberFile as C

def transform(FilePath,Key,operation):
    #将密钥转换为64位二进制
    Key = ' '.join(['{:04b}'.format(int(c,16)).replace('0b','') for c in Key])
    Key = Key.replace(' ', '')
    
    #求需要加密到的文件的路径以及名字
    WritePath = FilePath[::-1]
    location = -1
    for u in WritePath:
        if u!='.':
            location = location+1
        else:
            break
    WritePath = WritePath[location+2:]
    WritePath = WritePath[::-1]
    if operation == 1:
        WritePath = WritePath+'Encoded.txt'
    else:
        WritePath = WritePath+'Decoded.txt'
    
    #打开文件，按8字节读取
    with open(FilePath,'r') as f:
        Content = f.read(8)
        BContent = ' '.join(['{:08b}'.format(int(c)).replace('0b','') for c in Content])
        BContent = BContent.replace(' ', '')
        while(Content):
            BContent = ' '.join(['{:08b}'.format(int(c)).replace('0b','') for c in Content])
            BContent = BContent.replace(' ', '')
            if operation == 1:#加密
                CryContent = C.Encrypte(BContent,Key)
            else:
                CryContent = C.Decrypte(BContent,Key)
            
            #print(CryContent)
            
            #将结果转换为10进制
            WriteContentFull = []
            i = 0
            while(i+8<=len(CryContent)):
                WriteContent = '0b'+str(CryContent[i:i+8])
                #print(WriteContent)
                WriteContent = [str(int(WriteContent,2))]
                WriteContentFull = WriteContentFull+WriteContent
                i= i+8
            with open(WritePath,'a') as CryFile:
                WriteContentFull = ''.join(str(c) for c in WriteContentFull)
                #print(WriteContentFull)
                CryFile.write(WriteContentFull)
            Content = f.read(8)
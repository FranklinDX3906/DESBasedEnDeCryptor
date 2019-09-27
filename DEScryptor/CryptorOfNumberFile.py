#coding:UTF-8

def Encrypte(content,path):
    content = content+content
    path = path[::-1]
    location = -1
    for u in path:
        if u!='.':
            location = location+1
        else:
            break
    path = path[location+2:]
    path = path[::-1]
    path = path+'Encoded.txt'
    EnFile = open(path,mode = 'w',encoding ='UTF-8')
    EnFile.write(content)
    EnFile.close
    
def Decrypte(content,path):
    content = content[:(int(len(content)/2))]
    path = path[::-1]
    location = -1
    for u in path:
        if u!='.':
            location = location+1
        else:
            break
    path = path[location+2:]
    path = path[::-1]
    path = path+'Dncoded.txt'
    DnFile = open(path,mode = 'w',encoding ='UTF-8')
    DnFile.write(content)
    DnFile.close
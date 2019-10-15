#coding:UTF-8

def Encrypte(Content,Key):#传入64位二进制content，64位二进制密钥
    Message_Orin = Content
    Key_Orin = Key#初始版本内容以及密钥
    
    #将密钥进行PC1变换为56位(PC_1内容是从1开始)
    PC_1 = [57,49,41,33,25,17,9,
            1,58,50,42,34,26,18,
            10,2,59,51,43,35,27,
            19,11,3,60,52,44,36,
            63,55,47,39,31,23,15,
            7,62,54,46,38,30,22,
            14,6,61,53,45,37,29,
            21,13,5,28,20,12,4]
    Key_0_16 = [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
    i = 0
    while(i<56):
        Key_0_16[0].append(Key_Orin[PC_1[i]-1])
        i = i+1
        
    #16次移位
    
    return Content
    
def Decrypte(Content,Key):
    Content = Content
    return Content
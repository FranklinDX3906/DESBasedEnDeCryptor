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
    
    #16次移位，有些时候左移两次
    
    Left_Shfit = {'1':1,'2':1,'3':2,'4':2,'5':2,'6':2,'7':2,'8':2,'9':1,'10':2,'11':2,'12':2,'13':2,'14':2,'15':2,'16':1}
    i = 1
    while(i<17):
        if(Left_Shfit[str(i)] == 1):
            Key_0_16[i] = Key_0_16[i-1][1:28]+Key_0_16[i-1][0:1]+Key_0_16[i-1][29:56]+Key_0_16[i-1][28:29]
            i = i+1
        else:
            Key_0_16[i] = Key_0_16[i-1][2:28]+Key_0_16[i-1][0:2]+Key_0_16[i-1][30:56]+Key_0_16[i-1][28:30]
            i = i+1
    
    
    #对1~16号56位的密钥执行PC2变换为48位，为了将序号对应起来，我们这里将key0也做变换
    PC_2 = [14,17,11,24,1,5,
            3,28,15,6,21,10,
            23,19,12,4,26,8,
            16,7,27,20,13,2,
            41,52,31,37,47,55,
            30,40,51,45,33,48,
            44,49,39,56,34,53,
            46,42,50,36,29,32]
    Key_0_16_Final = [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
    
    i = 0
    j = 0
    while(i<17):
        j = 0
        while(j<48):
            Key_0_16_Final[i].append(Key_0_16[i][PC_2[j]-1])
            j = j+1
        i = i+1

    
    #将数据IP变换
    IP = [58,50,42,34,26,18,10,2,
          60,52,44,36,28,20,12,4,
          62,54,46,38,30,22,14,6,
          64,56,48,40,32,24,16,8,
          57,49,41,33,25,17,9,1,
          59,51,43,35,27,19,11,3,
          61,53,45,37,29,21,13,5,
          63,55,47,39,31,23,15,7]
    Message_IP = []
    i = 0
    while(i<64):
        Message_IP.append(Message_Orin[IP[i]-1])
        i = i+1
        
    #拆出左右各16个
    L_0_16 = [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
    R_0_16 = [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
    R_E_0_16 = [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]#扩列后的R
    L_0_16[0] = Message_IP[0:32]
    R_0_16[0] = Message_IP[32:64]
    E_Table = [ 32,1,2,3,4,5,
                  4,5,6,7,8,9,
                  8,9,10,11,12,13,
                 12,13,14,15,16,17,
                 16,17,18,19,20,21,
                 20,21,22,23,24,25,
                 24,25,26,27,28,29,
                 28,29,30,31,32,1]#用于32位扩大到48位的E盒
    
    S_1 = [14,4,13,1,2,15,11,8,3,10,6,12,5,9,0,7,
      0,15,7,4,14,2,13,1,10,6,12,11,9,5,3,8,
      4,1,14,8,13,6,2,11,15,12,9,7,3,10,5,0,
     15,12,8,2,4,9,1,7,5,11,3,14,10,0,6,13]
    
    S_2 = [  15,1,8,14,6,11,3,4,9,7,2,13,12,0,5,10,
      3,13,4,7,15,2,8,14,12,0,1,10,6,9,11,5,
      0,14,7,11,10,4,13,1,5,8,12,6,9,3,2,15,
     13,8,10,1,3,15,4,2,11,6,7,12,0,5,14,9]
    
    S_3 = [10,0,9,14,6,3,15,5,1,13,12,7,11,4,2,8,
     13,7,0,9,3,4,6,10,2,8,5,14,12,11,15,1,
     13,6,4,9,8,15,3,0,11,1,2,12,5,10,14,7,
      1,10,13,0,6,9,8,7,4,15,14,3,11,5,2,12]
    
    S_4 = [7,13,14,3,0,6,9,10,1,2,8,5,11,12,4,15,
     13,8,11,5,6,15,0,3,4,7,2,12,1,10,14,9,
     10,6,9,0,12,11,7,13,15,1,3,14,5,2,8,4,
      3,15,0,6,10,1,13,8,9,4,5,11,12,7,2,14]
    
    S_5 = [2,12,4,1,7,10,11,6,8,5,3,15,13,0,14,9,
     14,11,2,12,4,7,13,1,5,0,15,10,3,9,8,6,
      4,2,1,11,10,13,7,8,15,9,12,5,6,3,0,14,
     11,8,12,7,1,14,2,13,6,15,0,9,10,4,5,3]
    
    S_6 = [12,1,10,15,9,2,6,8,0,13,3,4,14,7,5,11,
     10,15,4,2,7,12,9,5,6,1,13,14,0,11,3,8,
      9,14,15,5,2,8,12,3,7,0,4,10,1,13,11,6,
      4,3,2,12,9,5,15,10,11,14,1,7,6,0,8,13]
    
    S_7 = [ 4,11,2,14,15,0,8,13,3,12,9,7,5,10,6,1,
     13,0,11,7,4,9,1,10,14,3,5,12,2,15,8,6,
      1,4,11,13,12,3,7,14,10,15,6,8,0,5,9,2,
      6,11,13,8,1,4,10,7,9,5,0,15,14,2,3,12]
    
    S_8 = [13,2,8,4,6,15,11,1,10,9,3,14,5,0,12,7,
      1,15,13,8,10,3,7,4,12,5,6,11,0,14,9,2,
      7,11,4,1,9,12,14,2,0,6,10,13,15,3,5,8,
      2,1,14,7,4,10,8,13,15,12,9,0,3,5,6,11]
    #初始化ER
    i = 0
    while(i<48):
        R_E_0_16[0].append(R_0_16[0][E_Table[i]-1])
        i = i+1
    #开始16次迭代
    i = 1
    while(i<17):
        L_0_16[i] = R_0_16[i-1]
        #求K和ER的异或
        j = 0
        R_Middle = []#求异或的中间变量(出来是48位)
        while(j<48):
            #print(i)
            if(R_E_0_16[i-1][j]==Key_0_16_Final[i][j]):
                R_Middle.append(0)
            else:
                R_Middle.append(1)
            j = j+1
            #print(j)
        #将R_MIDDLE经过一遍S盒
        location = 32*int(R_Middle[0])+8*int(R_Middle[1])+4*int(R_Middle[2])+2*int(R_Middle[3])+int(R_Middle[4])+16*int(R_Middle[5])
        R_0_16[i] = list(''.join('{:04b}'.format(int(S_1[location]))))
        
        location = 32*int(R_Middle[6])+8*int(R_Middle[7])+4*int(R_Middle[8])+2*int(R_Middle[9])+int(R_Middle[10])+16*int(R_Middle[11])
        R_0_16[i] = R_0_16[i]+list(''.join('{:04b}'.format(int(S_2[location]))))
        
        location = 32*int(R_Middle[12])+8*int(R_Middle[13])+4*int(R_Middle[14])+2*int(R_Middle[15])+int(R_Middle[16])+16*int(R_Middle[17])
        R_0_16[i] = R_0_16[i]+list(''.join('{:04b}'.format(int(S_3[location]))))
        
        location = 32*int(R_Middle[18])+8*int(R_Middle[19])+4*int(R_Middle[20])+2*int(R_Middle[21])+int(R_Middle[22])+16*int(R_Middle[23])
        R_0_16[i] = R_0_16[i]+list(''.join('{:04b}'.format(int(S_4[location]))))
        
        location = 32*int(R_Middle[24])+8*int(R_Middle[25])+4*int(R_Middle[26])+2*int(R_Middle[27])+int(R_Middle[28])+16*int(R_Middle[29])
        R_0_16[i] = R_0_16[i]+list(''.join('{:04b}'.format(int(S_5[location]))))
        
        location = 32*int(R_Middle[30])+8*int(R_Middle[31])+4*int(R_Middle[32])+2*int(R_Middle[33])+int(R_Middle[34])+16*int(R_Middle[35])
        R_0_16[i] = R_0_16[i]+list(''.join('{:04b}'.format(int(S_6[location]))))        
        
        location = 32*int(R_Middle[36])+8*int(R_Middle[37])+4*int(R_Middle[38])+2*int(R_Middle[39])+int(R_Middle[40])+16*int(R_Middle[41])
        R_0_16[i] = R_0_16[i]+list(''.join('{:04b}'.format(int(S_7[location]))))
        
        location = 32*int(R_Middle[42])+8*int(R_Middle[43])+4*int(R_Middle[44])+2*int(R_Middle[45])+int(R_Middle[46])+16*int(R_Middle[47])
        R_0_16[i] = R_0_16[i]+list(''.join('{:04b}'.format(int(S_8[location]))))
        

        #P盒
        P = [16,7,20,21,
            29,12,28,17,
            1,15,23,26,
            5,18,31,10,
            2,8,24,14,
            32,27,3,9,
            19,13,30,6,
            22,11,4,25]
        R_Middle_2= []
        j = 0
        while(j<32):
            R_Middle_2.append(R_0_16[i][P[j]-1])
            j = j+1

        #与左系求异或
        j = 0
        while(j<32):
            if(R_Middle_2[j] == L_0_16[i-1][j]):
                R_0_16[i][j] = 0
            else:
                R_0_16[i][j] = 1
            j = j+1

        #求出此次迭代的E
        j = 0
        while(j<48):
            R_E_0_16[i].append(R_0_16[i][E_Table[j]-1])
            j = j+1
        
        i = i+1
    
    Final_Message = R_0_16[16]+L_0_16[16]
    print(len(Final_Message))
    #IP-1变换
    IP_1 = [40,8,48,16,56,24,64,32,
            39,7,47,15,55,23,63,31,
            38,6,46,14,54,22,62,30,
            37,5,45,13,53,21,61,29,
            36,4,44,12,52,20,60,28,
            35,3,43,11,51,19,59,27,
            34,2,42,10,50,18,58,26,
            33,1,41,9,49,17,57,25]
    i = 0
    Final = []
    while(i<64):
        Final.append(Final_Message[IP_1[i]-1])
        i = i+1
    
    Content = "".join([str(c) for c in Final])
    #返回加密后文件    
    return Content
    
    
    
    
#解码部分    
def Decrypte(Content,Key):
    Content = Content
    return Content
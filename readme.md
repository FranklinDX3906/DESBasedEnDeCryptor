# DESBasedEnDeCryptor 基于DES算法的加密器和解密器

## 说明
- 初始为信息安全课程的课程设计
- 目的是制作一个基于DES算法的加密器和解密器
- 环境：Python3.6.4；Pyinstaller3.5；eclipse
- 使用readme同时也记录制作这个加密器之中的思路

## 目标
- 生成GUI以及Windows上的可执行文件，能够将各种类型的文件进行DES加密，生成新的文件，将新的文件执行解密，可以恢复成原来的文件。

## 各版本预期
- version1.1：能加密、解密只含数字的txt文件
- version1.2：增加加密、解密所有TXT文件
- version1.3：增加功能：加密解密png或jpg格式文件
- version1.4：增加功能：加密解密音频文件
- version1.5：增加功能：加密解密视频文件
- version1.6：待定

---------
# 1.1.0版本

## 内容
- 实现了DES加密（正确性有待验证）

## 注明
- 加密只能加密txt文件
- txt文件内只能含有数字
- 数字个数必须是8的整数倍
- 受制于时间关系，解密还未完成
- 生成的加密文件长度可能会大于原文件，因为写入文件是先将二进制转为十进制的，比方说“1”加密为了“1111 1111”那么原来1的地方会变成255
- 打包必须整个文件夹（GuiReaderAndSelector）一起才能使用

## 下一步
- 更新看时间安排
- 希望有人看到这个项目的话可以继续完成

# 1.0.3版本

## 内容
- 完善代码

## 注明
- 该版本没有可执行文件
- 距离1.1版本只剩DES加密内容
- 下一步开始做DES部分

# 1.0.2版本

## 内容
- 向着目标增加了一些代码

## 注明
- 该版本无EXE文件

# 1.0.1版本

## 内容
- 增加了文件类型选择模块以及密钥输入模块

## 思路
为了之后的可扩展性，初步的文件安排是：
- Gui.py负责Gui部分，与用户交互，获得文件路径、密钥，根据文件类型调用不同的函数，将路径与操作类型（+密钥）传递；
- 一个或几个单独的py负责读取文件，按照不同的文件类型进行预处理，处理为多个64位的数组，将数组以及上层传来的密钥传递给下层；
- 一个py文件负责将收到的64位数据使用接收到的密钥进行DES加密或解密，传送回上层；
- 上层再根据传回的数据进一步处理

## 注明
- GUI不自主生成密钥，皆由用户提供
- 增加了GUI密钥模块
- GUI不再负责读取文件内容，只负责提供文件路径

# 0.1.1版本

## 内容
- 生成exe，生成gui
- 能够打开文件资源管理器，选择文件并读取其路径，根据路径读取文件
- 文件只限含有数字，不含有符号以及文字
- 读入文件后可以做选择。选择加密，则原样拷贝，生成两遍的新文件到原文件相同目录；选择DES解密后也原样拷贝，但是是只截取前二分之一的内容，生成文件到相同目录
- 文件进行加密，再解密后应恢复成原来文件

## 思路
- 在一个py内完成读文件、写文件、GUI操作，在另一个文件内使用类定义完成文件内容加密解密

## 注明
- 未实现加密
- 打包必须整个文件夹（GuiReaderAndSelector）一起才能使用
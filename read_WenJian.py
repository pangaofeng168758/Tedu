'''
   读文件：
       读文件即将文件中的内容读取到内存中，常用读文件函数如下：
       read([size])
          功能：来直接读取文件中字符
          参数：如果没有定义size参数（默认值为-1）或者size值为负
          ，文件将被读取直至末尾，给定size最多读取给定数目个字符（字节）。
           返回值：返回读取到的内容

   注意：
        文件过大时候不建议直接读取到文件结尾，读到文件结尾会返回空字符串。
'''
# f = open('file')
#文件读操作
# data = f.read()
# data = f.read(10)
# data = f.read(1024)

#读文件操作:
# while True:
#     data = f.read(2)
#     if not data:
#         break
#     # print(data)
#     print(data,end=" ")


# data = f.readline(10)
# print(data)
# data = f.readline(10)
# print(data)

# data = f.readlines(42)
# print(data)
# # print(data,end="*")
# f.close()

# for line in f:
#     print(line)

'''
   案例2：查找单词
   1、从终端使用input输入一个单词，基于单词本找到该单词，
   将单词和单词解释打印出来。
'''
while True:
    word = input("word:") #要查找的单词
    #默认r打开
    f = open('dict.txt')
    #每次获取一行
    for line in f:
        w = line.split(' ')[0]
        #如果遍历到单词已经大于word就结束查找
        if w>word:
            print("没有找到该单词")
            break
        elif w == word:
            print(line)
            break
    else:
        print("没找到该单词")
    f.close()














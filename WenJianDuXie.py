'''
    文件读写
'''
# f = open('test.txt','r')
# data = f.read()
# print(data)
# f.close()

# f = open('test.txt','r')
# #循环读取
# while True:
#     #读到文件结尾返回空字符串
#     data = f.read(1024) #一次最多读100字节
#     if not data: #读到结尾跳出循环
#         break
#     print(data)
#
# f.close()

f = open('test.txt','r')
data = f.readline(16)
print(data)
# f.close()


data = f.readline(10)
print(data)
# f.close()


data = f.readlines(12)
print(data)
# f.close()


for i in f:
    print(i)  #每次迭代到一行的内容
f.close()
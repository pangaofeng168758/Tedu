'''
    文件细节处理
'''

# f = open("file",'w')
# while True:
#     data = input(">>")
#     if not data:
#         break
#     f.write(data)#encode()写入字节串
#
# f.close()

#设置缓冲去大小
# #1.打开二进制文件 2.5代表缓冲区为5个字节
# f = open("file",'wb',5)
# while True:
#     data = input(">>")
#     if not data:
#         break
#     f.write(data.encode())#encode()写入字节串
#
# f.close()


# #设置行缓冲
# f = open("file",'w',1)
# while True:
#     data = input(">>")
#     if not data:
#         break
#     f.write(data+'\n')
#
# f.close()


#调用flush()主动刷新缓冲
f = open("file", 'w')
while True:
    data = input(">>")
    if not data:
        break
    f.write(data)
    f.flush() #调用flush()主动刷新缓冲

f.close()
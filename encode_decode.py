'''
字节串
字符串
运行结果如下:
   encode()   b'123456'  加密
   decode()   123456     解密
'''
str01 = "123456"
print(str01.encode())     #字符串变为字节串
byte01 = str01.encode()
byte01 = byte01.decode()  #字节串变为字符串
print(byte01)


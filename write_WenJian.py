'''
   文件写操作
'''
# 'w'写操作,特点
#文件存在,清空已有文件,进行写入
#文件不存在,直接进行写入
f = open('file', 'w')
n = f.write("python")
print(n)
f.close()

# 'a'写操作,特点
#文件存在,不清空已有文件,进行写入
#文件不存在,直接进行写入
for i in range(3):
    f = open('file', 'a')
    n = f.write("python")
    i += 1
    print(n)
f.close()

# 'wb'二进制写操作,特点
#文件存在,清空已有文件,进行写入
#文件不存在,直接进行写入
for i in range(3):
    f = open('file', 'wb')
    n = f.write(b"python")
    i += 1
    print(n)
f.close()

# 'ab'二进制写操作,特点
#文件存在,不清空已有文件,进行写入
#文件不存在,直接进行写入
for i in range(10):
    f = open('file', 'ab')
    n = f.write(b"python\n")
    i += 1
    print("写入了%d个字符:"%n)
f.close()



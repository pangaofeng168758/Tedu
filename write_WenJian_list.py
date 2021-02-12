'''
   writelines(str_list)
功能：接受一个字符串列表作为参数，将它们写入文件。
参数：要写入的内容列表
'''
f = open('file', 'w')
list01 = ["hello\n","world\n"]
# f.writelines(list01)

for i in list01:
    f = open('file', 'a')
    f.writelines(list01)
f.close()
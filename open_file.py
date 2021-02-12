'''
打开文件
'''
# f = open('Day01_WenJian_ReadWrite_NetJiChuNeiRong.py','r')
# f = open('Day01_WenJian_ReadWrite_NetJiChuNeiRong.py','w')
# f = open('file','w')
f1 = open('test.txt','w')
f2 = open('test01.txt','w+')



#第三套方案:
# f3 = open('test01.txt','r+')
# f = open('file', 'a')  #追加的形式不会被覆盖

print(f)
f.close()
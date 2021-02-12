# f = open("t1.txt",'w')#'w'覆盖掉原来的内容
#f = open("t1.txt",'a')  #'a'不覆盖掉原来的内容 会追加内容
f = open("t1.txt",'ab')
# n = f.write("235545")
n = f.write(b"56568568568")
print(n)
f.write('哎呀,水岸到\n'.encode())

list01 = [b'21142\n',b'sdffsdf\n']
f.writelines(list01)
f.close()
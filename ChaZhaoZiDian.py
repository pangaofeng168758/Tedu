'''
再次修改----20210213
'''

# f = open("dict.txt",mode='r')
# a = input('请输入一个单词:')
# while 1:
#     data = f.readline().split(" ")[0]
#     if data == a:
#         print(f.readline())
#         break
#     if not data:
#         print('没有这个单词哦')
#         break
#
# f.close()


# f = open('dict.txt', 'r')
# str = input('请输入字符：')
# for line in f.readlines():
#     new_line = line.split(' ')
#     if str in new_line:
#         print(str)
# print('无此单词')
# f.close()


# while True:
#     alex = input("請輸入要查找的單詞:")
#     f = open("dict.txt", "r+")
#     for line in f.readlines():
#         w=line.split(" ")[0]
#         if w>alex:
#             print("查不到這個單詞")
#         if w==alex:
#             print(line)
#             break
#         else:
#             print("查不到這個單詞")
#     f.close()


while True:
    data = input(">>")
    f = open('dict.txt')
    for i in f:
        word = i.split(' ')[0]
        if data > word:
            # continue
            print("没有找到该单词")
            break
        elif data==word:
            print(i)
            break
    else:
        print('没有该单词')
        break
    f.close()

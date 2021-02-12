'''
   文件处理
   运行结果如下:
       文件大小: 24
        获取文件列表: ['buffer.py', 'write_WenJian.py',
                'Day01_WenJian_ReadWrite_NetJiChuNeiRong.py',
                'seek_exercise.py', 'os_Wenjian_hanshu.py',
                'log.txt', 'open_file.py', 'HTTP_XieYi', 'file',
                'Day02:TaoJieZiBianCheng_httpXieYi_strunctMoKuai.py',
                'struct', 'UDP_TaoJieZi_BianCheng', 'write_WenJian_list.py',
                'file.txt', 'TCP_KeHuDuan_FuWuDuan', 'dict.txt',
                'with_YuJu.py',
                 'read_WenJian.py', 'seek.py', 'with_YuJu_exercise.py',
                 'seek01.py']
        获取文件是否存在: True
        获取文件是否存在: True
'''
import os
print('文件大小:', os.path.getsize("file"))
print('获取文件列表:', os.listdir(".."))
print('获取文件是否存在:', os.path.exists("file"))
print('获取文件是否存在:', os.path.isfile("file"))
# os.remove("./file")


'''
   运行结果如下:
       inception-2015-12-05.tgz
'''
url = 'http://download.' \
      'tensorflow.org/models/imagenet/inception-2015-12-05.tgz'
filename = url.split('/')[-1]  #以‘/ ’为分割f符，保留最后一段
print(filename)

'''
   练习
   将一个指定文件夹下,大小不到10K的普通文件删除
'''
import os
dir = "/home/tarena/FTP/"

for file in os.listdir(dir):
    filename = dir + file
    if os.path.getsize(filename) < 1024 * 10 and \
            os.path.isfile(filename):
        os.remove(filename)

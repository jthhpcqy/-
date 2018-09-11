# 统计给定目录内的文件和文件夹
#-*- coding:utf-8 -*-
import os

disk = 'd:/'         # 这里填写要索引的磁盘或者文件夹
file_count = 0       # 用于文件计数


def list_dir(file_or_dir, indent):
    global file_count
    indent += 1             # 用于记录缩进层次
    for filename in os.listdir(file_or_dir):        # 获取指定文件夹中所有内容的名称列表
        if filename == '$RECYCLE.BIN' or filename == 'System Volume Information' or filename == 'study':       # study文件夹是隐藏文件夹，不会被统计,你懂的
            continue
        else:
            file_path = os.path.abspath(os.path.join(file_or_dir,filename))
            if os.path.isdir(file_path):
                name ='  '*indent + filename + '\n'
                f.write(name)
                list_dir(file_path,indent)
            else:
                name1 ='  '*indent + '--' + filename + '\n'
                f.write(name1)
                file_count += 1

with open(disk + '目录.txt', 'w', encoding='utf-8') as f:
    list_dir(disk,0)
    print('\n\n',disk,'里一共有',file_count,'个文件')

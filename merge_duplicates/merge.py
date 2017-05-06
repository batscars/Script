#coding=utf-8
'''
命令行参数
1：origin_path 源图片资源路径
2：org_path 图片筛选工具删选之后的图片所在路径
3. merge_path 合并图片到该文件路径下（脚本会自动创建merge_path路径）

'''

import os
import sys

overwrite_level = 1

if len(sys.argv) not in [4, 5]:
    print("USAGE: " + sys.argv[0] + " origin_path organized_path merge_path [overwrite_level]")
    exit(1)

origin_path = sys.argv[1]
org_path = sys.argv[2]
merge_path = sys.argv[3]

if len(sys.argv) == 5:
    overwrite_level = int(sys.argv[4])


def check_dir(path):
    if not os.path.isdir(path):
        raise Exception("Not a dir: " + path)


def check_file(path):
    if not os.path.isfile(path):
        raise Exception("Not a file: " + path)


def mkdir(path):
    if not os.path.exists(path):
        os.mkdir(path)
    check_dir(path)


def cpdir(src_dir, dst_dir):
    for files in os.listdir(src_dir):
        src_file = os.path.join(src_dir, files)
        dst_file = os.path.join(dst_dir, src_dir[src_dir.rfind('\\') + 1:] + "_" + files)
        check_file(src_file)
        if check_overwrite(dst_file):
            open(dst_file, "wb").write(open(src_file, "rb").read())


def check_overwrite(path):
    if os.path.isdir(path):
        raise Exception("Exist a dir: " + path)
    elif os.path.exists(path):
        if overwrite_level == -1:
            raise Exception("Exists: " + path)
        elif overwrite_level == 0:
            print ("Exists: " + path)
            return False
        elif overwrite_level == 1:
            if input("Overwrite " + path + " ?"):
                return True
            else:
                return False
        else:
            return True
    else:
        return True


mkdir(merge_path)
check_dir(org_path)
count = 0

for folder in os.listdir(org_path):
    if os.path.isdir(os.path.join(org_path, folder)):
        imgs = os.listdir(os.path.join(org_path, folder))
        dst_dir = os.path.join(merge_path, folder)
        mkdir(dst_dir)
        for img in imgs:
        	if ".jpg" in img.lower():
        		origin_folder = img[:img.rfind('.')]
        		src_dir = os.path.join(origin_path, origin_folder)
        		check_dir(src_dir)
        		cpdir(src_dir, dst_dir)
    count += 1

print (str(count) + " folders merged")

#coding=utf-8
'''
功能：
从源图片资源路径的每个图片文件夹中随机选取一张图片（以该文件夹名称命名）保存至样本图片文件夹

命令行参数
1：origin_path 源图片资源路径
2：sample_path 随机生成的样本图片保存路径
'''

import os
import random
import sys

overwrite_level = 1

if len(sys.argv) not in [3, 4]:
    print("USAGE: " + sys.argv[0] + " origin_path sample_path [overwrite_level]")
    exit(1)

origin_path = sys.argv[1]
sample_path = sys.argv[2]

if len(sys.argv) == 4:
    overwrite_level = int(sys.argv[3])


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
        dst_file = os.path.join(dst_dir, src_dir[src_dir.rfind('/') + 1:] + "_" + files)
        check_file(src_file)
        if check_overwrite(dst_file):
            # print src_file, dst_file
            open(dst_file, "wb").write(open(src_file, "rb").read())


def check_overwrite(path):
    if os.path.isdir(path):
        raise Exception("Exist a dir: " + path)
    elif os.path.exists(path):
        if overwrite_level == -1:
            raise Exception("Exists: " + path)
        elif overwrite_level == 0:
            print "Exists: " + path
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


mkdir(sample_path)
check_dir(origin_path)
count = 0

for folder in os.listdir(origin_path):
    if sample_path != os.path.join(origin_path, folder):
        imgs = os.listdir(os.path.join(origin_path, folder))
        random.shuffle(imgs)
        select_img = None
        for img in imgs:
            if ".jpg" in img.lower() or ".jpeg" in img.lower() or ".bmp" in img.lower() or ".png" in img.lower():
                select_img = img
                break
        if select_img is not None:
    	    source_path = os.path.join(origin_path, folder, img)
    	    check_file(source_path)
    	    target_path = os.path.join(sample_path, folder + img[img.rfind('.'):])
    	    if check_overwrite(target_path):
    	        # print source_path, target_path
    	        open(target_path, "wb").write(open(source_path, "rb").read())
    	        count += 1

print str(count) + " images sampled"

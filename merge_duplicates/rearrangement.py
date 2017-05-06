#coding=utf-8
'''
功能：
将源文件夹中所有嵌套的图片文件夹复制到一个指定的目录下，以便于后期的筛选操作进行

命令行参数
1：origin_path 源图片资源路径
2：arranged_path 整理之后的图片路径
'''

import os
import sys

origin_path = sys.argv[1]
arranged_path = sys.argv[2]

if not os.path.exists(arranged_path):
	os.mkdir(arranged_path)

filewriter = open("arranged.txt", "w")

count = 0
for root, dirs, files in os.walk(origin_path):
	if len(files) > 0:
		arranged = os.path.join(arranged_path, str(count))
		os.mkdir(arranged)

		filewriter.write(root)
		filewriter.write("\n")

		for file in files:
			src_file = os.path.join(root, file)
			dst_file = os.path.join(arranged, file)
			open(dst_file, "wb").write(open(src_file, "rb").read())
		count += 1

filewriter.close()

print str(count) + " folders rearranged!"

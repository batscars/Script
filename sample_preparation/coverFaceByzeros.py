import sys
import cv2
import os
import random
import numpy as np


root_path = '/home/zhangbin/NPD/npd/npd_train/data/face_annotation_zhangbin/Images'
bkg_path = sys.argv[1]
if not os.path.exists(bkg_path):
	os.makedirs(bkg_path)
annot = open(sys.argv[2])
bkg_list = open(sys.argv[3],'w')
while 1:
	line = annot.readline()
	if not line:
		break
	image_name = line.strip('\n')
	image_path = os.path.join(root_path, image_name)
	print(image_path)
	org_img = cv2.imread(image_path)
	rows, cols = org_img.shape[:2]
	cnt = annot.readline()
	cnt = cnt.strip('\n')
	for i in range(int(cnt)):
		line = annot.readline()
		line = line.strip('\n')
		temp = line.split(' ')
		x = int(temp[0])
		y = int(temp[1])
		w = int(temp[2])
		h = int(temp[3])
		x_ = x + w
		y_ = y + h
		mat = np.zeros((h,w,3), np.uint8)
		org_img[y:y_, x:x_, :] = mat[0:h, 0:w, :]
	
	image_save_path = os.path.join(bkg_path, image_name)
	print(image_save_path)
	cv2.imwrite(image_save_path, org_img)
	bkg_list.write(image_name + '\n')
annot.close()
bkg_list.close()
		


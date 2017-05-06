import sys
import cv2
import os
import random
import numpy as np

def get_max_gap(face_list=[]):
	max_gap  = face_list[0][2]
	for i in range(len(face_list)):
		if max_gap < face_list[i][2]:
			max_gap = face_list[i][2]
		if max_gap < face_list[i][3]:
			max_gap = face_list[i][3]	
	return max_gap


def get_random_rect(width, height, face_list=[]):
	max_gap = get_max_gap(face_list)
	res = []
	while 1:
		rx = random.randint(0, width - max_gap - 1)
		ry = random.randint(0, height - max_gap - 1)
		flag = 1
		for i in range(len(face_list)):
			x = face_list[i][0]
			y = face_list[i][1]
			w = face_list[i][2]
			h = face_list[i][3]
			if rx >= x and (rx <= x + w) and ry >= y and (ry <= y + h):
				flag = 0
				break
			if rx+w >= x and rx + w <= x + w and ry+h >= y and ry + h <= y + h:
				flag = 0
				break 
		if flag == 1 and len(res) < len(face_list):
			res.append([rx, ry])
		if len(res) == len(face_list):
			break;
	return res
	

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
	print(cnt)
	face_list = []
	for i in range(int(cnt)):
		line = annot.readline()
		line = line.strip('\n')
		temp = line.split(' ')
		x = int(temp[0])
		y = int(temp[1])
		w = int(temp[2])
		h = int(temp[3])
    		face_list.append([x,y,w,h])
	patch = get_random_rect(cols, rows, face_list)
	for i in range(len(patch)):
		rx = patch[i][0]
		ry = patch[i][1]
		x = face_list[i][0]
		y = face_list[i][1]
		w = face_list[i][2]
		h = face_list[i][3]
		rx_ = rx + w
		ry_ = ry + h
		x_ = x + w
		y_ = y + h
		# print('rx='+str(rx)+' ry='+str(ry) + ' rx_=' + str(rx_) + ' ry_=' + str(ry_))
		# print('x='+str(x)+' y='+str(y) + ' x_=' + str(x_) + ' y_=' + str(y_))
		org_img[y:y_, x:x_, :] = org_img[ry:ry_, rx:rx_, :]

	image_save_path = os.path.join(bkg_path, image_name)
	cv2.imwrite(image_save_path, org_img)
	bkg_list.write(image_save_path + '\n')
annot.close()
bkg_list.close()
		


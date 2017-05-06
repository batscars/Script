import sys
import cv2
import os
import random
import numpy as np

root_path = '.......'

def to_square(x, y, w, h):
	if w > h:
		gap = (w - h) / 2
		y -= gap
		face_size = w
	else:
		gap = (h - w) / 2
		x -= gap
		face_size = h
	expand = int(0.1 * face_size)
	box_size = face_size + 2 * expand
	box_x = x - expand
	box_y = y - expand
	return box_x, box_y, box_size, expand, face_size

face_annot = open(sys.argv[1])
left_root_path = sys.argv[2]
if not os.path.exists(left_root_path):
	os.makedirs(left_root_path)
left_list = open(sys.argv[3], 'w')
right_root_path = sys.argv[4]
if not os.path.exists(right_root_path):
	os.makedirs(right_root_path)
right_list = open(sys.argv[5], 'w')

while 1:
	line = face_annot.readline()
	if not line:
		break
	line = line.strip('\n')
	init_name = line.split('.')[0]
	image_path = os.path.join(root_path, line)
	org_img = cv2.imread(image_path)
	reflect = cv2.copyMakeBorder(org_img, 120, 120, 120, 120, cv2.BORDER_REPLICATE)
	cnt = face_annot.readline()
	cnt = cnt.strip('\n')
	face_cnt = 0
	for i in range(int(cnt)):
		line = face_annot.readline()
		line = line.strip('\n')
		temp = line.split(' ')
		x = int(temp[0])
		y = int(temp[1])
		w = int(temp[2])
		h = int(temp[3])
		label = int(temp[4])
		if label != 1 and label !=2:
			continue
		box_x, box_y, box_size, expand, face_size = to_square(x, y, w, h)
		print(box_x, box_y, box_size, expand, face_size)
		box_x += 120
		box_y += 120
		crop_img = reflect[box_y:box_y+box_size, box_x:box_x+box_size]
		if label == 1:
			image_name = init_name + '_face_' + str(face_cnt) + '_' + str(x) + '_' + str(y) + '_' + str(w) + '_' + str(h) + '.jpg'
			left_save_path = os.path.join(left_root_path, image_name)
			print(left_save_path)
			cv2.imwrite(left_save_path, crop_img)
			left_list.write(left_save_path + ' ' + str(expand) + ' ' + str(expand) + ' ' + str(face_size) + ' ' + str(face_size) + '\n')
		elif label == 2:
			image_name = init_name + '_face_' + str(face_cnt) + '_' + str(x) + '_' + str(y) + '_' + str(w) + '_' + str(h) + '.jpg'
			right_save_path = os.path.join(right_root_path, image_name)
			print(right_save_path)
			cv2.imwrite(right_save_path, crop_img)
			right_list.write(right_save_path + ' ' + str(expand) + ' ' + str(expand) + ' ' + str(face_size) + ' ' + str(face_size) + '\n')
			
		face_cnt += 1

face_annot.close()
left_list.close()
right_list.close()

	

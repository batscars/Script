import sys
import cv2
import os
import random
import numpy as np
import argparse


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


def main(face_annot, nor_path, abnor_path, nor_face, abnor_face):
	root_path = "/home/zhangbin/Pos"
	face_annot = open(face_annot)
	if not os.path.exists(nor_path):
		os.makedirs(nor_path)
	if not os.path.exists(abnor_path):
		os.makedirs(abnor_path)
	nor_face = open(nor_face,'w')
	abnor_face = open(abnor_face,'w')
	imageIndex = 0
	while 1:
		line = face_annot.readline()
		imageIndex += 1
		if not line:
			break
		print("processing image " + str(imageIndex))
		line = line.strip('\n')
		init_name = line.split('/')[-1].split('.')[0]
		image_path = os.path.join(root_path, line)
		org_img = cv2.imread(image_path)
		reflect = cv2.copyMakeBorder(org_img, 100, 100, 100, 100, cv2.BORDER_REPLICATE)
		cnt = face_annot.readline()
		cnt = cnt.strip('\n')
		if int(cnt) == 1:
			flag = True
		else:
			flag = False
		for i in range(int(cnt)):
			line = face_annot.readline()
			if flag:
				line = line.strip('\n')
				temp = line.split(' ')
				x = int(temp[0])
				y = int(temp[1])
				w = int(temp[2])
				h = int(temp[3])
				if x < 0:
					w += x
					x = 0
				if y < 0:
					h += y
					y = 0
				box_x, box_y, box_size, expand, face_size = to_square(x, y, w, h)
				print(box_x, box_y, box_size, expand, face_size)
				box_x += 100
				box_y += 100
				crop_img = reflect[box_y:box_y+box_size, box_x:box_x+box_size]
				image_name = init_name + '.png'
				if box_x + expand < 100 or box_y + expand < 100:
					save_path = os.path.join(abnor_path, image_name)
					print(save_path)
					cv2.imwrite(save_path, crop_img)
					abnor_face.write(save_path + ' ' + str(expand) + ' ' + str(expand) + ' ' + str(face_size) + ' ' + str(face_size) + '\n')
				else:
					save_path = os.path.join(nor_path, image_name)
					print(save_path)
					cv2.imwrite(save_path, crop_img)
					nor_face.write(save_path + ' ' + str(expand) + ' ' + str(expand) + ' ' + str(face_size) + ' ' + str(face_size) + '\n')

	face_annot.close()
	nor_face.close()
	abnor_face.close()

def parse_args():
	parser = argparse.ArgumentParser(description='pos annotation converter')
	parser.add_argument('-a', '--annot', dest='annot', type=str, default='./685pos_detected.txt', help='annotation list like fddb list format')
	parser.add_argument('-ap', '--abnor_path', dest='abnor_path', type=str, default='', help='the root path to save abnormal faces')
	parser.add_argument('-al', '--abnor_list', dest='abnor_list', type=str, default='', help='the list to store abnormal face position info')
	parser.add_argument('-np', '--nor_path', dest='nor_path', type=str, default='', help='the root path to save normal faces')
	parser.add_argument('-nl', '--nor_list', dest='nor_list', type=str, default='', help='the list to store normal face position info')
	args = parser.parse_args()
	return args

if __name__ == '__main__':
	args = parse_args()
	main(args.annot, args.nor_path, args.abnor_path, args.nor_list, args.abnor_list)


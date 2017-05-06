import sys
import cv2
import os
import numpy as np

root_path = '/home/zhangbin/NPD/npd/npd_train/data/face_annotation_zhangbin/Images'
annot = open(sys.argv[1])
res = open(sys.argv[2], 'w')

count = 0
while 1:
	line = annot.readline()
	if not line:
		break
	res.write(line)
	image_path = line.strip('\n')
	image_path = os.path.join(root_path, image_path)
	print(image_path)
	org_img = cv2.imread(image_path)
	height, width = org_img.shape[:2]

	cnt = annot.readline()
	res.write(cnt)
	cnt = cnt.strip('\n')
	for i in range(int(cnt)):
		line = annot.readline()
		line = line.strip('\n')
		temp = line.split(' ')
		x = int(temp[0])
		y = int(temp[1])
		w = int(temp[2])
		h = int(temp[3])
    		if x + w > width:
			w = width - x
			count += 1
		if y + h > height:
			h = height - y
			count += 1
		res.write(temp[0] + ' ' + temp[1] + ' ' + str(w) + ' ' + str(h) + ' ' + temp[4] + '\n')
print(str(count))
annot.close()
res.close()

		


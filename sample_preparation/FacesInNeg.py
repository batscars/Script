import sys
import os
import cv2
import random
res = open(sys.argv[1], 'w')
path01 = ''
pixels= []
for i in range(10):
	x = random.randint(0, 32)
	y = random.randint(0, 32)
	pixels.append([x, y])

lut = []
to_cmp = []
for dirs in os.path.listdir(path01):
	if dirs != 'neg_ends' and dirs != 'Faces':
		for images in os.path.join(path01, dirs):
			image_path = os.path.join(path01, dirs, images)
			img = cv2.imread(image_path, 0)
			p = []
			for i in range(10):
				p.append(img[pixels[i][1], pixels[i][0]])
			path = dirs + '/' + images
			lut.append([path, p])
	else if dirs == 'Faces':
		for images in os.path.join(path01, dirs):
			image_path = os.path.join(path01, dirs, images)
			img = cv2.imread(image_path, 0)
			p = []
			for i in range(10):
				p.append(img[pixels[i][1], pixels[i][0]])
			path = dirs + '/' + images
			to_cmp.append([path, p])

for cmps in to_cmp:
	path_cmps = cmps[0]
	p0 = cmps[1][0]
	p1 = cmps[1][1]
	p2 = cmps[1][2]
	p3 = cmps[1][3]
	p4 = cmps[1][4]
	p5 = cmps[1][5]
	p6 = cmps[1][6]
	p7 = cmps[1][7]
	p8 = cmps[1][8]
	p9 = cmps[1][9]
	for item in lut:
		path = item[0]
		p0_ = item[1][0]
		p1_ = item[1][1]
		p2_ = item[1][2]
		p3_ = item[1][3]
		p4_ = item[1][4]
		p5_ = item[1][5]
		p6_ = item[1][6]
		p7_ = item[1][7]
		p8_ = item[1][8]
		p9_ = item[1][9]
		if p0 != p0_:
			continue
		else if p1 != p1_:
			continue
		else if p2 != p2_:
			continue
		else if p3 != p3_:
			continue
		else if p4 != p4_:
			continue
		else if p5 != p5_:
			continue
		else if p6 != p6_:
			continue
		else if p7 != p7_:
			continue
		else if p8 != p8_:
			continue
		else if p9 != p9_:
			continue
		else:
			res.write(path_cmps + ' ' + path+'\n')
res.close()
			



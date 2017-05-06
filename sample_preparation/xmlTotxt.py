import sys, os, random
import xml.etree.ElementTree as ET
reload(sys)
sys.setdefaultencoding('utf8')

anno_path = sys.argv[1]
result = sys.argv[2]
face_cnt = {'face' : 0, 'left' : 0, 'right' : 0}
res_file = open(result, 'w')

for anno_file in os.listdir(anno_path):
	root = ET.parse(os.path.join(anno_path, anno_file)).getroot()
	image_name = root.find('filename').text
	print(image_name)
	res_file.write(image_name + '.jpg' + '\n')
	cnt = 0
	for obj in root.findall('object'):
		cnt += 1
		face_cnt['face'] += 1	
	res_file.write(str(cnt) + '\n')
	for obj in root.findall('object'):	
		name = obj.find('name').text
		if name in ['face_right_profile']:
			label = 2
			face_cnt['right'] += 1
		elif name in ['face_left_profile']:
			label = 1
			face_cnt['left'] += 1
		else:
			label = 0
		bbox = obj.find('bndbox')
		xmin = bbox.find('xmin').text
		ymin = bbox.find('ymin').text
		xmax = bbox.find('xmax').text
		ymax = bbox.find('ymax').text
		width = int(xmax) - int(xmin) + 1
		height = int(ymax) - int(ymin) + 1
		res_file.write(xmin + " " + ymin + " " + str(width) + " " + str(height) + " " + str(label) + "\n")
print("faces:"+str(face_cnt['face']))
print("left profile:"+str(face_cnt['left']))
print("right profile:"+str(face_cnt['right']))
res_file.close()
		


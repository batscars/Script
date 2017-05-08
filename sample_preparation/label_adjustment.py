import sys
import os
import xml.etree.ElementTree as ET
reload(sys)
sys.setdefaultencoding('utf8')


annotation_path = sys.argv[1]
res = open(sys.argv[2])

while 1:
	line = res.readline()
	if not line:
		break
	line = line.strip('\n')
	tmp = line.split(' ')
	annot_file = os.path.join(annotation_path, tmp[0])
	xmin = int(tmp[1])
	ymin = int(tmp[2])
	xmax = int(tmp[3])
	ymax = int(tmp[4])
	label = tmp[5]
	tree = ET.parse(annot_file)
	root = tree.getroot()
	for obj in root.findall('object'):
		bbox = obj.find('bndbox')
		xmin_ = bbox.find('xmin').text
		ymin_ = bbox.find('ymin').text
		xmax_ = bbox.find('xmax').text
		ymax_ = bbox.find('ymax').text
		if xmin_ == xmin and xmax_ == xmax and ymin_ == ymin and ymax_ == ymax:
			obj.find('name').text = label
	
	tree.write(annot_file, encoding='utf-8', xml_declaration=True)

res.close()


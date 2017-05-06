import cv2
import sys
import os

right_file = open(sys.argv[1])
left_root_path = sys.argv[2]
right_flip_file = open(sys.argv[3], 'w')

while 1:
    line = right_file.readline()
    if not line:
        break
    line = line.strip('\n')
    temp = line.split(' ')
    right_path = temp[0]
    right_name = right_path.split('/')[-1]
    org_img = cv2.imread(right_path)
    cv2.res
    rows, cols = org_img.shape[:2]
    flip_img = cv2.flip(org_img, 1)
    x = int(temp[1])
    y = int(temp[2])
    w = int(temp[3])
    h = int(temp[4])
    x = cols - w - x
    save_path = os.path.join(left_root_path, right_name)
    cv2.imwrite(save_path, flip_img)
    right_flip_file.write(save_path + ' ' + str(x) + ' ' + str(y) + ' ' + str(w) + ' ' + str(h) + '\n')

right_file.close()
right_flip_file.close()

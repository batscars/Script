import os
import cv2
import shutil
import numpy as np

root_path = raw_input()
print(root_path)
right_path = os.path.join(os.path.dirname(root_path), 'right')
if not os.path.exists(right_path):
    os.makedirs(right_path)
print(right_path)
img_list = []
rmv_list = []
right_list = []
for image in os.listdir(root_path):
    if ".jpg" in image.lower() or ".jpeg" in image.lower() or ".bmp" in image.lower() or ".png" in image.lower():
        img_path = os.path.join(root_path, image)
        img_list.append([img_path, 0])

index = 0
processing = 0
while 1:
    if index > len(img_list) - 1:
        break
    processing += 1
    print("processing num: " + str(processing))
    current_img_path = img_list[index][0]
    if img_list[index][0] == 1:
        rmv_list.remove(current_img_path)
        img_list[index][0] = 0
    elif img_list[index][0] == 2:
        right_list.remove(current_img_path)
        img_list[index][0] = 0
    img = cv2.imread(current_img_path)
    print('current processing image: '+current_img_path)
    cv2.namedWindow('show')
    cv2.imshow('show', img)
    key = cv2.waitKey()
    # print(key)
    if key == 100:  # keyboard 'd'
        img_list[index][1] = 1
        rmv_list.append(current_img_path)
        index += 1
        continue
    elif key == 114:  # keyboard 'r'
        img_list[index][1] = 2
        right_list.append(current_img_path)
        index += 1
        continue
    elif key == 2555904 or key == 2621440: #  linux key == 65363 or key == 65364:
        index += 1
        continue
    elif key == 2490368 or key == 2424832: #  linux key == 65361 or key == 65362:
        index -= 1
        continue
    elif key == 32:
        break
cv2.destroyAllWindows()
print('rmv_list length: ' + str(len(rmv_list)))
print('right_list length: ' + str(len(right_list)))
for item in rmv_list:
    print(item)
    os.remove(item)

for item in right_list:
    right_name = item.split('\\')[-1]
    right_name = os.path.join(right_path, right_name)
    shutil.move(item, right_name)
raw_input('press any key to exit!!!')

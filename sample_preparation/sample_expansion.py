import sys
import cv2
import os
import random
import numpy as np


def rotation_option(img_path):
    img = cv2.imread(img_path)  
    rows, cols = img.shape[:2]
    angle = random.uniform(-40, 50)
    print(angle)
    dist = (int((2 * rows ** 2) ** 0.5) - rows) / 2
    reflect = cv2.copyMakeBorder(img, dist, dist, dist, dist, cv2.BORDER_REFLECT)
    m = cv2.getRotationMatrix2D(((cols+dist)/2, (rows+dist)/2), angle, 1)
    dst = cv2.warpAffine(reflect, m, (cols+dist, rows+dist))
    res = dst[dist:dist+rows, dist:dist+cols]
    return res


def translation_option(img_path, direction):
    img = cv2.imread(img_path)
    rows, cols = img.shape[:2]
    distance = random.uniform(0.05, 0.1)
    distance = int(distance*rows)
    print(distance)

    # left
    if direction == 0:
        h = np.float32([[1, 0, -distance], [0, 1, 0]])
        reflect = cv2.copyMakeBorder(img, 0, 0, 0, distance, cv2.BORDER_REFLECT)
        r, c = reflect.shape[:2]
        res = cv2.warpAffine(reflect, h, (c, r))
        res = res[0:rows, 0:cols]
    # right
    elif direction == 1:
        h = np.float32([[1, 0, distance], [0, 1, 0]])
        reflect = cv2.copyMakeBorder(img, 0, 0, distance, 0, cv2.BORDER_REFLECT)
        r, c = reflect.shape[:2]
        res = cv2.warpAffine(reflect, h, (c, r))
        res = res[0:rows, distance:distance+cols]
    # up
    elif direction == 2:
        h = np.float32([[1, 0, 0], [0, 1, -distance]])
        reflect = cv2.copyMakeBorder(img, 0, distance, 0, 0, cv2.BORDER_REFLECT)
        r, c = reflect.shape[:2]
        res = cv2.warpAffine(reflect, h, (c, r))
        res = res[0:rows, 0:cols]
    # down
    else:
        h = np.float32([[1, 0, 0], [0, 1, distance]])
        reflect = cv2.copyMakeBorder(img, distance, 0, 0, 0, cv2.BORDER_REFLECT)
        r, c = reflect.shape[:2]
        res = cv2.warpAffine(reflect, h, (c, r))
        res = res[distance:distance+rows, 0:cols]

    return res


def translation(positive_list, res_list, save_path):
    if not os.path.exists(save_path):
        os.makedirs(save_path)
    left = os.path.join(save_path, 'left')
    right = os.path.join(save_path, 'right')
    up = os.path.join(save_path, 'up')
    down = os.path.join(save_path, 'down')
    if not os.path.exists(left):
        os.makedirs(left)
    if not os.path.exists(right):
        os.makedirs(right)
    if not os.path.exists(up):
        os.makedirs(up)
    if not os.path.exists(down):
        os.makedirs(down)

    pos_file = open(positive_list)
    res_file = open(res_list, 'w')

    while 1:
        line = pos_file.readline()
        if not line:
            break
        line = line.strip('\n')
        temp = line.split(' ')
        img_path = temp[0]
        print(img_path)
        img_name = img_path.split('/')[-1]
        left_img = translation_option(img_path, 0)
        right_img = translation_option(img_path, 1)
        up_img = translation_option(img_path, 2)
        down_img = translation_option(img_path, 3)
        left_path = os.path.join(left, img_name)
        right_path = os.path.join(right, img_name)
        up_path = os.path.join(up, img_name)
        down_path = os.path.join(down, img_name)
        cv2.imwrite(left_path, left_img)
        cv2.imwrite(right_path, right_img)
        cv2.imwrite(up_path, up_img)
        cv2.imwrite(down_path, down_img)
        res_file.write(left_path + ' ' + temp[1] + ' ' + temp[2] + ' ' + temp[3] + ' ' + temp[4] + '\n')
        res_file.write(right_path + ' ' + temp[1] + ' ' + temp[2] + ' ' + temp[3] + ' ' + temp[4] + '\n')
        res_file.write(up_path + ' ' + temp[1] + ' ' + temp[2] + ' ' + temp[3] + ' ' + temp[4] + '\n')
        res_file.write(down_path + ' ' + temp[1] + ' ' + temp[2] + ' ' + temp[3] + ' ' + temp[4] + '\n')

    pos_file.close()
    res_file.close()


def rotation(positive_list, res_list, save_path):
    if not os.path.exists(save_path):
        os.makedirs(save_path)
    pos_file = open(positive_list)
    res_file = open(res_list, 'w')
    while 1:
        line = pos_file.readline()
        if not line:
            break
        line = line.strip('\n')
        temp = line.split(' ')
        img_path = temp[0]
        print(img_path)
        img_name = img_path.split('/')[-1]
        rotate_path = os.path.join(save_path, img_name)
        rotate_img = rotation_option(img_path)
        cv2.imwrite(rotate_path, rotate_img)
        res_file.write(rotate_path + ' ' + temp[1] + ' ' + temp[2] + ' ' + temp[3] + ' ' + temp[4] + '\n')
    pos_file.close()
    res_file.close()

translation(sys.argv[1], sys.argv[2], sys.argv[3])

# rotation(sys.argv[1], sys.argv[2], sys.argv[3])

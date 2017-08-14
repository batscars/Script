# -*- coding:utf-8 -*-
import cv2
import random
import sys
import os
import argparse
import numpy as np
import shutil

def flip(folder, img_name, root, org_img):
    if not os.path.exists(os.path.join(root, folder)):
        os.makedirs(os.path.join(root, folder))
    dst = os.path.join(root, folder,img_name+"_f.jpg")
    print(dst)
    flip_img = cv2.flip(org_img, 1)
    cv2.imwrite(dst,flip_img)

def transform(folder, img_name, root, org_img):
    if not os.path.exists(os.path.join(root, folder)):
        os.makedirs(os.path.join(root, folder))
    seed = random.uniform(0.05, 0.1)
    rows, cols = org_img.shape[:2]
    dis00 = seed * cols
    dis01 = seed * rows
    left = np.float32([[1, 0, -dis00],[0, 1, 0]])
    right = np.float32([[1, 0, dis00],[0, 1, 0]])
    up = np.float32([[1, 0, 0],[0, 1, -dis01]])
    down = np.float32([[1, 0, 0],[0, 1, dis01]])
    left_res = cv2.warpAffine(org_img, left, (cols, rows))
    right_res = cv2.warpAffine(org_img, right, (cols, rows))
    up_res = cv2.warpAffine(org_img, up, (cols, rows))
    down_res = cv2.warpAffine(org_img, down, (cols, rows))
    cv2.imwrite(os.path.join(root, folder, img_name+"_l.jpg"), left_res)
    cv2.imwrite(os.path.join(root, folder, img_name+"_r.jpg"), right_res)
    cv2.imwrite(os.path.join(root, folder, img_name+"_u.jpg"), up_res)
    cv2.imwrite(os.path.join(root, folder, img_name+"_d.jpg"), down_res)
    print(os.path.join(root, folder, img_name+"_l.jpg"))
    print(os.path.join(root, folder, img_name+"_r.jpg"))
    print(os.path.join(root, folder, img_name+"_u.jpg"))
    print(os.path.join(root, folder, img_name+"_d.jpg"))

def rotation(folder, img_name, root, org_img):
    if not os.path.exists(os.path.join(root, folder)):
        os.makedirs(os.path.join(root, folder))
    seed00 = random.uniform(0, 30)
    seed01 = random.uniform(0, 30)
    rows, cols = org_img.shape[:2]
    M00 = cv2.getRotationMatrix2D((cols/2, rows/2), seed00, 1)
    M01 = cv2.getRotationMatrix2D((cols/2, rows/2), -seed00, 1)
    M10 = cv2.getRotationMatrix2D((cols/2, rows/2), seed01, 1)
    M11 = cv2.getRotationMatrix2D((cols/2, rows/2), -seed01, 1)
    R00 = cv2.warpAffine(org_img, M00, (cols, rows))
    R01 = cv2.warpAffine(org_img, M01, (cols, rows))
    R10 = cv2.warpAffine(org_img, M10, (cols, rows))
    R11 = cv2.warpAffine(org_img, M11, (cols, rows))
    cv2.imwrite(os.path.join(root, folder, img_name+"_r00.jpg"), R00)
    cv2.imwrite(os.path.join(root, folder, img_name+"_r01.jpg"), R01)
    cv2.imwrite(os.path.join(root, folder, img_name+"_r10.jpg"), R10)
    cv2.imwrite(os.path.join(root, folder, img_name+"_r11.jpg"), R11)
    print(os.path.join(root, folder, img_name+"_r00.jpg"))
    print(os.path.join(root, folder, img_name+"_r01.jpg"))
    print(os.path.join(root, folder, img_name+"_r10.jpg"))
    print(os.path.join(root, folder, img_name+"_r11.jpg"))
    
def parse_args():
    parser = argparse.ArgumentParser(description='augmentation option')
    parser.add_argument('-at','--aug-type', dest='aug_type', type=str, default='flip,transform,rotate',help='which augmentation to do')
    parser.add_argument('-br','--base-root', dest='base', type=str, help='base image root path')
    parser.add_argument('-bl','--base-lst', dest='base_lst', type=str, help='base image labeling list')
    parser.add_argument('-n', '--num', dest='num', type=int, default=float('Inf'), help='num of images to do augmentation')
    parser.add_argument('-dr', '--dst-root', dest='dst_root', type=str, help='augmentation result saving root path')
    #parser.add_argument('-dl','--dst-lst', dest='dst_lst', help='dst image lst',type=str)
    args = parser.parse_args()
    return args   

if __name__ == '__main__':
    args = parse_args()
    if not os.path.exists(args.dst_root):
        os.makedirs(args.dst_root)
    if not os.path.exists(args.base):
        print("error!!! base path not exists")
        exit(0)
    if not os.path.exists(args.base_lst):
        print("error!!! you should provide image list to do augmentations")
        exit(0)
    aug_type = args.aug_type.split(",")
    if len(aug_type) == 0:
        print("error!!! you should provide what augmentation you want to perform")
        exit(0)
    lst = open(args.base_lst)
    count = 1
    while 1:
        line = lst.readline()
        if not line:
            break
        print("start processing image " + str(count))
        if count>args.num:
            break
        count += 1
        img_path = line.strip("\n").split("\t")[-1]
        print(os.path.join(args.base, img_path))
        if not os.path.exists(os.path.join(args.base, img_path)):
            continue
        temp = img_path.split("/")
        folder = temp[0]
        if not os.path.exists(os.path.join(args.dst_root, folder)):
            os.makedirs(os.path.join(args.dst_root, folder))
        img_name = temp[1].split(".")[0]
        org_img = cv2.imread(os.path.join(args.base, img_path))
        for items in aug_type:
            if items == 'flip':
                flip(folder, img_name, args.dst_root, org_img)
            elif items == 'transform':
                transform(folder, img_name, args.dst_root, org_img)
            else:
                rotation(folder, img_name, args.dst_root, org_img)
        shutil.copy(os.path.join(args.base, img_path), os.path.join(args.dst_root, img_path))

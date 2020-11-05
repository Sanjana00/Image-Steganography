#!/usr/bin/env python3

import cv2
import numpy as np
import sys
import random
import os

source = 'img/'
dest = 'encryption/'

def encrypt(img1, img2):
    for x in range(img2.shape[0]):
        for y in range(img2.shape[1]):
            for z in range(img2.shape[2]):
                v1 = format(img1[x][y][z], '08b')
                v2 = format(img2[x][y][z], '08b')

                v3 = v1[:4] + v2[:4]

                img1[x][y][z] = int(v3, 2)

    return img1

arg_count = len(sys.argv)
if arg_count not in [3, 4]:
    print('Error: incorrect number of command line arguments (expected 2, found {})'.format(arg_count - 1))
    sys.exit(0)

if arg_count == 3:
    output = 'output'
else:
    output = sys.argv[3]

if not os.path.isdir(source):
    print('Error: source directory does not exist')
    sys.exit(0)

if not os.path.isdir(dest):
    os.mkdir(dest)

path1 = source + sys.argv[1]
path2 = source + sys.argv[2]

if not os.path.exists(path1) or not os.path.exists(path2):
    print('Error: File does not exist')
    sys.exit(0)

img1 = cv2.imread(source + sys.argv[1], cv2.IMREAD_UNCHANGED)
cv2.resize(img1, (1920, 1080))

img2 = cv2.imread(source + sys.argv[2], cv2.IMREAD_UNCHANGED)
cv2.resize(img2, (1920, 1080))

out = encrypt(img1, img2)
cv2.imwrite(dest + output + '.jpg', out)

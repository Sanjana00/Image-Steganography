#!/usr/bin/env python3

import cv2
import numpy as np
import sys
import random
import os
from math import floor

source = 'img/'
dest = 'encrypt/'

def resize(img1, img2):
    w1, h1, d1 = img1.shape
    w2, h2, d2 = img2.shape

    ratio = min(w1 / w2, h1 / h2, 1)

    return floor(ratio * h2), floor(ratio * w2)

def encrypt(img1, img2):
    for x in range(img2.shape[0]):
        for y in range(img2.shape[1]):
            for z in range(3):
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

img1 = cv2.imread(source + sys.argv[1])

img2 = cv2.imread(source + sys.argv[2])

img2_resized = cv2.resize(img2, resize(img1, img2))

cv2.imwrite(dest + output + '.png', encrypt(img1, img2_resized))

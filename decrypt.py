#!/usr/bin/env python3

import cv2
import numpy as np
import random
import sys
import os

source = 'encryption/'
dest = 'decrypt/'

def decrypt(img):
    width = img.shape[0]
    height = img.shape[1]
    dimensions = (width, height, 3)

    img1 = np.zeros(dimensions, np.uint8)
    img2 = np.zeros(dimensions, np.uint8)

    for x in range(width):
        for y in range(height):
            for z in range(3):
                v0 = format(img[x][y][z], '08b')
                v1 = v0[:4] + ''.join(random.choices('01', k = 4))
                v2 = v0[4:] + ''.join(random.choices('01', k = 4))

                img1[x][y][z] = int(v1, 2)
                img2[x][y][z] = int(v2, 2)
    return img1, img2

arg_count = len(sys.argv)

if arg_count not in [2, 3]:
    print('Incorrect number of command line arguments (expected 1, found {})'.format(arg_count - 1))
    sys.exit(0)

if arg_count == 3:
    output = sys.argv[2]
else:
    output = 'output'

if not os.path.isdir(source):
    print('Error: source directory does not exist')
    sys.exit(0)

if not os.path.isdir(dest):
    os.mkdir(dest)

path = source + sys.argv[1]

if not os.path.exists(path):
    print('Error: File does not exist')
    sys.exit(0)

img = cv2.imread(source + sys.argv[1], cv2.IMREAD_UNCHANGED)

out1, out2 = decrypt(img)
cv2.imwrite(dest + output + '1.png', out1)
cv2.imwrite(dest + output + '2.png', out2)

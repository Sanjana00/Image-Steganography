#!/usr/bin/env python3

import cv2
import numpy as np
import sys
import random

def encrypt(img1, img2):
    pass

arg_count = len(argv)
if arg_count not in [3, 4]:
    print('Error: Incorrect number of command line arguments')
    sys.exit(0)

if arg_count == 3:
    output = 'output.jpg'
else:
    output = sys.argv[3]

img1 = cv2.imread(sys.argv[1], cv2.IMREAD_UNCHANGED)
img2 = cv2.imread(sys.argv[2], cv2.IMREAD_UNCHANGED)

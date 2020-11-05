#!/usr/bin/env python3

import cv2
import numpy as np
import random
import sys

source = 'outputs/'
dest = 'decrypt/'

arg_count = len(sys.argv)

if arg_count not in [2, 3]:
    print('Incorrect number of command line arguments (expected 2)')
    sys.exit(0)

if arg_count == 3:
    output = sys.argv[2]
else:
    output = 'output'

img = cv2.imread(source + sys.argv[1], cv2.IMREAD_UNCHANGED)

out1, out2 = decrypt(img)
cv2.imwrite(dest + output + '1.jpg', out1)
cv2.imwrite(dest + output + '2.jpg', out2)

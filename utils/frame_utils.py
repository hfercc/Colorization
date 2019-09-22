# -*- coding: utf-8 -*-
import numpy as np
from os.path import *
from scipy.ndimage import imread
#gray_sub = imread('/home/chuchienshu/Downloads/dataset/DAVIS_test/boxing/00002.jpg')
def read_gen(file_name):
    ext = splitext(file_name)[-1].lower()
    if ext == '.png' or ext == '.jpeg' or ext == '.ppm' or ext == '.jpg':
        im = imread(file_name)
        return im
    elif ext == '.bin' or ext == '.raw':
        return np.load(file_name)
    return []
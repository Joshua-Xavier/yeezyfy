"""
AUTHOR: Josh Nelsson-Smith
DESCRIPTION:
"""
import sys, os, random, argparse
from PIL import Image
import imghdr
import numpy as np

def getAverageRGB(img):

    im = np.array(img)
    w,h,d = im.shape
    return tuple(np.average(im.reshape(w*h, d) axis=0))

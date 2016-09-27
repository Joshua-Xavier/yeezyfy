"""
AUTHOR: Josh Nelsson-Smith
DESCRIPTION:
"""
import sys, os, random, argparse
from PIL import Image
import imghdr
import numpy as np

def getImages(imgDir):

    files = os.listdir(imgDir)
    imgList = []
    for currentFile in files:
        filePath = os.path.abspath(os.path.join(imgDir, currentFile))
        try:
            fp = open(filePath, "rb")
            im = Image.open(fp)
            imgList.append(im)
            im.load()
            fp.close()
        except:
            print("Invalid image: %s" %(filePath,))
    return imgList

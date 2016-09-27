"""
AUTHOR: Josh Nelsson-Smith
DESCRIPTION:
"""
import sys, os, random, argparse
from PIL import Image
import imghdr
import numpy as np

def createGrid(images, dims):

    m, n = dims

    assert m*n == len(images)

    width = max([img.size[0] for img in images])
    height = max([img.size[1] for img in images])

    grid_img = Image.new('RGB', (n*width, m*height))

    for index in range(len(images)):
        row = int(index/n)
        col = index - n*row
        grid_img.paste(images[index], (col*width, row*height))

    return grid_img

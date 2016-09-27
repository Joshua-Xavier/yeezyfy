"""
AUTHOR: Josh Nelsson-Smith
DESCRIPTION:
"""
import sys, os, random, argparse
from PIL import Image
import imghdr
import numpy as np

def createMosaic(target_image, input_images, grid_size, reuse_images=True):

    print("Splitting up input image...")
    target_images = gridSplit(target_image, grid_size)

    print("finding image matches...")
    output_images = []
    count = 0
    batch_size = int(len(target_images)/10)

    avgs = []
    for img in input_images:
        avgs.append(getAverageRGB(img))

    for img in target_images:
        avg = getAverageRGB(img)
        match_index = colourMatch(avg, avgs)
        output_images.append(input_images[match_index])
        if count > 0 and batch_size > 10 and count % batch_size is 0:
            print("Processed %d of %d..."(count, len(target_images)))
        count += 1
        if not reuse_images:
            input_images.remove(match_index)

    print("Creating mosaic...")
    mosaic_image = createGrid(output_images, grid_size)

    return mosaic_image

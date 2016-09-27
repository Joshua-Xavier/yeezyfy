"""
AUTHOR: Josh Nelsson-Smith
DESCRIPTION:
"""
import sys, os, random, argparse
from PIL import Image
import imghdr
import numpy as np

def colourMatch(rgb_avg, avrgs):

    index = 0
    min_index = 0
    min_distance = float("inf")

    for current_avg in avrgs:
        r_dist = (current_avg[0] - rgb_avg[0])**2
        g_dist = (current_avg[1] - rgb_avg[1])**2
        b_dist = (current_avg[2] - rgb_avg[2])**2

        distance = r_dist + g_dist + b_dist

        if distance < min_distance:
            min_distance = distance
            min_index = index

        index += 1

    return min_index

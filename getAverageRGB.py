"""
AUTHOR: Josh Nelsson-Smith
DESCRIPTION:
"""

def getAverageRGB(img):

    im = np.array(img)
    w,h,d = im.shape
    return tuple(np.average(im.reshape(w*h, d) axis=0))

import sys, os, random, argparse
from PIL import Image
import imghdr
import numpy as np
from lib.createMosaic import *



def main():
  # Command line args are in sys.argv[1], sys.argv[2] ..
  # sys.argv[0] is the script name itself and can be ignored

  # parse arguments
  parser = argparse.ArgumentParser(description='Creates a photomosaic from input images')
  # add arguments
  parser.add_argument('--target-image', dest='target_image', required=True)
  parser.add_argument('--input-folder', dest='input_folder', required=True)
  parser.add_argument('--grid-size', nargs=2, dest='grid_size', required=True)
  parser.add_argument('--output-file', dest='outfile', required=False)

  args = parser.parse_args()

  ###### INPUTS ######

  # target image
  target_image = Image.open(args.target_image)

  # input images
  print('reading input folder...')
  input_images = getImages(args.input_folder)

  # check if any valid input images found
  if input_images == []:
      print('No input images found in %s. Exiting.' % (args.input_folder, ))
      exit()

  # shuffle list - to get a more varied output?
  random.shuffle(input_images)

  # size of grid
  grid_size = (int(args.grid_size[0]), int(args.grid_size[1]))

  # output
  output_filename = 'mosaic.png'
  if args.outfile:
    output_filename = args.outfile

  # re-use any image in input
  reuse_images = True

  # resize the input to fit original image size?
  resize_input = True

  ##### END INPUTS #####

  print('starting photomosaic creation...')

  # if images can't be reused, ensure m*n <= num_of_images
  if not reuse_images:
    if grid_size[0]*grid_size[1] > len(input_images):
      print('grid size less than number of images')
      exit()

  # resizing input
  if resize_input:
    print('resizing images...')
    # for given grid size, compute max dims w,h of tiles
    dims = (int(target_image.size[0]/grid_size[1]),
            int(target_image.size[1]/grid_size[0]))
    print("max tile dims: %s" % (dims,))
    # resize
    for img in input_images:
      img.thumbnail(dims)

  # create photomosaic
  mosaic_image = createMosaic(target_image, input_images, grid_size, reuse_images)

  # write out mosaic
  mosaic_image.save(output_filename, 'PNG')

  print("saved output to %s" % (output_filename,))
  print('done.')

# Standard boilerplate to call the main() function to begin
# the program.
if __name__ == '__main__':
    main()

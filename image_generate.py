# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# import the necessary packages
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.preprocessing.image import load_img
import numpy as np
import argparse
import os, sys

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True,
	help="path to the input image")
ap.add_argument("-o", "--output", required=True,
	help="path to output directory to store augmentation examples")
ap.add_argument("-t", "--total", type=int, default=300,
	help="# of training samples to generate")
args = vars(ap.parse_args())

# load the input image, convert it to a NumPy array, and then
# reshape it to have an extra dimension
print("[INFO] loading example image...")

aug = ImageDataGenerator(
	rotation_range=30,
	zoom_range=0.15,
	width_shift_range=0.2,
	height_shift_range=0.2,
	shear_range=0.15,
	horizontal_flip=True,
	fill_mode="nearest")

for i,img in enumerate(os.listdir(args["image"])):
	total = 0
	print("generating images, round: " + str(i))
	path = args["image"] + img
	image = load_img(path)
	image = image.resize((64,64))
	image = img_to_array(image)
	image = np.expand_dims(image, axis=0)
	# construct the image generator for data augmentation then
	# initialize the total number of images generated thus far
	save_prefix = "image_" + str(i)
	# construct the actual Python generator
	imageGen = aug.flow(image, batch_size=1, save_to_dir=args["output"],
		save_prefix=save_prefix, save_format="jpg")
	
	# loop over examples from our image data augmentation generator
	for image in imageGen:
		# increment our counter
		total += 1
		# if we have reached the specified number of examples, break
		# from the loop
		if total == args["total"]:
			break


# Run this in your anaconda terminal

# first create 4 folders named mh, wl, sc, jh
# command -> python image_generate.py --image data/train/mh/ --output mh
# Run above line 4 times for each mh, wl, sc, jh
# Then CUT paste the folders with generated images into data/train_gen

# do it again to create validation data 
# then again create 4 folders named mh, wl, sc, jh
# command -> python image_generate.py --image data/validation/mh/ --output mh
# Run above line 4 times for each mh, wl, sc, jh
# Then CUT paste the folders with generated images into data/validation_gen

# finally your folder structure will look like:
# main_folder (has image_generate.py)
# - data 
#   - train
#     - mh
#     - ..
#   - validation
#     - mh
#     - ..
#   - test
#     - test_images
#   - train_gen
#     - mh
#     - ..
#   - validation_gen
#     - mh
#     - ..

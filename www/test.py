import numpy as np
import re
import sys
import time
import os.path
import urllib.request
from PIL import Image
ASCII_CHARS = [' ','#','?','%','.','+','.','*',':',',','@']

def scale_image(image,new_width = 60):
    original_width,original_height = image.size
    aspect_ratio = original_height/float(original_width)*0.5

    new_height = int(aspect_ratio*new_width)
    new_image = image.resize((new_width,new_height))
    return new_image

def convert_to_grayscale(image):
    return image.convert('L')

#map image to ascii
def map_pixels_to_ascii_chars(image,range_width=25):
    pixels_in_image = list(image.getdata())
    pixels_to_chars = [ASCII_CHARS[int(pixel_value/range_width)] for pixel_value in pixels_in_image]
    return "".join(pixels_to_chars)

#整合输出
def convert_image_to_ascii(image,new_width=60):
    image = scale_image(image,new_width)
    image = convert_to_grayscale(image)
    pixels_to_chars = map_pixels_to_ascii_chars(image)
    len_chars = len(pixels_to_chars)
    image_ascii = [pixels_to_chars[index: index+new_width] for index in range(0,len_chars,new_width)]
    return "\n".join(image_ascii)

def handle_image_conversion(image_filepath,new_width=60):
    image = Image.open(image_filepath)
    image_ascii = convert_image_to_ascii(image,new_width)
    print(image_ascii)


image_filepath = '1.ico'
handle_image_conversion(image_filepath)
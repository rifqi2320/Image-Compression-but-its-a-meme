import numpy as np
import imageio
import scipy
from PIL import Image

def compress(original,compressed,rate):
    image = Image.open(original)
    
    try:
        rows = image.shape[0]
        cols = image.shape[1]
    except AttributeError:
        rows = image.size[0]
        cols = image.size[1]

    pixels = image.load()

    for i in range(rows):
        for j in range(cols): 
            pixels[i, j] = (rate, pixels[i,j][1], pixels[i,j][2])

    imageio.imwrite(compressed, image)
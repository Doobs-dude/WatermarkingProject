import tkinter as tk
import numpy as np
import hashlib 
import hmac
import block
import watermark
import hash

from PIL import Image

img = Image.open("C:\\Coursework\\puppyimg.jpeg") #test image used until GUI prototype

pixeldata = np.array(img)
block_size = 5
block = block.Block()
blocks = block.create_blocks(pixeldata, block_size) # code until this point is the same as the encryption process
distortion_array = 0

for i in blocks:
    i.positionfind(hasher, watermarkkey)
    i.calculate_meanpixel()
    distortion_array += i.distortion_getter() # the distortions found are added to the distortion_array


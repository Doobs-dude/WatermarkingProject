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
instance = block.Block()
blocks = instance.create_blocks(pixeldata, block_size)
watermark = watermark.Watermark('Turing', 'Alanturing@gmail.com', 'WQ!FJEEI','Scientist')

distortions = watermark.distortion_generator()

distortion_index = 0
for i in blocks:
    i.positionfind(hasher, watermarkkey)
    i.calculate_meanpixel()
    i.distortionpixel_setter(distortions[distortion_index])
    distortion_index += 1
    if distortion_index >= len(distortions):
        distortion_index = 0

block_index = 0
for i in range(0,pixeldata.shape[0],block_size):
    for j in range(0, pixeldata.shape[0],block_size):
        currentblock = blocks[block_index]
        pixeldata[i:i+block_size,j:j+block_size] = currentblock.blockdata
        block_index += 1

watermarked_image = Image.fromarray(pixeldata)
#the blocks have been placed into an empty image


def save_image(image): # the function which helps the user save through the image file
    file_path = filedialog.asksaveasfilename( #gile dialog to guide the user through the process
        defaultextension=".png",
        filetypes=["PNG files", "*.png"])
    
    if file_path: #checks if the user asked to save th image 
        image.save(file_path)
        print(f"Image saved at: {file_path}")

watermarked_image = Image.open("watermarked_image.png")  
save_image(watermarked_image)
    
import numpy as np
import tkinter as tk
from PIL import Image
import hash 
class Block:

    def __init__(self,block_data=None):
        self.blocksize = None
        self.blockdata = block_data # the block data should be added in the create blocks method
        self.mean_pixel = None
        self.position_x = None
        self.position_y = None
    
    def create_blocks(self, pixel_data, block_size):
        self.blocksize = block_size # initialize block size here so that it can be a parameter in create blocks
        blocks = []
        for i in range (0,pixel_data.shape[0], block_size): # iteriates through the whole pixel data, jumping by block size
            for j in range (0, pixel_data.shape[1], block_size):
                block_data = pixel_data[i:i+block_size, j:j+block_size]
                if block_data.shape[0] == block_size and block_data.shape[1] == block_size: # any imcomplete blocks formed are not appended

                    blocks.append(Block(block_data))
        return blocks

    def position_find(self, hasher,key): # algorithm is used because the algorithm must be used for decryption as well
        max_x = self.blocksize #boundaries for where the mean pixel is placed
        max_y = self.blocksize
        print(max_x, max_y)
        self.position_x, self.position_y = hasher(self.blockdata[0,0], max_x, max_y, key)          

    def calculate_meanpixel(self):
        mean_values = []
        for i in range(self.blocksize):
            for j in range(self.blocksize):
                if i != self.position_x and j != self.position_y: # average is calculated except target pixel 
                    mean_values.append(self.blockdata[i,j])
        self.mean_pixel = np.mean(mean_values)

    def distortionpixel_setter(self, distortion_value):
        distorted_pixel = self.mean_pixel
        distorted_pixel += distortion_value
        self.blockdata[self.position_x,self.position_y] = distorted_pixel

    def distortion_getter(self):
        distorted_pixel = self.blockdata[self.position_x,self.position_y]
        distortion_value = distorted_pixel - self.mean_pixel
        return distortion_value




img = Image.open("GUI_test/form_submit.png") #test image used until GUI prototype

pixeldata = np.array(img) #convert the image into an np array

block_size = 5 #set a standard block size
instance = Block() # create an instance of the block class
blocks = instance.create_blocks(pixeldata, block_size) #enumerate the blocks

print(f"Total number of blocks created: {len(blocks)}") #debugging statement which outputs the number of blocks made 


firstblock = blocks[0] #first block taken as a test, just to output the location calculated
key = "test key" #random salt so that hashing in manageable


firstblock.blockdata[firstblock.position_x, firstblock.position_y] = 45.8125

print("the pixel value of the pixel at the position x and y is", firstblock.blockdata[firstblock.position_x, firstblock.position_y])

print("[2.1, 3.8, 1.2, 4.5, 0.7, 2.1, 3.8, 1.2, 4.5, 0.7, 2.1, 3.8, 1.2, 4.5, 0.7]")

def createblocks(pixel_data,block_size):
    blocks=[]
    for i in range(0,pixel_data.shape[0],block_size):
        for j in range(0,pixel_data.shape[1],block_size):
            block_data = pixel_data[i:i+block_size,j+block_size]
            blocks = blocks.append(block(block_data))
            if block_data[0] == block_size and block_data[1] == block_size: 
            
def apply_mean(self,algorithm):
    first_rgbvalue = self.block_data[0,0]
    position = algorithm(first_rgbvalue)

class watermark:
    def __init__():
        self.user_data = user_data
        self.distortions = distortions


    def watermark_generator(self,name,email,copyright,publisher):
        self.user_data = name + email + copyright + publisher
        self.distortions = [(ord(char) % 256)/51 for char in self.user_data]
    
class block: 

    def __init__(self, block_size, block_data): 

        self.block_size = # A constant decided later on in the development process 
        self.block_data = block_data 
        self.mean_pixel = None
        self.location = None
    
    def position_find(self, algorithm):
        self.location = algorithm(self.block_data[0,0])

    def pixel_modify(self, mean_pixel, distortion_value):
        distorted_pixel = mean_pixel.copy()
        distorted_pixel += distortion_value
        return distorted_pixel
    
    def modifpixel_setter(self, location, distorted_pixel):
        self.block_data[self.location] = distorted_pixel
    
    def calculate_mean_pixel(self):
        mask = np.ones(self.block_data.shape[:2], dtype=bool)
        if self.output_position:
            mask[self.output_position] = False
        mean_pixel = self.block_data[mask].reshape(-1, self.block_data.shape[2]).mean(axis=0)
        self.mean_pixel = mean_pixel
    
    def distort_measure(self):
        distortion_value = self.block_data[self.location] - self.mean_pixel

for i in enumerate(blocks):
    distortion_value = watermark.distortion[i]
    distorted_pixel = block.pixel_modify(block.self.mean_pixel, distortion_value)
    block.modifpixel_setter(block.self.location, distorted_pixel)
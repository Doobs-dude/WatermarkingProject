## Overview

 The program I have proposed for my coursework is an encryption algorithm which encodes a message into an image without obvious visible changes to the original image's resolution, sharpness, and clarity. This message will be a watermark, with the purpose of copyright protection by the easy traceability of an image's details back to its owners through the embedding of metadata such as date of publishing, the owners' details; the name/company it was published under and perhaps copyright licensing details.



## Built on


The algorithm design process is made of mostly modular functions and object-oriented programming.

To access the image data in the user's digital media I will be using the python extension Pillow, which allows for the direct manipulation of pixels in an image, including brightness, contrast, color and color space conversions.


For the GUI, the application will be using Tkinter, since using Tkinter can allow for text boxes, buttons, labels, input boxes and even validation, which fits into the criteria for my screen designs and form system.


I will also be using the library hashlib and hmac to provide a key based hashing algorithm to encrypt the location of the mean pixel



## How to run
1. Clone the repo
2. Install dependencies: `pip install pillow`
3. Run: `python main_final.py`

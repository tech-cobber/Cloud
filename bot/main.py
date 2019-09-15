import requests
from PIL import Image, ImageDraw 
import numpy as np

im = Image.open("/Users/aldev/Cloud/images/Example.jpg")
print(im.size[0],im.size[1],im.mode)
raw = np.squeeze(np.asarray(im, np.uint8))
print(raw.shape)


image = {
    "name":"test", 
    "buf": [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    "width": 3, 
    "heigth": 3, 
    "color":"RGB"
    }

requests.post("http://127.0.0.1:8088/test", json=image)

import requests
from PIL import Image, ImageDraw 
import numpy as np
from utils import read_config

config = read_config(f'../config.yml')
token  = config['token']


im = Image.open("/Users/aldev/Cloud/images/Example.jpg")
print(im.size[0],im.size[1],im.mode)
raw = np.squeeze(np.asarray(im, np.uint8))
print(raw.shape)

image = {
    "name":"test", 
    "buf": list(range(4**4)), 
    "width": 4, 
    "heigth": 4, 
    "color":"RGB"
    }

requests.post("http://127.0.0.1:8088/test", json=image) 
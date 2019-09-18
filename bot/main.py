import requests
from PIL import Image, ImageDraw 
import numpy as np
from utils import read_config
import asyncio
from aiogram import Bot, Dispatcher, executor, types

config = read_config(f'../config.yml')
token  = config['token']
bot = Bot(token=token)
dp = Dispatcher(bot)

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


@dp.message_handler(commands='test') 
async def one_time_key(message: types.Message):
    requests.post("http://127.0.0.1:8088/test", json=image) 
    await message.reply("OK")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
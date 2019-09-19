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

@dp.message_handler(content_types=['photo']) 
async def test(message: types.Message):
    img = await bot.download_file_by_id(message.photo[0]['file_id'])
    photo_bytes = img.getvalue() # TODO u8 array from string of bytes
    image = {
        "name":"test", 
        "buf": photo_bytes, 
        "width": 240, 
        "heigth": 320, 
        "color":"RGB"
    }
    #requests.post("http://127.0.0.1:8088/test", json=image) 
    await message.reply_photo(message.photo[0]['file_id'])

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
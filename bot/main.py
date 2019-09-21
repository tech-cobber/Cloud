import requests
from PIL import Image, ImageDraw 
import numpy as np
from utils import read_config
import asyncio
from aiogram import Bot, Dispatcher, executor, types
from io import BytesIO

config = read_config(f'../config.yml')
token  = config['token']
bot = Bot(token=token)
dp = Dispatcher(bot)

@dp.message_handler(content_types=['photo']) 
async def test(message: types.Message):
    print(message.photo[len(message.photo)-1])
    file = await bot.get_file(message.photo[len(message.photo)-1]['file_id'])
    url = f"https://api.telegram.org/file/bot{token}/{file.file_path}"
    response = requests.get(url)
    image = Image.open(BytesIO(response.content))
    print(image.getcolors()) # None :C
    print(image.getbands())
    print(len(image.getdata())) # data - array of (int,int,int) TODO 
    image_json = {
        "name":"test", 
        #"buf": uint_array, 
        "width": message.photo[len(message.photo)-1]['width'], 
        "heigth": message.photo[len(message.photo)-1]['heigth'], 
        "color":"RGB"
    }
    #r = requests.post("http://127.0.0.1:8088/test", json=image_json) 
    #print(r.status_code)
    await message.reply_photo(message.photo[len(message.photo)-1]['file_id'])


async def shutdown(dispatcher: Dispatcher):
    await dispatcher.storage.close()
    await dispatcher.storage.wait_closed()

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_shutdown=shutdown)
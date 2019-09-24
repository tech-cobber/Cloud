from utils import read_config
from aiogram import Bot, Dispatcher, executor, types
from io import BytesIO
import requests
import asyncio

config = read_config(f'../config.yml')
token  = config['token']
bot    = Bot(token=token)
dp     = Dispatcher(bot)

@dp.message_handler(content_types=['photo']) 
async def test(message: types.Message):
    file = await bot.get_file(message.photo[len(message.photo)-1]['file_id'])
    r = requests.post("http://127.0.0.1:8088/image", json={'name': 'image', 
                                                           'path': f'{file.file_path}'
                                                           }) 
    await message.reply(r.status_code)

async def shutdown(dispatcher: Dispatcher):
    await dispatcher.storage.close()
    await dispatcher.storage.wait_closed()

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_shutdown=shutdown)
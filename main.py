import logging
from test import user_data as user
from test import all_user_name, get_user_avarage_a
from aiogram import Bot, Dispatcher, executor, types

logging.basicConfig(level=logging.INFO)
TOKEN = ''
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)
@dp.message_handler(commands=["start"])
async def starts(message):
    await bot.send_message(message.chat.id, "Salom,")
    s = []
    for i in all_user_name():
        s.append(i[0]+'\n')
    await bot.send_message(message.chat.id, f"O'quvchining to'liq ism familiyasini kriting, royhat:\n{''.join(s)}")


@dp.message_handler()
async def user_name(message: types.Message):
    if user(message.text):
        for i in user(message.text):
            await bot.send_message(message.chat.id, i )
        await bot.send_photo(message.chat.id, f"https://chart.googleapis.com/chart?cht=p3&chd=t:{int(get_user_avarage_a(message.text))},{int(100-get_user_avarage_a(message.text))}&chs=450x200&chl=А{int(get_user_avarage_a(message.text))}%|Р{100-int(get_user_avarage_a(message.text))}%")
    else:await bot.send_message(message.chat.id, "Bu ism bo'yicha malumot to'pilmadi" )

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
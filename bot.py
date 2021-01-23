from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

import logging

from config import TOKEN
import keyboards as kb


video_id = "BAACAgIAAxkBAANxYAmaNt18DjU00h1t5_c1jbRhLpwAAj4LAAKyFkhIKIDkPsVJQjceBA"

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)
logging.basicConfig(level=logging.INFO)


@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await bot.send_message(message.chat.id, "Записуйте кожну розмову з Вашими клієнтами, контролюйте роботу операторів та аналізуйте всю отриману інформацію з метою підвищення якості обслуговування!\n Функція розподілу прав доступу допоможе забезпечити високу безпеку даних.\n")
    await bot.send_video(message.chat.id, video_id)

    await bot.send_message(message.chat.id, text="Дізнайтесь більше про функціонал або натиснить /help", reply_markup=kb.kb_functional)
    

@dp.callback_query_handler(lambda c: c.data == 'functional')
async def process_callback_functional(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, 'Оберіть функціонал або натиснить /help', reply_markup=kb.kb_all_abilities)


@dp.callback_query_handler(lambda c: c.data == 'video')
async def process_callback_functional(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_video(callback_query.from_user.id, video_id)


@dp.callback_query_handler(lambda c: c.data == 'contact')
async def process_callback_functional(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_contact(callback_query.from_user.id, phone_number="+380 (44) 33 99 222", first_name='SMIDDLE support')
    await bot.send_message(callback_query.from_user.id, 'м. Київ, пр-т Степана Бандери 16-б, 4 поверх\nmailto:sales@smiddle.com')


@dp.callback_query_handler(lambda c: c.data == 'demo')
async def process_callback_functional(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id, text="Даний функціонал зараз в розробці. Замовте демо на нашому сайті або зв'яжіться з нами!", show_alert=True)


@dp.callback_query_handler(lambda c: c.data and c.data.startswith('func_'))
async def process_callback_kb1btn1(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    
    code = callback_query.data[5:]
    code_answer = ''
    
    if code == 'API':
        code_answer = "API\nМожливість інтеграції з іншими системами за допомогою API."
    if code == 'screen':
        code_answer = "Запис єкрану оператора\nДозволяє відстежувати та записувати всі дії оператора в процесі обслуговування клієнта від початку до кінця розмови."
    if code == 'safety':
        code_answer = "Безпека\nСистема надає можливість гнучкого налаштування прав доступу до записів для захисту та безпеки інформації."
    if code == 'multilingualism':
        code_answer = "Багатомовний веб-інтерфейс\nСистема може бути налаштована таким чином, що інформація веб-інтерфейсу буде відображатися будь-якою мовою, необхідною користувачу (опціонально)."
    if code == 'keep':
        code_answer = "Зберігання записів\nУсі записи копіюються в спеціальне сховище та стискаються до формату mp3."
    if code == 'listen':
        code_answer = "Прискорене прослуховування записів\nМожливість прискореного прослуховування записів дозволяє економити час на оцінювання дзвінків. Таким чином, Ваші супервізори зможуть прослухати більшу кількість записаних дзвінків за той самий проміжок часу."
    if code == 'search':
        code_answer = "Пошук за параметрами\nПошук за певними опціями, фільтрація, прослуховування – ось неповний перелік доступних функцій для роботи з записами. Зручність роботи з системою робить взаємодію з нею легкою та ефективною."
    if code == 'speech':
        code_answer = "Розпізнавання мовлення\nАвтоматизація за допомогою розпізнавання мовлення та пошук по розпізнаних словах дозволяють витрачати менше сил на ручну роботу й більше на аналіз. Унікальна україно-російська мовна модель дозволяє розпізнати і перекласти в текст промову, в якій використовується одночасно дві мови."

    await bot.send_message(callback_query.from_user.id, code_answer)


@dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    await bot.send_message(message.chat.id, "Більше інформації про SMIDDLE RECORDING на нашому сайті або зв'яжіться з нами", reply_markup=kb.kb_help)


@dp.message_handler()
async def echo_message(message: types.Message):
    await bot.send_message(message.chat.id, "Записуйте кожну розмову з Вашими клієнтами, контролюйте роботу операторів та аналізуйте всю отриману інформацію з метою підвищення якості обслуговування!\n Функція розподілу прав доступу допоможе забезпечити високу безпеку даних.")
    await bot.send_message(message.from_user.id, 'Більше інформації /help')


# @dp.message_handler(content_types=["document", "video", "audio"])
# async def handle_files(message):
#     print(message.video.file_id)
#     await bot.send_message(message.chat.id, "С новым годом!⛄")


if __name__ == '__main__':
    executor.start_polling(dp)

import logging

from aiogram import Bot, Dispatcher, executor, types

from buttons import start_keyboards, translations, contact_keyboard
from config import TOKEN
from func import translate

API_TOKEN = TOKEN

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

language = ''


@dp.message_handler(commands=['start'])
async def echo(message: types.Message):
    await bot.send_message(message.chat.id, f'Assalom aleykum, hurmatli {message.from_user.full_name}\n'
                                            f'Tarjimon botimizga xush kelibsiz!\n', reply_markup=start_keyboards)


@dp.callback_query_handler(text='uz_en')
async def inline_button_callback(query: types.CallbackQuery):
    global language
    language = 'uz_en'
    await bot.send_message(query.from_user.id, 'Siz "uz ➡️ en" tilini tanladingiz\nKerakli matnni kiriting')


@dp.callback_query_handler(text='en_uz')
async def inline_button_callback(query: types.CallbackQuery):
    global language
    language = 'en_uz'
    await bot.send_message(query.from_user.id, 'You chose "en ➡️ uz" language\nEnter the text you want to translate')


@dp.callback_query_handler(text='ru_uz')
async def inline_button_callback(query: types.CallbackQuery):
    global language
    language = 'ru_uz'
    await bot.send_message(query.from_user.id, 'Вы выбрали язык "ru ➡️ uz"\nВведите текст, который хотите перевести')


@dp.callback_query_handler(text='uz_ru')
async def inline_button_callback(query: types.CallbackQuery):
    global language
    language = 'uz_ru'
    await bot.send_message(query.from_user.id, 'Siz "uz ➡️ ru" tilini tanladingiz\nKerakli matnni kiriting')


@dp.callback_query_handler(text='ru_en')
async def inline_button_callback(query: types.CallbackQuery):
    global language
    language = 'ru_en'
    await bot.send_message(query.from_user.id, 'Вы выбрали язык "ru ➡️ en"\nВведите текст, который хотите перевести')


@dp.callback_query_handler(text='en_ru')
async def inline_button_callback(query: types.CallbackQuery):
    global language
    language = 'en_ru'
    await bot.send_message(query.from_user.id, 'You chose "en ➡️ ru" language\nEnter the text you want to translate')


@dp.message_handler(content_types=['contact'])
async def contact(message: types.Message):
    user_contact = message.contact.phone_number
    text = f'Telefon raqamingiz qabul qilindi, tez orada siz bilan bog`lanamiz\nTelefon raqam: {user_contact}.'
    await bot.send_message(message.chat.id, text=text,   reply_markup=start_keyboards)


@dp.message_handler()
async def translation(message: types.Message):
    if message.text == '🏠 Bosh sahifa':
        await bot.send_message(message.chat.id, 'Bosh sahifaga qaytdik', reply_markup=start_keyboards)
    elif message.text == '🌐 Tilni tanlash':
        await bot.send_message(message.chat.id, 'Tilni tanlang', reply_markup=translations)
    elif message.text == '❓ Yordam':
        await bot.send_message(message.chat.id, 'Yordam bo`limiga qaytdik', reply_markup=start_keyboards)
    elif message.text == '📞 Aloqa':
        text = ('Aloqa bo`limiga xush kelibsiz!\n'
                'Iltimos admin siz bilan bog`lanishi uchun telefon raqamingizni qoldiring:')
        await bot.send_message(message.chat.id, text=text, reply_markup=contact_keyboard)
    elif message.text == '⬅️ Orqaga':
        await bot.send_message(message.chat.id, 'Orqaga qaytdik', reply_markup=start_keyboards)
    elif message.text == '🇺🇿 uz ➡️ en 🏴󠁧󠁢󠁥󠁮󠁧󠁿':
        await bot.send_message(message.chat.id, 'uz ➡️ en')
    elif message.text == '🏴󠁧󠁢󠁥󠁮󠁧󠁿 en ➡️ uz 🇺🇿':
        await bot.send_message(message.chat.id, 'en ➡️ uz')
    elif message.text == '🇷🇺 ru ➡️ uz 🇺🇿':
        await bot.send_message(message.chat.id, 'ru ➡️ uz')
    elif message.text == '🇺🇿 uz ➡️ ru 🇷🇺':
        await bot.send_message(message.chat.id, 'uz ➡️ ru')
    elif message.text == '🇷🇺 ru ➡️ en 🏴󠁧󠁢󠁥󠁮󠁧󠁿':
        await bot.send_message(message.chat.id, 'ru ➡️ en')
    elif message.text == '🏴󠁧󠁢󠁥󠁮󠁧󠁿 en ➡️ ru 🇷🇺':
        await bot.send_message(message.chat.id, 'en ➡️ ru')
    elif language == 'uz_en':
        await bot.send_message(message.chat.id, translate(message.text, 'en', 'uz'), reply_markup=start_keyboards)
    elif language == 'en_uz':
        await bot.send_message(message.chat.id, translate(message.text, 'uz', 'en'), reply_markup=start_keyboards)
    elif language == 'ru_uz':
        await bot.send_message(message.chat.id, translate(message.text, 'uz', 'ru'), reply_markup=start_keyboards)
    elif language == 'uz_ru':
        await bot.send_message(message.chat.id, translate(message.text, 'ru', 'uz'), reply_markup=start_keyboards)
    elif language == 'ru_en':
        await bot.send_message(message.chat.id, translate(message.text, 'en', 'ru'), reply_markup=start_keyboards)
    elif language == 'en_ru':
        await bot.send_message(message.chat.id, translate(message.text, 'ru', 'en'), reply_markup=start_keyboards)
    else:
        await bot.send_message(message.chat.id, 'Iltimos, tilni tanlang', reply_markup=translations)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

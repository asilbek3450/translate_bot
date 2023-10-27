import logging
import requests
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from buttons import start_keyboards, translations, contact_keyboard, buttons
from config import TOKEN
from func import translate
from data import language_messages, language_mappings

API_TOKEN = TOKEN

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

language = ''


@dp.message_handler(commands=['start'])
async def start_bot(message: types.Message):
    await bot.send_message(message.chat.id, f'Assalom aleykum, hurmatli {message.from_user.full_name}\n'
                                            f'Tarjimon botimizga xush kelibsiz!\n', reply_markup=start_keyboards)


@dp.message_handler(commands=['help'])
async def help_command(message: types.Message):
    await bot.send_message(message.chat.id, 'Yordam bo`limiga xush kelibsiz!\n'
                                            f'Botdan foydalanish uchun quyidagi buyruqlarni kiriting:\n\n'
                                            f'/start - Botni ishga tushurish\n'
                                            f'/help - Yordam\n'
                                            f'/contact - Aloqa bo`limiga o`tish\n'
                                            f'/language - Tilni tanlash\n'
                                            f'/back - Bosh sahifaga qaytish\n'
                                            f'/info - Bot haqida ma`lumot\n'
                                            f'/stop - Botni o`chirish\n'
                           )


@dp.message_handler(commands=['contact'])
async def contact_command(message: types.Message):
    text = ('Aloqa bo`limiga xush kelibsiz!\n'
            'Iltimos admin siz bilan bog`lanishi uchun telefon raqamingizni qoldiring:')
    await bot.send_message(message.chat.id, text=text, reply_markup=contact_keyboard)


@dp.message_handler(commands=['language'])
async def language_command(message: types.Message):
    await bot.send_message(message.chat.id, 'Tilni tanlang', reply_markup=translations)


@dp.message_handler(commands=['back'])
async def back_command(message: types.Message):
    await bot.send_message(message.chat.id, 'Bosh sahifaga qaytdik', reply_markup=start_keyboards)


@dp.message_handler(commands=['info'])
async def info_command(message: types.Message):
    text = ('Tarjimon botimizga xush kelibsiz!\n'
            'Bu bot orqali siz matnlaringizni turli tillarga tarjima qilishingiz mumkin.\n'
            'Tarjima qilish uchun quyidagi buyruqlarni kiriting:\n\n'
            '/start - Botni ishga tushurish\n'
            '/help - Yordam\n'
            '/contact - Aloqa bo`limiga o`tish\n'
            '/language - Tilni tanlash (Barcha tillar orasidan)\n'
            '/back - Bosh sahifaga qaytish\n'
            '/info - Bot haqida ma`lumot\n'
            '/stop - Botni o`chirish\n'
            )
    await bot.send_message(message.chat.id, text=text)


@dp.message_handler(commands=['stop'])
async def stop_command(message: types.Message):
    await bot.send_message(message.chat.id, 'Botni o`chirish uchun /stop ni bosing')
    await bot.send_message(message.chat.id, 'Bot o`chirildi', reply_markup=types.ReplyKeyboardRemove())


# Define the number of buttons per page
buttons_per_page = 2


def generate_buttons_page(page_num):
    start_idx = (page_num - 1) * buttons_per_page
    end_idx = start_idx + buttons_per_page
    return buttons[start_idx:end_idx]


# if text = '🌐 Tilni tanlash'
@dp.message_handler(lambda message: message.text == '🌐 Tilni tanlash')
async def send_buttons(message: types.Message):
    chat_id = message.chat.id
    page_num = 1  # Start with the first page
    markup = get_buttons_markup(page_num)

    # Send the initial message with buttons
    sent_message = await message.reply("Please select a language:", reply_markup=markup)


@dp.callback_query_handler(lambda callback_query: callback_query.data.startswith("next_page_"))
async def button_callback(callback_query: types.CallbackQuery):
    chat_id = callback_query.message.chat.id
    page_num = int(callback_query.data.split("_")[2])

    markup = get_buttons_markup(page_num)
    await bot.edit_message_reply_markup(chat_id=chat_id, message_id=callback_query.message.message_id,
                                        reply_markup=markup)


def get_buttons_markup(page_num):
    keyboard = generate_buttons_page(page_num)
    keyboard.append([InlineKeyboardButton("⬅️ Back", callback_data=f"next_page_{page_num - 1 if page_num > 1 else 7}"),
                     InlineKeyboardButton("Next ➡️", callback_data=f"next_page_{page_num + 1 if page_num < 8 else 1}")
                     ])
    return InlineKeyboardMarkup(inline_keyboard=keyboard)


@dp.callback_query_handler()
async def inline_button_callback(query: types.CallbackQuery):
    global language
    language = query.data

    if query.data in language_messages:
        message = language_messages[language]
        await bot.send_message(query.from_user.id, message)
    else:
        await bot.send_message(query.from_user.id, 'Iltimos, tilni tanlang', reply_markup=translations)


@dp.message_handler(content_types=['contact'])
async def contact(message: types.Message):
    user_contact = message.contact.phone_number
    text = f'Telefon raqamingiz qabul qilindi, tez orada siz bilan bog`lanamiz\nTelefon raqam: {user_contact}.'
    await bot.send_message(message.chat.id, text=text, reply_markup=start_keyboards)


@dp.message_handler()
async def translation(message: types.Message):
    if message.text == '🏠 Bosh sahifa':
        await bot.send_message(message.chat.id, 'Bosh sahifaga qaytdik', reply_markup=start_keyboards)
    elif message.text == '🌐 Tilni tanlash':
        await bot.send_message(message.chat.id, 'Tilni tanlang', reply_markup=translations)
    elif message.text == '❓ Yordam':
        await bot.send_message(message.chat.id, 'Yordam bo`limiga o\'tish uchun /help ni bosing',
                               reply_markup=start_keyboards)
    elif message.text == '📞 Aloqa':
        text = ('Aloqa bo`limiga xush kelibsiz!\n'
                'Iltimos admin siz bilan bog`lanishi uchun telefon raqamingizni qoldiring:')
        await bot.send_message(message.chat.id, text=text, reply_markup=contact_keyboard)
    elif message.text == '⬅️ Orqaga':
        await bot.send_message(message.chat.id, 'Orqaga qaytdik', reply_markup=start_keyboards)

    language_combination = language

    if language_combination in language_mappings:
        translation_target, translation_source = language_mappings[language_combination]
        translation_result = translate(message.text, translation_source, translation_target)
        await bot.send_message(message.chat.id, translation_result, reply_markup=start_keyboards)

    # else:
    #     await bot.send_message(message.chat.id, 'Iltimos, tilni tanlang', reply_markup=translations)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup

home_button = KeyboardButton('🏠 Bosh sahifa')
language_button = KeyboardButton('🌐 Tilni tanlash')
help_button = KeyboardButton('❓ Yordam')
contact_button = KeyboardButton('📞 Aloqa')
back_button = KeyboardButton('⬅️ Orqaga')

start_keyboards = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
start_keyboards.add(home_button, language_button)
start_keyboards.add(help_button, contact_button, back_button)

contact = KeyboardButton('Telefon raqamni yuborish', request_contact=True)
contact_keyboard = ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
contact_keyboard.add(contact, back_button)



uz_en = InlineKeyboardButton('🇺🇿 uz ➡️ en 🏴󠁧󠁢󠁥󠁮󠁧󠁿', callback_data='uz_en')
en_uz = InlineKeyboardButton('🏴󠁧󠁢󠁥󠁮󠁧󠁿 en ➡️ uz 🇺🇿', callback_data='en_uz')
ru_uz = InlineKeyboardButton('🇷🇺 ru ➡️ uz 🇺🇿', callback_data='ru_uz')
uz_ru = InlineKeyboardButton('🇺🇿 uz ➡️ ru 🇷🇺', callback_data='uz_ru')
ru_en = InlineKeyboardButton('🇷🇺 ru ➡️ en 🏴󠁧󠁢󠁥󠁮󠁧󠁿', callback_data='ru_en')
en_ru = InlineKeyboardButton('🏴󠁧󠁢󠁥󠁮󠁧󠁿 en ➡️ ru 🇷🇺', callback_data='en_ru')

translations = InlineKeyboardMarkup(row_width=2)
translations.add(uz_en, en_uz, ru_uz, uz_ru, ru_en, en_ru)


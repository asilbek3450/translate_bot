from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

home_button = KeyboardButton(text='🏠 Bosh sahifa')
language_button = KeyboardButton(text='🌐 Tilni tanlash')
help_button = KeyboardButton(text='❓ Yordam')
contact_button = KeyboardButton(text='📞 Aloqa')
back_button = KeyboardButton(text='⬅️ Orqaga')

# `keyboard` maydoni qo'shildi
start_keyboards = ReplyKeyboardMarkup(keyboard=[
    [home_button, language_button],
    [help_button, contact_button],
    [back_button]
], resize_keyboard=True)

contact_keyboard = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Telefon raqamni yuborish', request_contact=True)],
    [back_button]
], resize_keyboard=True)

# Inline tugmalar
uz_en = InlineKeyboardButton(text='🇺🇿 uz ➡️ en 🏴', callback_data='uz_en')
en_uz = InlineKeyboardButton(text='🏴 en ➡️ uz 🇺🇿', callback_data='en_uz')
ru_uz = InlineKeyboardButton(text='🇷🇺 ru ➡️ uz 🇺🇿', callback_data='ru_uz')
uz_ru = InlineKeyboardButton(text='🇺🇿 uz ➡️ ru 🇷🇺', callback_data='uz_ru')
ru_en = InlineKeyboardButton(text='🇷🇺 ru ➡️ en 🏴', callback_data='ru_en')
en_ru = InlineKeyboardButton(text='🏴 en ➡️ ru 🇷🇺', callback_data='en_ru')

uz_tr = InlineKeyboardButton(text='🇺🇿 uz ➡️ tr 🇹🇷', callback_data='uz_tr')
tr_uz = InlineKeyboardButton(text='🇹🇷 tr ➡️ uz 🇺🇿', callback_data='tr_uz')
ru_tr = InlineKeyboardButton(text='🇷🇺 ru ➡️ tr 🇹🇷', callback_data='ru_tr')
tr_ru = InlineKeyboardButton(text='🇹🇷 tr ➡️ ru 🇷🇺', callback_data='tr_ru')
en_tr = InlineKeyboardButton(text='🏴 en ➡️ tr 🇹🇷', callback_data='en_tr')
tr_en = InlineKeyboardButton(text='🇹🇷 tr ➡️ en 🏴', callback_data='tr_en')

uz_ar = InlineKeyboardButton(text='🇺🇿 uz ➡️ ar 🇸🇦', callback_data='uz_ar')
ar_uz = InlineKeyboardButton(text='🇸🇦 ar ➡️ uz 🇺🇿', callback_data='ar_uz')
ru_ar = InlineKeyboardButton(text='🇷🇺 ru ➡️ ar 🇸🇦', callback_data='ru_ar')
ar_ru = InlineKeyboardButton(text='🇸🇦 ar ➡️ ru 🇷🇺', callback_data='ar_ru')
en_ar = InlineKeyboardButton(text='🏴 en ➡️ ar 🇸🇦', callback_data='en_ar')
ar_en = InlineKeyboardButton(text='🇸🇦 ar ➡️ en 🏴', callback_data='ar_en')

uz_kk = InlineKeyboardButton(text='🇺🇿 uz ➡️ kk 🇰🇿', callback_data='uz_kk')
kk_uz = InlineKeyboardButton(text='🇰🇿 kk ➡️ uz 🇺🇿', callback_data='kk_uz')
ru_kk = InlineKeyboardButton(text='🇷🇺 ru ➡️ kk 🇰🇿', callback_data='ru_kk')
kk_ru = InlineKeyboardButton(text='🇰🇿 kk ➡️ ru 🇷🇺', callback_data='kk_ru')
en_kk = InlineKeyboardButton(text='🏴 en ➡️ kk 🇰🇿', callback_data='en_kk')
kk_en = InlineKeyboardButton(text='🇰🇿 kk ➡️ en 🏴', callback_data='kk_en')

uz_ko = InlineKeyboardButton(text='🇺🇿 uz ➡️ ko 🇰🇷', callback_data='uz_ko')
ko_uz = InlineKeyboardButton(text='🇰🇷 ko ➡️ uz 🇺🇿', callback_data='ko_uz')
ru_ko = InlineKeyboardButton(text='🇷🇺 ru ➡️ ko 🇰🇷', callback_data='ru_ko')
ko_ru = InlineKeyboardButton(text='🇰🇷 ko ➡️ ru 🇷🇺', callback_data='ko_ru')
en_ko = InlineKeyboardButton(text='🏴 en ➡️ ko 🇰🇷', callback_data='en_ko')
ko_en = InlineKeyboardButton(text='🇰🇷 ko ➡️ en 🏴', callback_data='ko_en')

uz_ja = InlineKeyboardButton(text='🇺🇿 uz ➡️ ja 🇯🇵', callback_data='uz_ja')
ja_uz = InlineKeyboardButton(text='🇯🇵 ja ➡️ uz 🇺🇿', callback_data='ja_uz')
ru_ja = InlineKeyboardButton(text='🇷🇺 ru ➡️ ja 🇯🇵', callback_data='ru_ja')
ja_ru = InlineKeyboardButton(text='🇯🇵 ja ➡️ ru 🇷🇺', callback_data='ja_ru')
en_ja = InlineKeyboardButton(text='🏴 en ➡️ ja 🇯🇵', callback_data='en_ja')
ja_en = InlineKeyboardButton(text='🇯🇵 ja ➡️ en 🏴', callback_data='ja_en')

uz_de = InlineKeyboardButton(text='🇺🇿 uz ➡️ de 🇩🇪', callback_data='uz_de')
de_uz = InlineKeyboardButton(text='🇩🇪 de ➡️ uz 🇺🇿', callback_data='de_uz')
ru_de = InlineKeyboardButton(text='🇷🇺 ru ➡️ de 🇩🇪', callback_data='ru_de')
de_ru = InlineKeyboardButton(text='🇩🇪 de ➡️ ru 🇷🇺', callback_data='de_ru')
en_de = InlineKeyboardButton(text='🏴 en ➡️ de 🇩🇪', callback_data='en_de')
de_en = InlineKeyboardButton(text='🇩🇪 de ➡️ en 🏴', callback_data='de_en')

# Inline markup
translations = InlineKeyboardMarkup(row_width=3, inline_keyboard=[
    [uz_en, en_uz, ru_uz],
    [uz_ru, ru_en, en_ru],
    [uz_tr, tr_uz, ru_tr],
    [tr_ru, en_tr, tr_en],
    [uz_ar, ar_uz, ru_ar],
    [ar_ru, en_ar, ar_en],
    [uz_kk, kk_uz, ru_kk],
    [kk_ru, en_kk, kk_en],
    [uz_ko, ko_uz, ru_ko],
    [ko_ru, en_ko, ko_en],
    [uz_ja, ja_uz, ru_ja],
    [ja_ru, en_ja, ja_en],
    [uz_de, de_uz, ru_de],
    [de_ru, en_de, de_en],
])

# Tugmalar ro'yxati (optional foydalanish uchun)
buttons = [
    [uz_en, en_uz, ru_uz],
    [uz_ru, ru_en, en_ru],
    [uz_tr, tr_uz, ru_tr],
    [tr_ru, en_tr, tr_en],
    [uz_ar, ar_uz, ru_ar],
    [ar_ru, en_ar, ar_en],
    [uz_kk, kk_uz, ru_kk],
    [kk_ru, en_kk, kk_en],
    [uz_ko, ko_uz, ru_ko],
    [ko_ru, en_ko, ko_en],
    [uz_ja, ja_uz, ru_ja],
    [ja_ru, en_ja, ja_en],
    [uz_de, de_uz, ru_de],
    [de_ru, en_de, de_en],
]

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

uz_tr = InlineKeyboardButton('🇺🇿 uz ➡️ tr 🇹🇷', callback_data='uz_tr')
tr_uz = InlineKeyboardButton('🇹🇷 tr ➡️ uz 🇺🇿', callback_data='tr_uz')
ru_tr = InlineKeyboardButton('🇷🇺 ru ➡️ tr 🇹🇷', callback_data='ru_tr')
tr_ru = InlineKeyboardButton('🇹🇷 tr ➡️ ru 🇷🇺', callback_data='tr_ru')
en_tr = InlineKeyboardButton('🏴󠁧󠁢󠁥󠁮󠁧󠁿 en ➡️ tr 🇹🇷', callback_data='en_tr')
tr_en = InlineKeyboardButton('🇹🇷 tr ➡️ en 🏴󠁧󠁢󠁥󠁮󠁧󠁿', callback_data='tr_en')

uz_ar = InlineKeyboardButton('🇺🇿 uz ➡️ ar 🇸🇦', callback_data='uz_ar')
ar_uz = InlineKeyboardButton('🇸🇦 ar ➡️ uz 🇺🇿', callback_data='ar_uz')
ru_ar = InlineKeyboardButton('🇷🇺 ru ➡️ ar 🇸🇦', callback_data='ru_ar')
ar_ru = InlineKeyboardButton('🇸🇦 ar ➡️ ru 🇷🇺', callback_data='ar_ru')
en_ar = InlineKeyboardButton('🏴󠁧󠁢󠁥󠁮󠁧󠁿 en ➡️ ar 🇸🇦', callback_data='en_ar')
ar_en = InlineKeyboardButton('🇸🇦 ar ➡️ en 🏴󠁧󠁢󠁥󠁮󠁧󠁿', callback_data='ar_en')

uz_kk = InlineKeyboardButton('🇺🇿 uz ➡️ kk 🇰🇿', callback_data='uz_kk')
kk_uz = InlineKeyboardButton('🇰🇿 kk ➡️ uz 🇺🇿', callback_data='kk_uz')
ru_kk = InlineKeyboardButton('🇷🇺 ru ➡️ kk 🇰🇿', callback_data='ru_kk')
kk_ru = InlineKeyboardButton('🇰🇿 kk ➡️ ru 🇷🇺', callback_data='kk_ru')
en_kk = InlineKeyboardButton('🏴󠁧󠁢󠁥󠁮󠁧󠁿 en ➡️ kk 🇰🇿', callback_data='en_kk')
kk_en = InlineKeyboardButton('🇰🇿 kk ➡️ en 🏴󠁧󠁢󠁥󠁮󠁧󠁿', callback_data='kk_en')

uz_ko = InlineKeyboardButton('🇺🇿 uz ➡️ ko 🇰🇷', callback_data='uz_ko')
ko_uz = InlineKeyboardButton('🇰🇷 ko ➡️ uz 🇺🇿', callback_data='ko_uz')
ru_ko = InlineKeyboardButton('🇷🇺 ru ➡️ ko 🇰🇷', callback_data='ru_ko')
ko_ru = InlineKeyboardButton('🇰🇷 ko ➡️ ru 🇷🇺', callback_data='ko_ru')
en_ko = InlineKeyboardButton('🏴󠁧󠁢󠁥󠁮󠁧󠁿 en ➡️ ko 🇰🇷', callback_data='en_ko')
ko_en = InlineKeyboardButton('🇰🇷 ko ➡️ en 🏴󠁧󠁢󠁥󠁮󠁧󠁿', callback_data='ko_en')

uz_ja = InlineKeyboardButton('🇺🇿 uz ➡️ ja 🇯🇵', callback_data='uz_ja')
ja_uz = InlineKeyboardButton('🇯🇵 ja ➡️ uz 🇺🇿', callback_data='ja_uz')
ru_ja = InlineKeyboardButton('🇷🇺 ru ➡️ ja 🇯🇵', callback_data='ru_ja')
ja_ru = InlineKeyboardButton('🇯🇵 ja ➡️ ru 🇷🇺', callback_data='ja_ru')
en_ja = InlineKeyboardButton('🏴󠁧󠁢󠁥󠁮󠁧󠁿 en ➡️ ja 🇯🇵', callback_data='en_ja')
ja_en = InlineKeyboardButton('🇯🇵 ja ➡️ en 🏴󠁧󠁢󠁥󠁮󠁧󠁿', callback_data='ja_en')

uz_de = InlineKeyboardButton('🇺🇿 uz ➡️ de 🇩🇪', callback_data='uz_de')
de_uz = InlineKeyboardButton('🇩🇪 de ➡️ uz 🇺🇿', callback_data='de_uz')
ru_de = InlineKeyboardButton('🇷🇺 ru ➡️ de 🇩🇪', callback_data='ru_de')
de_ru = InlineKeyboardButton('🇩🇪 de ➡️ ru 🇷🇺', callback_data='de_ru')
en_de = InlineKeyboardButton('🏴󠁧󠁢󠁥󠁮󠁧󠁿 en ➡️ de 🇩🇪', callback_data='en_de')
de_en = InlineKeyboardButton('🇩🇪 de ➡️ en 🏴󠁧󠁢󠁥󠁮󠁧󠁿', callback_data='de_en')

translations = InlineKeyboardMarkup(row_width=3)
translations.add(uz_en, en_uz, ru_uz, uz_ru, ru_en, en_ru)
translations.add(uz_tr, tr_uz, ru_tr, tr_ru, en_tr, tr_en)
translations.add(uz_ar, ar_uz, ru_ar, ar_ru, en_ar, ar_en)
translations.add(uz_kk, kk_uz, ru_kk, kk_ru, en_kk, kk_en)
translations.add(uz_ko, ko_uz, ru_ko, ko_ru, en_ko, ko_en)
translations.add(uz_ja, ja_uz, ru_ja, ja_ru, en_ja, ja_en)
translations.add(uz_de, de_uz, ru_de, de_ru, en_de, de_en)


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

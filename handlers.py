from aiogram import Router, types
from aiogram import F
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message, CallbackQuery
from buttons import start_keyboards, translations, contact_keyboard, buttons
from data import language_messages, language_mappings
from func import translate
from aiogram.fsm.state import State, StatesGroup
from aiogram.filters import StateFilter

from aiogram.fsm.context import FSMContext

class Form(StatesGroup):
    contact = State()
router = Router()

language = ''
buttons_per_page = 2

def generate_buttons_page(page_num):
    start_idx = (page_num - 1) * buttons_per_page
    end_idx = start_idx + buttons_per_page
    return buttons[start_idx:end_idx]

def get_buttons_markup(page_num):
    keyboard = generate_buttons_page(page_num)
    keyboard.append([ 
        InlineKeyboardButton("⬅️ Back", callback_data=f"next_page_{page_num - 1 if page_num > 1 else 7}"),
        InlineKeyboardButton("Next ➡️", callback_data=f"next_page_{page_num + 1 if page_num < 8 else 1}")
    ])
    return InlineKeyboardMarkup(inline_keyboard=keyboard)

# Use F.text for command matching
@router.message(F.text == "/start")
async def start_bot(message: Message):
    await message.answer(f'Assalom aleykum, hurmatli {message.from_user.full_name}\n'
                         f'Tarjimon botimizga xush kelibsiz!\n', reply_markup=start_keyboards)

# Similarly for other commands like /help, /contact etc.
@router.message(F.text == "/help")
async def help_command(message: Message):
    await message.answer('Yordam bo‘limiga xush kelibsiz!\n'
                         '/start - Botni ishga tushurish\n'
                         '/help - Yordam\n'
                         '/contact - Aloqa\n'
                         '/language - Til tanlash\n'
                         '/back - Bosh sahifa\n'
                         '/info - Bot haqida\n'
                         '/stop - Botni o‘chirish')

@router.message(F.text == "/contact")
async def contact_command(message: Message):
    await message.answer('Aloqa bo‘limiga xush kelibsiz!\nTelefon raqamingizni yuboring.', reply_markup=contact_keyboard)
    await Form.contact.set()

@router.message(F.text == "/language")
async def language_command(message: Message):
    await message.answer('Tilni tanlang', reply_markup=translations)

@router.message(F.text == "/back")
async def back_command(message: Message):
    await message.answer('Bosh sahifaga qaytdik', reply_markup=start_keyboards)

@router.message(F.text == "/info")
async def info_command(message: Message):
    await message.answer('Bot haqida ma’lumot...\n/start\n/help\n/contact\n/language\n/back\n/info\n/stop')

@router.message(F.text == "/stop")
async def stop_command(message: Message):
    await message.answer('Bot o‘chirildi', reply_markup=types.ReplyKeyboardRemove())

# For handling button text commands
@router.message(F.text == "🌐 Tilni tanlash")
async def send_buttons(message: Message):
    page_num = 1
    markup = get_buttons_markup(page_num)
    await message.answer("Tilni tanlang:", reply_markup=markup)

# Your callback_query handler remains the same
@router.callback_query(lambda call: call.data.startswith("next_page_"))
async def button_callback(callback_query: CallbackQuery):
    page_num = int(callback_query.data.split("_")[2])
    markup = get_buttons_markup(page_num)
    await callback_query.message.edit_reply_markup(reply_markup=markup)

@router.callback_query()
async def inline_button_callback(query: CallbackQuery):
    global language
    language = query.data
    if query.data in language_messages:
        await query.message.answer(language_messages[language])
    else:
        await query.message.answer('Iltimos, tilni tanlang', reply_markup=translations)

@router.message(StateFilter(Form.contact))
async def contact(message: Message):
    user_contact = message.contact.phone_number
    await message.answer(f'Telefon raqamingiz qabul qilindi: {user_contact}', reply_markup=start_keyboards)

@router.message()
async def translation(message: Message, state: FSMContext):
    global language
    if message.text == '🏠 Bosh sahifa':
        await message.answer('Bosh sahifaga qaytdik', reply_markup=start_keyboards)
    elif message.text == '🌐 Tilni tanlash':
        await message.answer('Tilni tanlang', reply_markup=translations)
    elif message.text == '❓ Yordam':
        await message.answer('Yordam bo‘limiga o‘ting: /help', reply_markup=start_keyboards)
    elif message.text == '📞 Aloqa':
        await message.answer('Aloqa uchun telefon raqamingizni yuboring', reply_markup=contact_keyboard)
        await state.set_state('contact')

    elif message.text == '⬅️ Orqaga':
        await message.answer('Orqaga qaytdik', reply_markup=start_keyboards)
    
    if language in language_mappings:
        translation_source, translation_target = language_mappings[language]
        translation_result = translate(message.text, translation_target, translation_source)
        await message.answer(translation_result, reply_markup=start_keyboards)

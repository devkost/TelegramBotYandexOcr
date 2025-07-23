from aiogram import Router, F
from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.filters import CommandStart

from model.yandex_vision_api import request_to_convert

from app.keyboards import CreateKeyboardWords


Router = Router()
PhotoData = []

@Router.message( CommandStart() )
async def cmd_start( message: Message ):
    answer_text = f"""
<b>📸 Бот для распознавания текста с фото</b>

Привет, {message.from_user.first_name}! Я могу:

• Распознавать текст с изображений (JPG/PNG)
• Поддерживаю русский и английский языки
• Работаю даже с плохим качеством фото

<i>Просто отправь мне фото с текстом!</i>

🛠 Этот бот - часть школьного проекта по ИИ.
<b>Автор: Юшко Константин | Ученик 11А класса</b>"""

    await message.answer( answer_text, parse_mode="HTML" )

@Router.message( F.photo )
async def cmd_photo( message: Message ):
    PhotoData.append( message )

    return message.answer( "Теперь выберите тип текста:", reply_markup=CreateKeyboardWords() )

@Router.message(F.text.in_(["🖨 Печатный текст", "✍️ Рукописный текст"]))
async def set_text_type( message: Message ):
    temp_msg = await message.answer("🔄 Изображение получено, начинаю распознавание...")

    model_type = ( "Рукописный" in message.text ) and "handwritten" or "page"

    data = PhotoData[ 0 ]
    if not data.message_id:
        return message.answer( "❌ Error", reply_markup = ReplyKeyboardRemove() )

    file = await data.bot.get_file( data.photo[ -1 ].file_id )
    file_path = file.file_path

    photo_bytes = await message.bot.download_file( file_path )
    photo_bytes = photo_bytes.read()

    response = request_to_convert( photo_bytes, model_type )

    PhotoData.clear()

    await temp_msg.delete()

    await message.answer( response, reply_markup= ReplyKeyboardRemove(), parse_mode="HTML" )
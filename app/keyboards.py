from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

def CreateKeyboardWords():
    buttons = [ KeyboardButton( text = "🖨 Печатный текст" ), KeyboardButton( text= "✍️ Рукописный текст" ) ]
    keyboard = ReplyKeyboardMarkup( keyboard = [ buttons ], resize_keyboard=True, input_field_placeholder="Выберите вид текста, чтобы бот смог определить модель" )

    return keyboard
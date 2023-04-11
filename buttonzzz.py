from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

# Кнопка для отправки номера:
def phone_number_kb():
    kb = ReplyKeyboardMarkup(resize_keyboard=True)

    button = KeyboardButton('Share contact', request_contact=True)

    return kb

# Кнопка для отправки локации
def location_kb():
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    button = KeyboardButton('Share contact', request_location=True)

    return kb


# Кнопка для выбора пола
def gender_kb():
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    button = KeyboardButton('Мужчина')
    button2 = KeyboardButton('Женщина')

    return kb

#Кнопки для выбора количества
def product_count():
    kb = ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)

    buttons = [KeyboardButton(str(i)) for i in range(1, 10)]
    back = KeyboardButton('Назад')

    kb.add(*buttons, back)

    return kb

# Корзина

def cart_kb():
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    button = KeyboardButton('Очистить')
    button2 = KeyboardButton('Оформит')
    button3 = KeyboardButton('Редактировать')
    button4 = KeyboardButton('Назад')

    kb.add(button, button2, button3, button4)

    return kb

# Кнопки при выборе способа оплаты

def pay_type_kb():
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    button = KeyboardButton('Наличные')
    button2 = KeyboardButton('Картой')
    button3 = KeyboardButton('Назад')
    kb.add(button, button2, button3)

    return kb

# Кнопки для подтверждения заказа

def confirmation_kb():
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    button = KeyboardButton('Подтвердить')
    button2 = KeyboardButton('Отменить')
    button3 = KeyboardButton('Назад')

    kb.add(button, button2, button3)

    return kb

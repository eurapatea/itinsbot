import telebot
from telebot import types

bot = telebot.TeleBot('7236728689:AAGQdE4Tios98YsLgMBcJpXZJOWlZQpYBoA')


# СНЯТЬ В  АРЕНДЫ
def rent(message, bot):
    markup = types.ReplyKeyboardMarkup(row_width=2)
    itembtn_rent1 = types.KeyboardButton('Квартира для аренды')
    itembtn_rent2 = types.KeyboardButton('Дом для аренды')
    itembtn_rent3 = types.KeyboardButton('Апартаменты для аренды')
    itembtn_rent4 = types.KeyboardButton('Коммерческая недвижимость для аренды')
    itembtn_rent5 = types.KeyboardButton('Назад')
    markup.add(itembtn_rent1, itembtn_rent2, itembtn_rent3, itembtn_rent4, itembtn_rent5)
    bot.reply_to(message, "Отлично, выберите то, что вас интересует!", reply_markup=markup)

def specific_rent(message, bot):
    if message.text in ['Квартира для аренды', 'Дом для аренды', 'Апартаменты для аренды', 'Коммерческая недвижимость для аренды']:
        markup = types.ReplyKeyboardMarkup(row_width=2)
        itembtn_rent_location1 = types.KeyboardButton('Ленинградская область')
        itembtn_rent_location2 = types.KeyboardButton('Санкт-Петербург')
        itembtn_rent_location3 = types.KeyboardButton('Назад')
        markup.add(itembtn_rent_location1, itembtn_rent_location2, itembtn_rent_location3)
        bot.reply_to(message, "Желаемое месторасположение", reply_markup=markup)

def spb_districts_rent(message, bot):
    if message.text == 'Санкт-Петербург':
        markup = types.ReplyKeyboardMarkup(row_width=2)
        itembtn_rent_district1 = types.KeyboardButton('Адмиралтейский район для аренды')
        itembtn_rent_district2 = types.KeyboardButton('Василеостровский район для аренды')
        itembtn_rent_district3 = types.KeyboardButton('Выборгский район для аренды')
        itembtn_rent_district4 = types.KeyboardButton('Калининский район для аренды')
        itembtn_rent_district5 = types.KeyboardButton('Кировский район для аренды')
        itembtn_rent_district6 = types.KeyboardButton('Колпинский район для аренды')
        itembtn_rent_district7 = types.KeyboardButton('Красногвардейский район для аренды')
        itembtn_rent_district8 = types.KeyboardButton('Красносельский район для аренды')
        itembtn_rent_district9 = types.KeyboardButton('Кронштадтский район для аренды')
        itembtn_rent_district10 = types.KeyboardButton('Курортный район для аренды')
        itembtn_rent_district11 = types.KeyboardButton('Московский район для аренды')
        itembtn_rent_district12 = types.KeyboardButton('Невский район для аренды')
        itembtn_rent_district13 = types.KeyboardButton('Петроградский район для аренды')
        itembtn_rent_district14 = types.KeyboardButton('Петродворцовый район для аренды')
        itembtn_rent_district15 = types.KeyboardButton('Приморский район для аренды')
        itembtn_rent_district16 = types.KeyboardButton('Пушкинский район для аренды')
        itembtn_rent_district17 = types.KeyboardButton('Фрунзенский район для аренды')
        itembtn_rent_district18 = types.KeyboardButton('Центральный район для аренды')
        itembtn_rent_district19 = types.KeyboardButton('Назад')
        markup.add(itembtn_rent_district1, itembtn_rent_district2, itembtn_rent_district3, itembtn_rent_district4, itembtn_rent_district5, itembtn_rent_district6, itembtn_rent_district7, itembtn_rent_district8, itembtn_rent_district9, itembtn_rent_district10, itembtn_rent_district11, itembtn_rent_district12, itembtn_rent_district13, itembtn_rent_district14, itembtn_rent_district15, itembtn_rent_district16, itembtn_rent_district17, itembtn_rent_district18, itembtn_rent_district19)
        bot.reply_to(message, "Выберите район", reply_markup=markup)

def request_accepted_rent(message, bot):
    bot.reply_to(message, "Заявка принята!")


# СДАТЬ В АРЕНДУ
def rent3(message, bot):
    markup = types.ReplyKeyboardMarkup(row_width=2)
    itembtn_rent1 = types.KeyboardButton('Квартира для аренды')
    itembtn_rent2 = types.KeyboardButton('Дом для аренды')
    itembtn_rent3 = types.KeyboardButton('Апартаменты для аренды')
    itembtn_rent4 = types.KeyboardButton('Коммерческая недвижимость для аренды')
    itembtn_rent5 = types.KeyboardButton('Назад')
    markup.add(itembtn_rent1, itembtn_rent2, itembtn_rent3, itembtn_rent4, itembtn_rent5)
    bot.reply_to(message, "Отлично, выберите то, что вас интересует!", reply_markup=markup)

def specifi3c_rent(message, bot):
    if message.text in ['Квартира для аренды', 'Дом для аренды', 'Апартаменты для аренды', 'Коммерческая недвижимость для аренды']:
        markup = types.ReplyKeyboardMarkup(row_width=2)
        itembtn_rent_location1 = types.KeyboardButton('Ленинградская область')
        itembtn_rent_location2 = types.KeyboardButton('Санкт-Петербург')
        itembtn_rent_location3 = types.KeyboardButton('Назад')
        markup.add(itembtn_rent_location1, itembtn_rent_location2, itembtn_rent_location3)
        bot.reply_to(message, "Желаемое месторасположение", reply_markup=markup)

def spb2_districts_rent(message, bot):
    if message.text == 'Санкт-Петербург':
        markup = types.ReplyKeyboardMarkup(row_width=2)
        itembtn_rent_district1 = types.KeyboardButton('Адмиралтейский район для аренды')
        itembtn_rent_district2 = types.KeyboardButton('Василеостровский район для аренды')
        itembtn_rent_district3 = types.KeyboardButton('Выборгский район для аренды')
        itembtn_rent_district4 = types.KeyboardButton('Калининский район для аренды')
        itembtn_rent_district5 = types.KeyboardButton('Кировский район для аренды')
        itembtn_rent_district6 = types.KeyboardButton('Колпинский район для аренды')
        itembtn_rent_district7 = types.KeyboardButton('Красногвардейский район для аренды')
        itembtn_rent_district8 = types.KeyboardButton('Красносельский район для аренды')
        itembtn_rent_district9 = types.KeyboardButton('Кронштадтский район для аренды')
        itembtn_rent_district10 = types.KeyboardButton('Курортный район для аренды')
        itembtn_rent_district11 = types.KeyboardButton('Московский район для аренды')
        itembtn_rent_district12 = types.KeyboardButton('Невский район для аренды')
        itembtn_rent_district13 = types.KeyboardButton('Петроградский район для аренды')
        itembtn_rent_district14 = types.KeyboardButton('Петродворцовый район для аренды')
        itembtn_rent_district15 = types.KeyboardButton('Приморский район для аренды')
        itembtn_rent_district16 = types.KeyboardButton('Пушкинский район для аренды')
        itembtn_rent_district17 = types.KeyboardButton('Фрунзенский район для аренды')
        itembtn_rent_district18 = types.KeyboardButton('Центральный район для аренды')
        itembtn_rent_district19 = types.KeyboardButton('Назад')
        markup.add(itembtn_rent_district1, itembtn_rent_district2, itembtn_rent_district3, itembtn_rent_district4, itembtn_rent_district5, itembtn_rent_district6, itembtn_rent_district7, itembtn_rent_district8, itembtn_rent_district9, itembtn_rent_district10, itembtn_rent_district11, itembtn_rent_district12, itembtn_rent_district13, itembtn_rent_district14, itembtn_rent_district15, itembtn_rent_district16, itembtn_rent_district17, itembtn_rent_district18, itembtn_rent_district19)
        bot.reply_to(message, "Выберите район", reply_markup=markup)

def request3_accepted_rent(message, bot):
    bot.reply_to(message, "Заявка принята!")



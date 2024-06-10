import telebot
from telebot import types
import func

API_TOKEN = "7236728689:AAGQdE4Tios98YsLgMBcJpXZJOWlZQpYBoA"
bot = telebot.TeleBot(API_TOKEN)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = types.ReplyKeyboardMarkup(row_width=2)
    itembtn1 = types.KeyboardButton('Покупка')
    itembtn2 = types.KeyboardButton('Продажа')
    itembtn3 = types.KeyboardButton('Сдать в аренду')
    itembtn4 = types.KeyboardButton('Снять в аренду')
    itembtn5 = types.KeyboardButton('Управление недвижимостью')
    itembtn6 = types.KeyboardButton('Юридическое сопровождение сделки')
    markup.add(itembtn1, itembtn2, itembtn3, itembtn4, itembtn5, itembtn6)
    bot.reply_to(message, "Здравствуйте! Какой вопрос о недвижимости вас интересует?", reply_markup=markup)

@bot.message_handler(func=lambda message: message.text in ['Ленинградская область', 'Адмиралтейский район', 'Василеостровский район', 'Выборгский район', 'Калининский район', 'Кировский район', 'Колпинский район', 'Красногвардейский район', 'Красносельский район', 'Кронштадтский район', 'Курортный район', 'Московский район', 'Невский район', 'Петроградский район', 'Петродворцовый район', 'Приморский район', 'Пушкинский район', 'Фрунзенский район', 'Центральный район'])
def request_accepted(message):
    bot.reply_to(message, "Заявка принята !")
    markup = types.ReplyKeyboardMarkup(row_width=2)
    itembtn1 = types.KeyboardButton('Покупка')
    itembtn2 = types.KeyboardButton('Продажа')
    itembtn3 = types.KeyboardButton('Сдать в аренду')
    itembtn4 = types.KeyboardButton('Снять в аренду')
    itembtn5 = types.KeyboardButton('Управление недвижимостью')
    itembtn6 = types.KeyboardButton('Юридическое сопровождение сделки')
    markup.add(itembtn1, itembtn2, itembtn3, itembtn4, itembtn5, itembtn6)
    bot.reply_to(message, "Здравствуйте, Какой вопрос о недвижимости вас интересует?", reply_markup=markup)

# Юридическое сопровождение сделки

@bot.message_handler(func=lambda message: message.text == 'Юридическое сопровождение сделки')
def legal_support(message):
    bot.reply_to(message, "Как я могу к вам обращаться?")
    bot.register_next_step_handler(message, get_name)

def get_name(message):
    name = message.text
    markup = types.ReplyKeyboardMarkup(row_width=2)
    itembtn1 = types.KeyboardButton('Telegram')
    itembtn2 = types.KeyboardButton('Телефон')
    itembtn3 = types.KeyboardButton('WhatsApp')
    itembtn4 = types.KeyboardButton('Назад')
    markup.add(itembtn1, itembtn2, itembtn3, itembtn4)
    bot.reply_to(message, "Выберите способ связи", reply_markup=markup)
    bot.register_next_step_handler(message, lambda message: get_contact(message, name))

def get_contact(message, name):
    if message.text == 'Назад':
        bot.reply_to(message, "Здравствуйте Какой вопрос о недвижимости вас интересует?")
        markup = types.ReplyKeyboardMarkup(row_width=2)
        itembtn1 = types.KeyboardButton('Покупка')
        itembtn2 = types.KeyboardButton('Продажа')
        itembtn3 = types.KeyboardButton('Сдать в аренду')
        itembtn4 = types.KeyboardButton('Снять в аренду')
        itembtn5 = types.KeyboardButton('Управление недвижимостью')
        itembtn6 = types.KeyboardButton('Юридическое сопровождение сделки')
        markup.add(itembtn1, itembtn2, itembtn3, itembtn4, itembtn5, itembtn6)
        bot.reply_to(message, "Здравствуйте, Какой вопрос о недвижимости вас интересует?", reply_markup=markup)
    else:
        contact = message.text
        bot.reply_to(message, "Оставьте свой телефон для связи")
        bot.register_next_step_handler(message, lambda message: get_phone(message, name, contact))

def get_phone(message, name, contact):
    phone = message.text
    bot.reply_to(message, f"{name}, Мы свяжемся с вами для согласования времени проведения бесплатной консультации")
    markup = types.ReplyKeyboardMarkup(row_width=2)
    itembtn1 = types.KeyboardButton('Покупка')
    itembtn2 = types.KeyboardButton('Продажа')
    itembtn3 = types.KeyboardButton('Сдать в аренду')
    itembtn4 = types.KeyboardButton('Снять в аренду')
    itembtn5 = types.KeyboardButton('Управление недвижимостью')
    itembtn6 = types.KeyboardButton('Юридическое сопровождение сделки')
    markup.add(itembtn1, itembtn2, itembtn3, itembtn4, itembtn5, itembtn6)
    bot.reply_to(message, "Здравствуйте, Какой вопрос о недвижимости вас интересует?!", reply_markup=markup)

@bot.message_handler(func=lambda message: message.text == 'Покупка')
def purchase(message):
    markup = types.ReplyKeyboardMarkup(row_width=2)
    itembtn1 = types.KeyboardButton('Квартира')
    itembtn2 = types.KeyboardButton('Дом')
    itembtn3 = types.KeyboardButton('Земельный участок')
    itembtn4 = types.KeyboardButton('Коммерческая недвижимость')
    itembtn5 = types.KeyboardButton('Апартаменты')
    itembtn6 = types.KeyboardButton('Назад')
    markup.add(itembtn1, itembtn2, itembtn3, itembtn4, itembtn5, itembtn6)
    bot.reply_to(message, "Отлично!, выберите подходящий вам вариант!", reply_markup=markup)

@bot.message_handler(func=lambda message: message.text in ['Квартира', 'Дом', 'Земельный участок', 'Апартаменты'])
def specific_interest(message):
    markup = types.ReplyKeyboardMarkup(row_width=2)
    if message.text == 'Квартира':
        itembtn1 = types.KeyboardButton('Новостройка')
        itembtn2 = types.KeyboardButton('Вторичное жилье')
        itembtn3 = types.KeyboardButton('Назад')
        markup.add(itembtn1, itembtn2, itembtn3)
    elif message.text == 'Дом':
        itembtn1 = types.KeyboardButton('Готовый')
        itembtn2 = types.KeyboardButton('Строящийся')
        itembtn3 = types.KeyboardButton('Назад')
        markup.add(itembtn1, itembtn2, itembtn3)
    elif message.text == 'Земельный участок':
        itembtn1 = types.KeyboardButton('Для инвестиций')
        itembtn2 = types.KeyboardButton('Для строительства')
        itembtn3 = types.KeyboardButton('Назад')
        markup.add(itembtn1, itembtn2, itembtn3)
    else:
        itembtn1 = types.KeyboardButton('Далее')
        itembtn2 = types.KeyboardButton('Назад')
        markup.add(itembtn1, itembtn2)
    bot.reply_to(message, "Что вас конкретно интересует?", reply_markup=markup)

@bot.message_handler(func=lambda message: message.text in ['Новостройка', 'Вторичное жилье', 'Готовый', 'Строящийся', 'Далее'])
def specific_purpose(message):
    markup = types.ReplyKeyboardMarkup(row_width=2)
    itembtn1 = types.KeyboardButton('Для проживания')
    itembtn2 = types.KeyboardButton('Для инвестиций')
    itembtn3 = types.KeyboardButton('Назад')
    markup.add(itembtn1, itembtn2, itembtn3)
    bot.reply_to(message, "Для каких целей нужна недвижимость?", reply_markup=markup)

@bot.message_handler(func=lambda message: message.text in ['Для проживания', 'Для инвестиций'])
def location(message):
    markup = types.ReplyKeyboardMarkup(row_width=2)
    itembtn1 = types.KeyboardButton('Ленинградская область')
    itembtn2 = types.KeyboardButton('Санкт-Петербург')
    itembtn3 = types.KeyboardButton('Назад')
    markup.add(itembtn1, itembtn2, itembtn3)
    bot.reply_to(message, "Желаемое месторасположение", reply_markup=markup)

@bot.message_handler(func=lambda message: message.text == 'Санкт-Петербург')
def spb_districts(message):
    markup = types.ReplyKeyboardMarkup(row_width=2)
    itembtn1 = types.KeyboardButton('Адмиралтейский район')
    itembtn2 = types.KeyboardButton('Василеостровский район')
    itembtn3 = types.KeyboardButton('Выборгский район')
    itembtn4 = types.KeyboardButton('Калининский район')
    itembtn5 = types.KeyboardButton('Кировский район')
    itembtn6 = types.KeyboardButton('Колпинский район')
    itembtn7 = types.KeyboardButton('Красногвардейский район')
    itembtn8 = types.KeyboardButton('Красносельский район')
    itembtn9 = types.KeyboardButton('Кронштадтский район')
    itembtn10 = types.KeyboardButton('Курортный район')
    itembtn11 = types.KeyboardButton('Московский район')
    itembtn12 = types.KeyboardButton('Невский район')
    itembtn13 = types.KeyboardButton('Петроградский район')
    itembtn14 = types.KeyboardButton('Петродворцовый район')
    itembtn15 = types.KeyboardButton('Приморский район')
    itembtn16 = types.KeyboardButton('Пушкинский район')
    itembtn17 = types.KeyboardButton('Фрунзенский район')
    itembtn18 = types.KeyboardButton('Центральный район')
    itembtn19 = types.KeyboardButton('Назад')
    markup.add(itembtn1, itembtn2, itembtn3, itembtn4, itembtn5, itembtn6, itembtn7, itembtn8, itembtn9, itembtn10, itembtn11, itembtn12, itembtn13, itembtn14, itembtn15, itembtn16, itembtn17, itembtn18, itembtn19)
    bot.reply_to(message, "Выберите район", reply_markup=markup)

@bot.message_handler(func=lambda message: message.text in ['Ленинградская область', 'Адмиралтейский район', 'Василеостровский район', 'Выборгский район', 'Калининский район', 'Кировский район', 'Колпинский район', 'Красногвардейский район', 'Красносельский район', 'Кронштадтский район', 'Курортный район', 'Московский район', 'Невский район', 'Петроградский район', 'Петродворцовый район', 'Приморский район', 'Пушкинский район', 'Фрунзенский район', 'Центральный район'])
def request_accepted(message):
    bot.reply_to(message, "Заявка принята!")

@bot.message_handler(func=lambda message: message.text in ['Для инвестиций', 'Для строительства'])
def location_land(message):
    markup = types.ReplyKeyboardMarkup(row_width=2)
    itembtn1 = types.KeyboardButton('Ленинградская область')
    itembtn2 = types.KeyboardButton('Санкт-Петербург')
    itembtn3 = types.KeyboardButton('Назад')
    markup.add(itembtn1, itembtn2, itembtn3)
    bot.reply_to(message, "Желаемое месторасположение", reply_markup=markup)

@bot.message_handler(func=lambda message: message.text == 'Коммерческая недвижимость')
def commercial_property(message):
    markup = types.ReplyKeyboardMarkup(row_width=2)
    itembtn1 = types.KeyboardButton('Строящаяся')
    itembtn2 = types.KeyboardButton('Готовая')
    itembtn3 = types.KeyboardButton('Назад')
    markup.add(itembtn1, itembtn2, itembtn3)
    bot.reply_to(message, "Что вас конкретно интересует?", reply_markup=markup)

@bot.message_handler(func=lambda message: message.text in ['Строящаяся', 'Готовая'])
def commercial_purpose(message):
    markup = types.ReplyKeyboardMarkup(row_width=2)
    itembtn1 = types.KeyboardButton('Для собственного использования')
    itembtn2 = types.KeyboardButton('Для инвестиций')
    itembtn3 = types.KeyboardButton('Назад')
    markup.add(itembtn1, itembtn2, itembtn3)
    bot.reply_to(message, "Для каких целей нужна недвижимость?", reply_markup=markup)

@bot.message_handler(func=lambda message: message.text in ['Для собственного использования', 'Для инвестиций'])
def commercial_location(message):
    markup = types.ReplyKeyboardMarkup(row_width=2)
    itembtn1 = types.KeyboardButton('Ленинградская область')
    itembtn2 = types.KeyboardButton('Санкт-Петербург')
    itembtn3 = types.KeyboardButton('Назад')
    markup.add(itembtn1, itembtn2, itembtn3)
    bot.reply_to(message, "Желаемое месторасположение", reply_markup=markup)

@bot.message_handler(func=lambda message: message.text == 'Апартаменты')
def apartments(message):
    markup = types.ReplyKeyboardMarkup(row_width=2)
    itembtn1 = types.KeyboardButton('Строящиеся')
    itembtn2 = types.KeyboardButton('Готовые')
    itembtn3 = types.KeyboardButton('Назад')
    markup.add(itembtn1, itembtn2, itembtn3)
    bot.reply_to(message, "Что вас конкретно интересует?", reply_markup=markup)

@bot.message_handler(func=lambda message: message.text in ['Строящиеся', 'Готовые'])
def apartments_purpose(message):
    markup = types.ReplyKeyboardMarkup(row_width=2)
    itembtn1 = types.KeyboardButton('Для собственного использования')
    itembtn2 = types.KeyboardButton('Для инвестиций')
    itembtn3 = types.KeyboardButton('Назад')
    markup.add(itembtn1, itembtn2, itembtn3)
    bot.reply_to(message, "Для каких целей нужна недвижимость?", reply_markup=markup)

@bot.message_handler(func=lambda message: message.text in ['Для собственного использования', 'Для инвестиций'])
def apartments_location(message):
    markup = types.ReplyKeyboardMarkup(row_width=2)
    itembtn1 = types.KeyboardButton('Ленинградская область')
    itembtn2 = types.KeyboardButton('Санкт-Петербург')
    itembtn3 = types.KeyboardButton('Назад')
    markup.add(itembtn1, itembtn2, itembtn3)
    bot.reply_to(message, "Желаемое месторасположение", reply_markup=markup)


@bot.message_handler(func=lambda message: message.text == 'Назад')
def go_back(message):
    markup = types.ReplyKeyboardMarkup(row_width=2)
    itembtn1 = types.KeyboardButton('Покупка')
    itembtn2 = types.KeyboardButton('Продажа')
    itembtn3 = types.KeyboardButton('Сдать в аренду')
    itembtn4 = types.KeyboardButton('Снять в аренду')
    itembtn5 = types.KeyboardButton('Управление недвижимостью')
    itembtn6 = types.KeyboardButton('Юридическое сопровождение сделки')
    markup.add(itembtn1, itembtn2, itembtn3, itembtn4, itembtn5, itembtn6)
    bot.reply_to(message, "Здравствуйте! Какой вопрос о недвижимости вас интересует?", reply_markup=markup)

@bot.message_handler(func=lambda message: message.text == 'Снять в аренду')
def rent(message):
    func.rent(message, bot)

@bot.message_handler(func=lambda message: message.text in ['Квартира для аренды', 'Дом для аренды', 'Апартаменты для аренды', 'Коммерческая недвижимость для аренды'])
def specific_rent(message):
    func.specific_rent(message, bot)

@bot.message_handler(func=lambda message: message.text == 'Санкт-Петербург')
def spb_districts_rent(message):
    func.spb_districts_rent(message, bot)

@bot.message_handler(func=lambda message: message.text in ['Ленинградская область', 'Адмиралтейский район для аренды', 'Василеостровский район для аренды', 'Выборгский район для аренды', 'Калининский район для аренды', 'Кировский район для аренды', 'Колпинский район для аренды', 'Красногвардейский район для аренды', 'Красносельский район для аренды', 'Кронштадтский район для аренды', 'Курортный район для аренды', 'Московский район для аренды', 'Невский район для аренды', 'Петроградский район для аренды', 'Петродворцовый район для аренды', 'Приморский район для аренды', 'Пушкинский район для аренды', 'Фрунзенский район для аренды', 'Центральный район для аренды'])
def request_accepted_rent(message):
    func.request_accepted_rent(message, bot)

# СДАТЬ В АРЕНДУ

@bot.message_handler(func=lambda message: message.text == 'Сдать в аренду')
def send_rent(message):
    markup = types.ReplyKeyboardMarkup(row_width=2)
    itembtn_rent1 = types.KeyboardButton('Квартира для аренды')
    itembtn_rent2 = types.KeyboardButton('Дом для аренды')
    itembtn_rent3 = types.KeyboardButton('Апартаменты для аренды')
    itembtn_rent4 = types.KeyboardButton('Коммерческая недвижимость для аренды')
    itembtn_rent5 = types.KeyboardButton('Назад')
    markup.add(itembtn_rent1, itembtn_rent2, itembtn_rent3, itembtn_rent4, itembtn_rent5)
    bot.reply_to(message, "Выберите тип недвижимости для аренды", reply_markup=markup)


# Продажа

@bot.message_handler(func=lambda message: message.text == 'Продажа')
def sale(message):
    markup = types.ReplyKeyboardMarkup(row_width=2)
    itembtn1 = types.KeyboardButton('Квартира для продажи')
    itembtn2 = types.KeyboardButton('Дом для продажи')
    itembtn3 = types.KeyboardButton('Земельный участок для продажи')
    itembtn4 = types.KeyboardButton('Апартаменты для продажи')
    itembtn5 = types.KeyboardButton('Коммерческая недвижимость для продажи')
    itembtn6 = types.KeyboardButton('Назад')
    markup.add(itembtn1, itembtn2, itembtn3, itembtn4, itembtn5, itembtn6)
    bot.reply_to(message, "Отлично, выберите какой тип продажи вас интересует?", reply_markup=markup)

@bot.message_handler(func=lambda message: message.text == 'Квартира для продажи')
def specific_sale_apartment(message):
    markup = types.ReplyKeyboardMarkup(row_width=2)
    itembtn1 = types.KeyboardButton('Новостройка для продажи')
    itembtn2 = types.KeyboardButton('Вторичное жилье для продажи')
    itembtn3 = types.KeyboardButton('Назад')
    markup.add(itembtn1, itembtn2, itembtn3)
    bot.reply_to(message, "Выберите тип недвижимости", reply_markup=markup)

@bot.message_handler(func=lambda message: message.text == 'Дом для продажи')
def specific_sale_house(message):
    markup = types.ReplyKeyboardMarkup(row_width=2)
    itembtn1 = types.KeyboardButton('Жилой дом для продажи')
    itembtn2 = types.KeyboardButton('Недостроенный дом для продажи')
    itembtn3 = types.KeyboardButton('Назад')
    markup.add(itembtn1, itembtn2, itembtn3)
    bot.reply_to(message, "Выберите тип недвижимости", reply_markup=markup)

@bot.message_handler(func=lambda message: message.text == 'Земельный участок для продажи')
def specific_sale_land(message):
    markup = types.ReplyKeyboardMarkup(row_width=2)
    itembtn1 = types.KeyboardButton('Ленинградская область')
    itembtn2 = types.KeyboardButton('Санкт-Петербург')
    itembtn3 = types.KeyboardButton('Назад')
    markup.add(itembtn1, itembtn2, itembtn3)
    bot.reply_to(message, "Желаемое месторасположение", reply_markup=markup)

@bot.message_handler(func=lambda message: message.text == 'Апартаменты для продажи')
def specific_sale_apartments(message):
    markup = types.ReplyKeyboardMarkup(row_width=2)
    itembtn1 = types.KeyboardButton('Строящиеся для продажи')
    itembtn2 = types.KeyboardButton('Готовые для продажи')
    itembtn3 = types.KeyboardButton('Назад')
    markup.add(itembtn1, itembtn2, itembtn3)
    bot.reply_to(message, "Выберите тип недвижимости", reply_markup=markup)

@bot.message_handler(func=lambda message: message.text == 'Коммерческая недвижимость для продажи')
def specific_sale_commercial(message):
    markup = types.ReplyKeyboardMarkup(row_width=2)
    itembtn1 = types.KeyboardButton('Строящаяся для продажи')
    itembtn2 = types.KeyboardButton('Готовая для продажи')
    itembtn3 = types.KeyboardButton('Назад')
    markup.add(itembtn1, itembtn2, itembtn3)
    bot.reply_to(message, "Выберите тип недвижимости", reply_markup=markup)

@bot.message_handler(func=lambda message: message.text in ['Новостройка для продажи', 'Вторичное жилье для продажи', 'Жилой дом для продажи', 'Недостроенный дом для продажи', 'Строящиеся для продажи', 'Готовые для продажи', 'Строящаяся для продажи', 'Готовая для продажи'])
def sale_location(message):
    markup = types.ReplyKeyboardMarkup(row_width=2)
    itembtn1 = types.KeyboardButton('Ленинградская область')
    itembtn2 = types.KeyboardButton('Санкт-Петербург')
    itembtn3 = types.KeyboardButton('Назад')
    markup.add(itembtn1, itembtn2, itembtn3)
    bot.reply_to(message, "Желаемое месторасположение", reply_markup=markup)

@bot.message_handler(func=lambda message: message.text == 'Санкт-Петербург')
def spb_districts(message):
    markup = types.ReplyKeyboardMarkup(row_width=2)
    itembtn1 = types.KeyboardButton('Адмиралтейский район')
    itembtn2 = types.KeyboardButton('Василеостровский район')
    itembtn3 = types.KeyboardButton('Выборгский район')
    itembtn4 = types.KeyboardButton('Калининский район')
    itembtn5 = types.KeyboardButton('Кировский район')
    itembtn6 = types.KeyboardButton('Колпинский район')
    itembtn7 = types.KeyboardButton('Красногвардейский район')
    itembtn8 = types.KeyboardButton('Красносельский район')
    itembtn9 = types.KeyboardButton('Кронштадтский район')
    itembtn10 = types.KeyboardButton('Курортный район')
    itembtn11 = types.KeyboardButton('Московский район')
    itembtn12 = types.KeyboardButton('Невский район')
    itembtn13 = types.KeyboardButton('Петроградский район')
    itembtn14 = types.KeyboardButton('Петродворцовый район')
    itembtn15 = types.KeyboardButton('Приморский район')
    itembtn16 = types.KeyboardButton('Пушкинский район')
    itembtn17 = types.KeyboardButton('Фрунзенский район')
    itembtn18 = types.KeyboardButton('Центральный район')
    itembtn19 = types.KeyboardButton('Назад')
    markup.add(itembtn1, itembtn2, itembtn3, itembtn4, itembtn5, itembtn6, itembtn7, itembtn8, itembtn9, itembtn10, itembtn11, itembtn12, itembtn13, itembtn14, itembtn15, itembtn16, itembtn17, itembtn18, itembtn19)
    bot.reply_to(message, "Выберите район", reply_markup=markup)

@bot.message_handler(func=lambda message: message.text in ['Ленинградская область', 'Адмиралтейский район', 'Василеостровский район', 'Выборгский район', 'Калининский район', 'Кировский район', 'Колпинский район', 'Красногвардейский район', 'Красносельский район', 'Кронштадтский район', 'Курортный район', 'Московский район', 'Невский район', 'Петроградский район', 'Петродворцовый район', 'Приморский район', 'Пушкинский район', 'Фрунзенский район', 'Центральный район'])
def request_accepted(message):
    bot.reply_to(message, "Заявка принята!")
    markup = types.ReplyKeyboardMarkup(row_width=2)
    itembtn1 = types.KeyboardButton('Покупка')
    itembtn2 = types.KeyboardButton('Продажа')
    itembtn3 = types.KeyboardButton('Сдать в аренду')
    itembtn4 = types.KeyboardButton('Снять в аренду')
    itembtn5 = types.KeyboardButton('Управление недвижимостью')
    itembtn6 = types.KeyboardButton('Юридическое сопровождение сделки')
    markup.add(itembtn1, itembtn2, itembtn3, itembtn4, itembtn5, itembtn6)
    bot.reply_to(message, "Здравствуйте Какой вопрос о недвижимости вас интересует?", reply_markup=markup)

# Управление недвижимостью

@bot.message_handler(func=lambda message: message.text == 'Управление недвижимостью')
def send_property_management(message):
    markup = types.ReplyKeyboardMarkup(row_width=2)
    itembtn_pm1 = types.KeyboardButton('✅ Жилая недвижимость')
    itembtn_pm2 = types.KeyboardButton('✅ Коммерческая недвижимость')
    itembtn_pm3 = types.KeyboardButton('Назад')
    markup.add(itembtn_pm1, itembtn_pm2, itembtn_pm3)
    bot.reply_to(message, "Выберите тип недвижимости для управления", reply_markup=markup)

@bot.message_handler(func=lambda message: message.text == '✅ Жилая недвижимость')
def send_residential_property(message):
    markup = types.ReplyKeyboardMarkup(row_width=2)
    itembtn_rp1 = types.KeyboardButton('Ленинградская область')
    itembtn_rp2 = types.KeyboardButton('Санкт-Петербург')
    itembtn_rp3 = types.KeyboardButton('Назад')
    markup.add(itembtn_rp1, itembtn_rp2, itembtn_rp3)
    bot.reply_to(message, "Выберите регион", reply_markup=markup)

@bot.message_handler(func=lambda message: message.text == '✅ Коммерческая недвижимость')
def send_commercial_property(message):
    markup = types.ReplyKeyboardMarkup(row_width=2)
    itembtn_cp1 = types.KeyboardButton('Ленинградская область')
    itembtn_cp2 = types.KeyboardButton('Санкт-Петербург')
    itembtn_cp3 = types.KeyboardButton('Назад')
    markup.add(itembtn_cp1, itembtn_cp2, itembtn_cp3)
    bot.reply_to(message, "Выберите регион", reply_markup=markup)

@bot.message_handler(func=lambda message: message.text == 'Санкт-Петербург')
def spb_districts(message):
    markup = types.ReplyKeyboardMarkup(row_width=2)
    itembtn_district1 = types.KeyboardButton('🏢 Адмиралтейский район')
    itembtn_district2 = types.KeyboardButton('🏢 Василеостровский район')
    itembtn_district3 = types.KeyboardButton('🏢 Выборгский район')
    itembtn_district4 = types.KeyboardButton('🏢 Калининский район')
    itembtn_district5 = types.KeyboardButton('🏢 Кировский район')
    itembtn_district6 = types.KeyboardButton('🏢 Колпинский район')
    itembtn_district7 = types.KeyboardButton('🏢 Красногвардейский район')
    itembtn_district8 = types.KeyboardButton('🏢 Красносельский район')
    itembtn_district9 = types.KeyboardButton('🏢 Кронштадтский район')
    itembtn_district10 = types.KeyboardButton('🏢 Курортный район')
    itembtn_district11 = types.KeyboardButton('🏢 Московский район')
    itembtn_district12 = types.KeyboardButton('🏢 Невский район')
    itembtn_district13 = types.KeyboardButton('🏢 Петроградский район')
    itembtn_district14 = types.KeyboardButton('🏢 Петродворцовый район')
    itembtn_district15 = types.KeyboardButton('🏢 Приморский район')
    itembtn_district16 = types.KeyboardButton('🏢 Пушкинский район')
    itembtn_district17 = types.KeyboardButton('🏢 Фрунзенский район')
    itembtn_district18 = types.KeyboardButton('🏢 Центральный район')
    itembtn_district19 = types.KeyboardButton('Назад')
    markup.add(itembtn_district1, itembtn_district2, itembtn_district3, itembtn_district4, itembtn_district5, itembtn_district6, itembtn_district7, itembtn_district8, itembtn_district9, itembtn_district10, itembtn_district11, itembtn_district12, itembtn_district13, itembtn_district14, itembtn_district15, itembtn_district16, itembtn_district17, itembtn_district18, itembtn_district19)
    bot.reply_to(message, "Выберите район", reply_markup=markup)

@bot.message_handler(func=lambda message: True)
def request_accepted(message):
    bot.reply_to(message, "Заявка принята!")




if __name__ == "__func__":
    func()



bot.polling()

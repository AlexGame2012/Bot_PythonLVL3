from telebot import TeleBot, types
from config import token

bot = TeleBot(token)

def create_main_keyboard():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    btn1 = types.KeyboardButton('ℹ️ Информация')
    btn2 = types.KeyboardButton('🌐 Наш сайт')
    btn3 = types.KeyboardButton('💼 Услуги')
    btn4 = types.KeyboardButton('📞 Контакты')
    markup.add(btn1, btn2, btn3, btn4)
    return markup

@bot.message_handler(commands=['start'])
def send_welcome(message):
    welcome_text = """
✨ *Добро пожаловать в AlexStudio Code!* ✨

Мы рады приветствовать вас в нашем боте. 
Здесь вы можете узнать о наших услугах и возможностях.

Выберите нужный вариант из меню ниже 👇
    """
    
    bot.send_message(message.chat.id, welcome_text, 
                     parse_mode='Markdown', 
                     reply_markup=create_main_keyboard())
    
@bot.message_handler(commands=['info'])
def information(message):
    info_text = """
📊 *Информация о компании*

Компания AlexStudioCode была основана в октябре 2024 года и на сегодняшний день — это 
небольшая, но целеустремленная команда специалистов, специализирующихся на создании веб-сайтов,
игр, телеграм-ботов и мобильных приложений.

Несмотря на небольшой масштаб, мы стремимся к высоким стандартам и индивидуальному подходу 
к каждому клиенту. Наша миссия — разрабатывать качественные и современные 
цифровые решения, которые помогают нашим заказчикам развивать бизнес и реализовывать их идеи.
    """
    
    bot.send_message(message.chat.id, info_text, parse_mode='Markdown')

@bot.message_handler(func=lambda message: True)
def handle_text(message):
    if message.text == 'ℹ️ Информация':
        information(message)
    elif message.text == '🌐 Наш сайт':
        bot.send_message(message.chat.id, "🌐 *Наш сайт:* https://alexstudiocode.ru", parse_mode='Markdown')
    elif message.text == '💼 Услуги':
        services_text = """
🛠 *Наши услуги:*

• 🌐 Создание веб-сайтов
• 🎮 Разработка игр
• 🤖 Telegram-боты
• 📱 Мобильные приложения

Хотите узнать подробности? Обращайтесь!
        """
        bot.send_message(message.chat.id, services_text, parse_mode='Markdown')
    elif message.text == '📞 Контакты':
        contact_text = """
📞 *Свяжитесь с нами:*

• 📧 Email: info@alexstudiocode.ru
• 🌐 Сайт: https://alexstudiocode.ru
• 💬 Telegram: @alexstudiocode

Мы всегда рады новым проектам и сотрудничеству!
        """
        bot.send_message(message.chat.id, contact_text, parse_mode='Markdown')
    else:
        bot.send_message(message.chat.id, "🤔 *Не понимаю вашего запроса*\nИспользуйте кнопки меню для навигации", 
                        parse_mode='Markdown', reply_markup=create_main_keyboard())

if __name__ == '__main__':
    print("🤖 Бот запущен и готов к работе...")
    print("⚡ AlexStudio Code 2025")
    bot.infinity_polling()
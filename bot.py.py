import telebot
import time

BOT_TOKEN = "8632262692:AAEw4opvu-r5zow6yr2W051YoST9KI5f4qo"
ADMIN_ID = 5788056369

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])

def start_message(message):

    bot.send_message(
        message.chat.id,
        "👋 Добро пожаловать!\n\n"
        "📨 Напишите любое сообщение."
    )

    bot.send_message(
        message.chat.id,
        "☰ Для получения помощи используйте команду /help"
    )

    if message.chat.id != ADMIN_ID:

        user_name = message.from_user.full_name

        if message.from_user.username:
            username = "@" + message.from_user.username
        else:
            username = "нет username"

        bot.send_message(
            ADMIN_ID,
            f"🚀 Новый пользователь запустил бота\n\n"
            f"👤 {user_name}\n"
            f"🔹 {username}\n"
            f"🆔 {message.from_user.id}"
        )

@bot.message_handler(commands=['command1'])
def help_command(message):

    bot.send_message(
        message.chat.id,
        "📚 Помощь\n\n"
        "🤖 Я могу ответить на вопросы:\n\n"
        "• Кто сделал этого бота?\n"
        "• Куда отправляются мои сообщения?\n"
        "• Сколько сообщений можно отправлять?\n\n"
        "⚠️ На остальные вопросы бот не отвечает."
    )


@bot.message_handler(content_types=['text'])
def handle_text(message):

    text = message.text.lower()

    if any(word in text for word in [
        "на какие вопросы отвечает бот",
        "что умеет бот",
        "какие вопросы можно задавать",
        "на что отвечает бот",
        "какие команды есть"
    ]):

        bot.send_message(
            message.chat.id,
            "🤖 Я могу ответить на следующие вопросы:\n\n"
            "• Кто сделал этого бота?\n"
            "• Куда отправляются мои сообщения?\n"
            "• Сколько сообщений можно отправлять?\n\n"
            "⚠️ На остальные вопросы бот не отвечает."
        )
        return

    if any(word in text for word in [
        "кто сделал",
        "кто создал",
        "кто автор",
        "кто разработчик",
        "кем создан бот"
    ]):

        bot.send_message(
            message.chat.id,
            "👨‍💻 Бот был создан пользователем @Dawood30"
        )
        
        
        return

    if any(word in text for word in [
        "куда отправляются мои сообщения",
        "куда уходят мои сообщения",
        "кому отправляются мои сообщения",
        "кому приходят мои сообщения",
        "куда попадают сообщения",
        "кто получает мои сообщения",
        "кто читает мои сообщения",
        "кому пишет бот",
        "кому отправляет бот",
        "кому приходят сообщения",
        "куда идут сообщения",
        "куда деваются сообщения",
        "куда отправляется сообщение"
    ]):

        bot.send_message(
            message.chat.id,
            "📨 Ваши сообщения отправляются создателю этого бота."
        )
        return

    if any(word in text for word in [
        "сколько сообщений",
        "лимит сообщений",
        "ограничение сообщений",
        "можно отправлять много сообщений",
        "есть лимит сообщений",
        "есть ограничения"
    ]):

        bot.send_message(
            message.chat.id,
            "📨 Ограничений на количество сообщений нет."
        )
        return

    if message.chat.id == ADMIN_ID:
        return

    user_name = message.from_user.full_name

    if message.from_user.username:
        username = "@" + message.from_user.username
    else:
        username = "нет username"

    bot.send_message(
        ADMIN_ID,
        f"👤 {user_name}\n"
        f"🔹 {username}\n"
        f"🆔 {message.from_user.id}\n\n"
        f"💬 {message.text}"
    )

    bot.send_message(
        message.chat.id,
        "📨 Сообщение успешно отправлено!"
    )


@bot.message_handler(content_types=['photo'])
def handle_photo(message):

    bot.send_photo(
        ADMIN_ID,
        message.photo[-1].file_id,
        caption=f"📷 Фото от {message.from_user.full_name}"
    )

    bot.send_message(
        message.chat.id,
        "📨 Фото успешно отправлено!"
    )


@bot.message_handler(content_types=['video'])
def handle_video(message):

    bot.send_video(
        ADMIN_ID,
        message.video.file_id,
        caption=f"🎥 Видео от {message.from_user.full_name}"
    )

    bot.send_message(
        message.chat.id,
        "📨 Видео успешно отправлено!"
    )


@bot.message_handler(content_types=['animation'])
def handle_gif(message):

    bot.send_animation(
        ADMIN_ID,
        message.animation.file_id,
        caption=f"🎞 GIF от {message.from_user.full_name}"
    )

    bot.send_message(
        message.chat.id,
        "📨 GIF успешно отправлен!"
    )


@bot.message_handler(content_types=['sticker'])
def handle_sticker(message):

    bot.send_sticker(
        ADMIN_ID,
        message.sticker.file_id
    )

    bot.send_message(
        ADMIN_ID,
        f"😄 Стикер от {message.from_user.full_name}"
    )

    bot.send_message(
        message.chat.id,
        "📨 Стикер успешно отправлен!"
    )


while True:
    try:
        print("Бот запущен")
        bot.infinity_polling(
            timeout=60,
            long_polling_timeout=60
        )

    except Exception as e:
        print("Ошибка:", e)
        time.sleep(5)
import telebot

bot = telebot.TeleBot('5459496090:AAEip2vap6ReUchtK5WBa0amK0NLcQ1eXqA')
val = id(object)


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Приветствуем Вас!\nНаправьте информацию, которую хотели бы сообщить.'
                                      '\n----------------------------\n'
                                      'Вітаємо Вас!\nНаправте інформацію, '
                                      'яку хотіли б повідомити.', parse_mode='html')
@bot.message_handler(content_types=['text'])
def get_user_text(message):
    mess = f'информация от <b>{message.from_user.username}: </b>{message.text}'
    bot.send_message(5636064377,mess,parse_mode='html')
@bot.message_handler(content_types=['photo'])
def photo(message):
    mess1 = f'фотография от <b>{message.from_user.username}: </b>'
    bot.send_message(5636064377, mess1, parse_mode='html')
    bot.send_photo(5636064377,message.photo[0].file_id)

@bot.message_handler(content_types=['video'])
def video(message):
    mess2 = f'видео от <b>{message.from_user.username}: </b>'
    bot.send_message(5636064377, mess2, parse_mode='html')
    bot.send_video(5636064377,message.video.file_id)

bot.infinity_polling()


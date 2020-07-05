import telebot

from flask import Flask, request
from telebot import types

import os

import sys
sys.path.append('/')


import alex_style_transfer_class_work



TOKEN = ""
tel_bot = telebot.TeleBot(TOKEN)
server = Flask(__name__)


n = 0
zap = False
@tel_bot.message_handler(content_types=['text'])
def start(message):
    if message.text == '/start':
        tel_bot.send_message(message.from_user.id, "Привет! Это бот, которому можно отправить две фотографии и получить в ответ фото с перенесенным стилем. Пришлите, пожалуйста, изображение, с которого нужно перенести стиль")
        tel_bot.register_next_step_handler(message, get_style_image)
    else:
        tel_bot.send_message(message.from_user.id, 'Напиши /start')
        
 
def get_style_image(message): #
    global style_image
    global src_style
    if message.content_type!= 'photo':
        tel_bot.send_message(message.chat.id, 'Мне нужно изображение, отправьте, пожалуйста')
        tel_bot.register_next_step_handler(message, get_style_image)
    if message.content_type== 'photo': 
        

        #пытаемся фото сохранить 
        file_info = tel_bot.get_file(message.photo[len(message.photo)-1].file_id)
        style_image = tel_bot.download_file(file_info.file_path)

        src_style='style_image.jpg'
        
        with open(src_style, 'wb') as new_file:
           new_file.write(style_image)
        
        

        tel_bot.send_message(message.from_user.id, 'Спасибо, теперь мне нужно изображение, на которое нужно перенести стиль') 
        tel_bot.register_next_step_handler(message, get_content_image)
 
def get_content_image(message):
    global content_image
    global src_content
    global output
    if message.content_type!= 'photo':
        tel_bot.send_message(message.chat.id, 'Мне нужно изображение, отправьте, пожалуйста')
    if message.content_type== 'photo':     
       
        
        file_info = tel_bot.get_file(message.photo[len(message.photo)-1].file_id)
        content_image = tel_bot.download_file(file_info.file_path)

        src_content='content_image.jpg'
        
        with open(src_content, 'wb') as new_file:
           new_file.write(content_image)
         #пытаемся фото сохранить 
        

        tel_bot.send_message(message.chat.id,'Спасибо, начинаю обработку')
        object_style_transfer = alex_style_transfer_class_work.StyleTransfer(style_image_path=src_style,
                                                    content_image_path=src_content) 
        output =object_style_transfer.transfer_style(out_image_path= "out_image.png") 
        photo = open('out_image.png', 'rb')
        tel_bot.send_photo(message.from_user.id, photo)
       

@server.route('/' + TOKEN, methods=['POST'])
def getMessage():
    tel_bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
    return "!", 200


@server.route("/")
def webhook():
    tel_bot.remove_webhook()
    tel_bot.set_webhook(url='https://peaceful-saguaro-86061.herokuapp.com/' + TOKEN)
    return "!", 200


if __name__ == "__main__":
    server.run(host="0.0.0.0", port=int(os.environ.get('PORT', 5000)))
	
#tel_bot.polling()







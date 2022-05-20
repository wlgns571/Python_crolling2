# pip install python-telegram-bot
TOKEN = '5394746204:AAFxd2IpP7l1wW5WI1-HavZnTPtnRMWZarE'

from telegram.ext import Updater
from telegram.ext import MessageHandler, Filters, CommandHandler

updater = Updater(token=TOKEN, use_context=True)

def fn_echo(update, context):
    user_id = update.effective_chat.id
    user_text = update.message.text
    context.bot.send_message(chat_id=user_id, text='hi')

import os
import datetime
import shutil
def fn_write_diary(msg):
    now = datetime.datetime.now()
    formattedDate = now.strftime("%Y%m%d_diary.txt")
    f = open(formattedDate,'a')
    from_ = formattedDate
    to_ = './diary'
    if not os.path.exists(to_):
        os.makedirs(to_)
    shutil.move(from_, to_)
    f.write(msg + '\n')

def fn_diary(update, context):
    user_id = update.effective_chat.id
    user_text = update.message.text
    print(user_text)
    msg = user_text.replace('/diary','')
    fn_write_diary(msg)
    context.bot.send_message(chat_id=user_id, text=msg + ' 저장 했습니다.')
# 기본 메세지
echo_handler = MessageHandler(Filters.text & (~Filters.command), fn_echo)
updater.dispatcher.add_handler(echo_handler)
# /diary <-- 텍스트 있을시 실행
updater.dispatcher.add_handler(CommandHandler('diary', fn_diary))

def save_photo(update, context):
    dir = './'
    imgNm = 'save_png.png'
    file_path = os.path.join(dir, imgNm)
    bot = context.bot
    photo = bot.getFile(update.message.photo[-1].file_id)
    photo.download(file_path)
    update.message.reply_text('photo saved')

photo_handler = MessageHandler(Filters.photo, save_photo)
updater.dispatcher.add_handler(photo_handler)
updater.start_polling()
updater.idle()

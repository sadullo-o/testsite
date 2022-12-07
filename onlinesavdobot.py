from telegram.ext import *
from telegram import *
import urllib.request

import requests

OLINGAN_MALUMOT = []

def start(update, context):
    r = requests.get('http://127.0.0.1:8000/api/v1/tovarlar')
    data = r.json()
    for i in data:
        urllib.request.urlretrieve(i["img"], "image.jpg")

        tovarlar = f'''Tovar kodi: <b>{i["id"]}</b>
Tovar nomi: <b>{i["title"]}</b>
Tovar haqida: <b>{i["about"]}</b>
Tovar narxi: <b>{i["narx"]}</b>\n\n\n'''
        context.bot.send_photo(update.message.chat_id, open('image.jpg', 'rb'), parse_mode='HTML', caption=tovarlar)
        # update.message.reply_html(tovarlar)


    return 1

def tovars(update, context):
    OLINGAN_MALUMOT.append(update.message.text)
    update.message.reply_html('Telefon raqamingizni kiriting')
    return 2

def savat(update, context):
    olingan_mal = OLINGAN_MALUMOT[0]
    tel = update.message.text
    r = requests.get('http://127.0.0.1:8000/api/v1/tovarlar')
    data = r.json()
    m = []
    for i in data:
        if i['id'] == int(olingan_mal):
            m.append(i)

    data = {
        'username': update.message.from_user.username,
        'phone': tel,
        'tovar': m[0]['title'],
        'summa': f'{m[0]["narx"]} sum'
    }

    r = requests.post('http://127.0.0.1:8000/api/v1/savat', data)
    update.message.reply_html('Tez orada admin siz bilan boglanadi')


def main():
    updater = Updater('5878325250:AAEn-07bIq66AIHQQyg0TagpcSkGbEZoqqQ', use_context=True)

    dispatcher = updater.dispatcher

    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],
        states={
            1: [MessageHandler(Filters.text, tovars)],
            2: [MessageHandler(Filters.text, savat)]
        },
        fallbacks=[CommandHandler('start', start)]
    )

    dispatcher.add_handler(conv_handler)

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()



















#get
# r = requests.get('http://127.0.0.1:8000/api/v1/tovarlar')
#
# data = r.json()
#
# print(data[0])


#post
# data = {
#     'username': 'ali',
#     'phone': '97723333',
#     'tovar': 'Cola',
#     'summa': '11000 sum'
# }
#
# r = requests.post('http://127.0.0.1:8000/api/v1/savat', data)
#
# print(r)
# 설치해야할 라이브러리
# pip install requests Beautifulsoup4 lxml python-telegram-bot

import telegram
from telegram.ext import Updater, CommandHandler
import logging

import requests
from bs4 import BeautifulSoup

TELEGRAM_TOKEN = "텔레그램 토큰을 입력하세요"
CHAT_ID = "채팅 아이디를 입력하세요"


# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.DEBUG)
logger = logging.getLogger(__name__)

exchange_lists = {}

def get_exchange_info():
    url = "https://finance.naver.com/marketindex/exchangeList.nhn"
    r = requests.get(url)
    bs = BeautifulSoup(r.content, "lxml")
    trs = bs.select("table.tbl_exchange > tbody > tr") # list 자료형을 리턴함
    for tr in trs:
        tds = tr.select("td")
        if len(tds) == 7:
            name = tds[0].text.strip() # 미국 USD
            value = float(tds[1].text.strip().replace(",", "")) # 1,120
            print(name, value)
            exchange_lists[name] = value

def get_money(update, context, args):
    # ['미국', '영국']
    message = ""
    for a in args:
        for key, value in exchange_lists.items():
            if str(key).find(a) >= 0:
                message += '{} {}'.format(key, value)
                message += "\n"
    
    if message != "":
        bot.send_message(CHAT_ID, message)
    else:
        bot.send_message(CHAT_ID, "요청한 데이터가 없습니다.")

get_exchange_info()
print(exchange_lists)

bot = telegram.Bot(TELEGRAM_TOKEN)
updater = Updater(TELEGRAM_TOKEN)
updater.stop()

updater.dispatcher.add_handler(CommandHandler("m", get_money, pass_args=True))
updater.start_polling()
updater.idle()

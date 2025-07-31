import requests
# import telegram
from secrets import *



URL = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/"

USER_IDS = [
    TELEGRAM_MIKE_ID,
    TELEGRAM_LUKE_ID,
]

#r = requests.get(URL + 'getUpdates') #, params={'getUpdates'})
# r = requests.get(URL + 'sendMessage', params={"chat_id": USER_IDS[0], 'text': "multi\nline"})

def send_msg(msg: str):
    for u in USER_IDS:
        r = requests.get(URL + "sendMessage", params={
            'chat_id': u,
            'text': msg
        })
        print(r.json())


# if __name__ == "__main__":

#     bot = telegram.Bot(token=TOKEN)

#     bot.
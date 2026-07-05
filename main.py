import requests
import time
from datetime import datetime
import pytz

import os
TOKEN = os.environ["8560032476:AAGabGXhK-wRmWfMk2IkidYkXaQ_2zd6Rbs
"]
CHAT_ID = "@yscountdown_2026"

URL = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

count1 = 286
count2 = 258

def send():
    text = f"""🌸 Countdown :

~~AMA+ : D-{count1}✨
~~fall semester : D-{count2}✨
"""
    requests.post(URL, data={"chat_id": CHAT_ID, "text": text})

print("bot started")

while True:
    tz = pytz.timezone("Asia/Tehran")
    now = datetime.now(tz)

    if now.hour == 9 and now.minute == 0:
        send()
        time.sleep(60)

    time.sleep(20)

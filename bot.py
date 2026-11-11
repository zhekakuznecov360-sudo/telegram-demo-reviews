
import os
import time
import random
import requests

TOKEN = os.environ["BOT_TOKEN"]
CHANNEL = os.environ["CHANNEL_ID"]

messages = [
    "💎 Обмен USDT — демонстрационный пример. Быстро и удобно!",
    "🔥 Пример уведомления: заявка на обмен криптовалюты обработана.",
    "✅ Демо-сообщение: операция покупки успешно завершена.",
    "🚀 Пример автоматического уведомления об обмене TON.",
    "💰 Демо-уведомление: заявка на покупку принята."
]

def send_demo():
    name = f"Демо-профиль №{random.randint(100, 9999)}"
    message = random.choice(messages)

    text = (
        "↪️ ДЕМО-ПУБЛИКАЦИЯ\n"
        f"Отправитель: {name}\n\n"
        f"{message}\n\n"
        "ℹ️ Это автоматически созданный пример, "
        "не реальный отзыв клиента."
    )

    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    response = requests.post(
        url,
        json={"chat_id": CHANNEL, "text": text},
        timeout=20
    )
    response.raise_for_status()

while True:
    try:
        time.sleep(1800)
        send_demo()
    except Exception as error:
        print("Ошибка:", error)
        time.sleep(60)
      

import asyncio
from telegram.ext import Application, MessageHandler, filters
import requests

# Your hardcoded values
TELEGRAM_BOT_TOKEN = "7738310811:AAGg9hP7geVPiL4Mkv-PWsDEv-UzzpTFnkY"
DISCORD_WEBHOOK_URL = "https://discord.com/api/webhooks/1365540345340887090/vTaZjUxIoW8b5m32iJYyaXDpYXyLBUOz-wU0i3JvHXA92NrYCDSGHMKjkP45Rjxf9dYt"
MY_ADMIN_USER_ID = 2108081519  # your real Telegram User ID

async def forward_deal_messages(update, context):
    message = update.message

    if message and message.from_user and message.from_user.id == MY_ADMIN_USER_ID:
        if message.text and "View on Steam" in message.text:
            data = {
                "content": message.text
            }
            response = requests.post(DISCORD_WEBHOOK_URL, json=data)
            print(f"✅ Forwarded your deal to Discord! Status: {response.status_code}")
        else:
            print("Ignored message (not a Steam deal).")
    else:
        print("Ignored: not admin or not a deal.")

def main():
    app = Application.builder().token(TELEGRAM_BOT_TOKEN).build()

    app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), forward_deal_messages))

    print("🚀 Bot is running... ONLY forwarding Steam deals triggered by admin (/deals).")
    app.run_polling()

if __name__ == '__main__':
    main()



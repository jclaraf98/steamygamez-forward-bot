import asyncio
from telegram.ext import Application, MessageHandler, filters
import requests
import time

# Hardcoded values
TELEGRAM_BOT_TOKEN = "7738310811:AAGg9hP7geVPiL4Mkv-PWsDEv-UzzpTFnkY"
DISCORD_WEBHOOK_URL = "https://discord.com/api/webhooks/1365540345340887090/vTaZjUxIoW8b5m32iJYyaXDpYXyLBUOz-wU0i3JvHXA92NrYCDSGHMKjkP45Rjxf9dYt"
MY_ADMIN_USER_ID = 2108081519  # Your real Telegram User ID

async def forward_deal_messages(update, context):
    message = update.message

    if message and message.from_user and message.from_user.id == MY_ADMIN_USER_ID:
        if message.text and "View on Steam" in message.text:
            data = {
                "content": message.text
            }
            try:
                response = requests.post(DISCORD_WEBHOOK_URL, json=data)
                print(f"✅ Forwarded to Discord! Status: {response.status_code}")
                time.sleep(0.8)  # Small delay to respect Discord's limits
            except Exception as e:
                print(f"❌ Error sending to Discord: {e}")
        else:
            print("Ignored: Not a Steam deal.")
    else:
        print("Ignored: Not admin or wrong message.")

def main():
    app = Application.builder().token(TELEGRAM_BOT_TOKEN).build()

    app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), forward_deal_messages))

    print("🚀 Bot is running... ONLY forwarding Steam deals triggered by admin (/deals).")
    app.run_polling()

if __name__ == '__main__':
    main()

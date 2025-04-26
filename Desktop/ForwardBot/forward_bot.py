from telegram.ext import Application, CallbackQueryHandler
import requests

# Your credentials (HARDCODED VERSION)
TELEGRAM_BOT_TOKEN = "7738310811:AAGg9hP7geVPiL4Mkv-PWsDEv-UzzpTFnkY"
DISCORD_WEBHOOK_URL = "https://discord.com/api/webhooks/1365540345340887090/vTaZjUxIoW8b5m32iJYyaXDpYXyLBUOz-wU0i3JvHXA92NrYCDSGHMKjkP45Rjxf9dYt"
MY_BOT_USER_ID = 8197133639  # ← your bot ID

async def forward_to_discord_from_callback(update, context):
    query = update.callback_query
    if query and query.from_user and query.from_user.id == MY_BOT_USER_ID:
        callback_data = query.data
        if callback_data:
            data = {
                "content": callback_data
            }
            response = requests.post(DISCORD_WEBHOOK_URL, json=data)
            print(f"✅ Forwarded CALLBACK to Discord: {response.status_code}")
        await query.answer()

def main():
    app = Application.builder().token(TELEGRAM_BOT_TOKEN).build()

    app.add_handler(CallbackQueryHandler(forward_to_discord_from_callback))

    print("🚀 Bot is running... ONLY listening for button clicks (callback queries).")
    app.run_polling()

if __name__ == '__main__':
    main()




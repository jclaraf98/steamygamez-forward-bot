from telegram.ext import Application, MessageHandler, filters
import requests

# Your credentials
TELEGRAM_BOT_TOKEN = '7738310811:AAGg9hP7geVPiL4Mkv-PWsDEv-UzzpTFnkY'
DISCORD_WEBHOOK_URL = 'https://discord.com/api/webhooks/1365540345340887090/vTaZjUxIoW8b5m32iJYyaXDpYXyLBUOz-wU0i3JvHXA92NrYCDSGHMKjkP45Rjxf9dYt'

# Your bot's own user ID
MY_BOT_USER_ID = 8197133639  # <- Your bot's Telegram ID (not a username)

async def forward_to_discord(update, context):
    message = update.message

    # Only forward if the message is sent by the bot itself
    if message and message.from_user and message.from_user.id == MY_BOT_USER_ID:
        message_text = message.text

        if message_text:
            data = {
                "content": message_text  # << NO emoji, no extra text
            }
            response = requests.post(DISCORD_WEBHOOK_URL, json=data)
            print(f"Forwarded to Discord: {response.status_code}")
    else:
        print("Ignored user message.")

def main():
    app = Application.builder().token(TELEGRAM_BOT_TOKEN).build()

    app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), forward_to_discord))

    print("Bot is running... Listening for BOT messages only.")
    app.run_polling()

if __name__ == '__main__':
    main()



from telegram.ext import Application, CallbackQueryHandler
import requests

# --- Your bot credentials ---
TELEGRAM_BOT_TOKEN = "7738310811:AAGg9hP7geVPiL4Mkv-PWsDEv-UzzpTFnkY"
MY_BOT_USER_ID = 8197133639
DISCORD_WEBHOOK_URL = "https://discord.com/api/webhooks/1365540345340887090/vTaZjUxIoW8b5m32iJYyaXDpYXyLBUOz-wU0i3JvHXA92NrYCDSGHMKjkP45Rjxf9dYt"

# --- What happens when a button (deal) is clicked ---
async def handle_callback_query(update, context):
    query = update.callback_query

    if query and query.from_user and query.from_user.id == MY_BOT_USER_ID:
        deal_text = query.data  # <- This grabs the callback data (the deal content)

        if deal_text:
            data = {
                "content": f"New Deal clicked: {deal_text}"  # Customize your Discord message
            }
            response = requests.post(DISCORD_WEBHOOK_URL, json=data)
            print(f"✅ Forwarded deal to Discord: {response.status_code}")
        else:
            print("⚠️ Callback query has no data.")
    else:
        print("⚠️ Ignored callback query from another user.")

async def main():
    app = Application.builder().token(TELEGRAM_BOT_TOKEN).build()

    app.add_handler(CallbackQueryHandler(handle_callback_query))

    print("🚀 Bot is running... ONLY listening for button clicks (callback queries).")
    await app.run_polling()

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())



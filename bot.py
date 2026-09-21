import os
import logging

from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    Application,
    CommandHandler,
    CallbackQueryHandler,
    ContextTypes,
)

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)

BOT_TOKEN = os.getenv("BOT_TOKEN")
SUPPORT_USERNAME = os.getenv("SUPPORT_USERNAME", "Vibrantech1")


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [
            InlineKeyboardButton("Services", callback_data="services"),
            InlineKeyboardButton("How It Works", callback_data="how")
        ],
        [
            InlineKeyboardButton("FAQ", callback_data="faq"),
            InlineKeyboardButton("Contact Support", callback_data="support")
        ]
    ]

    text = (
        "Welcome 👋\n\n"
        "Thanks for visiting our Telegram service bot.\n\n"
        "Choose an option below to learn more."
    )

    await update.message.reply_text(
        text,
        reply_markup=InlineKeyboardMarkup(keyboard)
    )


async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == "services":
        text = (
            "Our Services\n\n"
            "• Telegram Ads setup\n"
            "• Telegram Ads campaign support\n"
            "• Ad destination setup\n"
            "• Telegram channel promotion\n"
            "• Campaign troubleshooting\n\n"
            "Contact support if you want to discuss your project."
        )

        keyboard = [
            [InlineKeyboardButton("Contact Support", callback_data="support")],
            [InlineKeyboardButton("⬅️ Back", callback_data="back")]
        ]

    elif query.data == "how":
        text = (
            "How It Works\n\n"
            "1. Tell us about your project.\n"
            "2. We review your requirements.\n"
            "3. We explain the available setup options.\n"
            "4. You can decide whether to proceed.\n\n"
            "Every project is handled according to the applicable "
            "Telegram Ads requirements."
        )

        keyboard = [
            [InlineKeyboardButton("Contact Support", callback_data="support")],
            [InlineKeyboardButton("⬅️ Back", callback_data="back")]
        ]

    elif query.data == "faq":
        text = (
            "Frequently Asked Questions\n\n"
            "Q: Can you help with Telegram Ads?\n"
            "A: Yes. We can discuss setup, campaign configuration "
            "and troubleshooting.\n\n"
            "Q: How long does approval take?\n"
            "A: Review times can vary. Approval is determined by "
            "Telegram's review process.\n\n"
            "Q: Can you guarantee approval?\n"
            "A: No. No legitimate service can guarantee approval."
        )

        keyboard = [
            [InlineKeyboardButton("Contact Support", callback_data="support")],
            [InlineKeyboardButton("⬅️ Back", callback_data="back")]
        ]

    elif query.data == "support":
        text = (
            "Contact Support\n\n"
            "If you have a question about Telegram Ads or your project, "
            "contact our support team."
        )

        keyboard = [
            [
                InlineKeyboardButton(
                    "Message Support",
                    url=f"https://t.me/{SUPPORT_USERNAME}"
                )
            ],
            [InlineKeyboardButton("⬅️ Back", callback_data="back")]
        ]

    else:
        text = (
            "Welcome 👋\n\n"
            "Choose an option below to learn more."
        )

        keyboard = [
            [
                InlineKeyboardButton("Services", callback_data="services"),
                InlineKeyboardButton("How It Works", callback_data="how")
            ],
            [
                InlineKeyboardButton("FAQ", callback_data="faq"),
                InlineKeyboardButton("Contact Support", callback_data="support")
            ]
        ]

    await query.edit_message_text(
        text,
        reply_markup=InlineKeyboardMarkup(keyboard)
    )


def main():
    if not BOT_TOKEN:
        raise ValueError("BOT_TOKEN environment variable is missing.")

    app = Application.builder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button_handler))

    print("Bot is running...")
    app.run_polling()


if __name__ == "__main__":
    main()

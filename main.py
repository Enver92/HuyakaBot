"""
    This is my first telegram bot.
    I still don't know what it's going.
    We'll see...
"""
import telebot

import config

bot = telebot.TeleBot(config.token)

bot.send_message(chat_id=204475218, text="sho ti")

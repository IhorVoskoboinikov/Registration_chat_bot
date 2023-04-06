from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup
from typing import Tuple

from registration import config


def start_kb(error_login: bool = False) -> Tuple[str, ReplyKeyboardMarkup]:
    mess = "Hello, are you ready to register! If yes, click the button 'Start Registration'"
    if error_login:
        mess = "Login already exists, please create another one. Fill out the form from the beginning!"
    start_keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    button = KeyboardButton("Start Registration")
    start_keyboard.add(button)
    return mess, start_keyboard


def go_to_site() -> Tuple[str, InlineKeyboardMarkup]:
    mess = "To go to the site, click 'Go to the site'"
    start_keyboard = InlineKeyboardMarkup(row_width=1)
    button = InlineKeyboardButton(text="Go to the site", url='http://127.0.0.1:8000/login/', callback_data="data")
    start_keyboard.add(button)
    return mess, start_keyboard


def get_contact_kb() -> Tuple[str, ReplyKeyboardMarkup]:
    mess = "To send a phone, click on the 'Send phone' button"
    contact_keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    button = KeyboardButton('Send phone', request_contact=True)
    contact_keyboard.add(button)
    return mess, contact_keyboard


def get_photo_kb() -> Tuple[str, ReplyKeyboardMarkup]:
    mess = "You can add a photo to your profile, to do this, " \
           "send a photo to the chat bot, or click 'Finish'"
    photo_keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    button_finish = KeyboardButton('Finish')
    photo_keyboard.add(button_finish)
    return mess, photo_keyboard


def get_done_to_save_data(message: object) -> Tuple[str, ReplyKeyboardMarkup]:
    mess = f"Check your details\n" \
           f"login - {config.USERS_PROFILE[message.chat.id]['login']}\n" \
           f"password - {config.USERS_PROFILE[message.chat.id]['password']}\n" \
           f"first name - {config.USERS_PROFILE[message.chat.id]['first_name']}\n" \
           f"last name - {config.USERS_PROFILE[message.chat.id]['last_name']}\n" \
           f"user name - {config.USERS_PROFILE[message.chat.id]['user_name']}\n" \
           f"phone - {config.USERS_PROFILE[message.chat.id]['phone']}\n" \
           f"photo - {'Photo is done' if config.USERS_PROFILE[message.chat.id]['photo'] else 'No photo'}\n" \
           f" if everything is correct, click 'Save', if you want to start filling from the beginning, click 'Restart'"
    go_to_site_keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    button_save = KeyboardButton("Save")
    button_restart = KeyboardButton("Restart")
    go_to_site_keyboard.add(button_save, button_restart)
    return mess, go_to_site_keyboard


def return_to_start_kb() -> Tuple[str, ReplyKeyboardMarkup]:
    mess = "An error occurred in the chat bot, try filling out the profile from the beginning."
    start_keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    button = KeyboardButton("Start Registration")
    start_keyboard.add(button)
    return mess, start_keyboard

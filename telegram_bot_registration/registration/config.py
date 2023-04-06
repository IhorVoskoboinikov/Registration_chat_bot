import os
from collections import defaultdict

USERS_PROFILE = defaultdict(dict)

# with open('bot_token.txt', 'r') as f:
#     TELEGRAM_TOKEN = f.read()
TELEGRAM_TOKEN = '6095222446:AAERcOlPxiGc3hxs_sGgVFd9B7XsJ34r7M4'


def assign_users_profile_data(message: object) -> None:
    USERS_PROFILE[message.chat.id]['login'] = None
    USERS_PROFILE[message.chat.id]['password'] = None
    USERS_PROFILE[message.chat.id]['first_name'] = None
    USERS_PROFILE[message.chat.id]['last_name'] = None
    USERS_PROFILE[message.chat.id]['user_name'] = None
    USERS_PROFILE[message.chat.id]['phone'] = None
    USERS_PROFILE[message.chat.id]['photo'] = None



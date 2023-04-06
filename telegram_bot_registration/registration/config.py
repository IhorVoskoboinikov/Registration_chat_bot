from collections import defaultdict

TELEGRAM_TOKEN = '6095222446:AAERcOlPxiGc3hxs_sGgVFd9B7XsJ34r7M4'
USERS_PROFILE = defaultdict(dict)


def assign_users_profile_data(message: object) -> None:
    USERS_PROFILE[message.chat.id]['login'] = None
    USERS_PROFILE[message.chat.id]['password'] = None
    USERS_PROFILE[message.chat.id]['first_name'] = None
    USERS_PROFILE[message.chat.id]['last_name'] = None
    USERS_PROFILE[message.chat.id]['user_name'] = None
    USERS_PROFILE[message.chat.id]['phone'] = None
    USERS_PROFILE[message.chat.id]['photo'] = None

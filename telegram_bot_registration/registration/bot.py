from io import BytesIO
from aiogram import Bot, Dispatcher, types
from aiogram import executor
from django.core.files.uploadedfile import InMemoryUploadedFile
from PIL import Image

from registration import config, bot_db
import keyboards

bot = Bot(token=config.TELEGRAM_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    mess, keyboard = keyboards.start_kb()
    await bot.send_message(message.chat.id, mess, reply_markup=keyboard)


@dp.message_handler(content_types=['text'])
async def handle_text_messages(message):
    try:
        if message.text == 'Start Registration':
            markup = types.ReplyKeyboardRemove()
            config.assign_users_profile_data(message)
            await bot.send_message(message.chat.id, "Enter your new login", reply_markup=markup)

        elif message.text == 'Finish':
            mess, keyboard = keyboards.get_done_to_save_data(message)
            await bot.send_message(message.chat.id, mess, reply_markup=keyboard)

        elif message.text == 'Restart':
            mess, keyboard = keyboards.start_kb()
            await bot.send_message(message.chat.id, mess, reply_markup=keyboard)
            del config.USERS_PROFILE[message.chat.id]

        elif message.text == 'Save':
            if await bot_db.save_user_data(config.USERS_PROFILE[message.chat.id]):
                await bot.send_message(message.chat.id, 'Saving was successful!',
                                       reply_markup=types.ReplyKeyboardRemove())
                mess, keyboard = keyboards.go_to_site()
                await bot.send_message(message.chat.id, mess, reply_markup=keyboard)
                del config.USERS_PROFILE[message.chat.id]
            else:
                mess, keyboard = keyboards.start_kb(error_login=True)
                await bot.send_message(message.chat.id, mess, reply_markup=keyboard)
                del config.USERS_PROFILE[message.chat.id]

        elif message.chat.id in config.USERS_PROFILE:
            if config.USERS_PROFILE[message.chat.id]["login"] is None:
                config.USERS_PROFILE[message.chat.id]["login"] = message.text
                await bot.send_message(message.chat.id, "Enter your new password:")
            elif config.USERS_PROFILE[message.chat.id]["password"] is None:
                config.USERS_PROFILE[message.chat.id]["password"] = message.text
                await bot.send_message(message.chat.id, "Enter your first name:")
            elif config.USERS_PROFILE[message.chat.id]["first_name"] is None:
                config.USERS_PROFILE[message.chat.id]["first_name"] = message.text
                await bot.send_message(message.chat.id, "Enter your last name:")

            elif config.USERS_PROFILE[message.chat.id]["last_name"] is None:
                config.USERS_PROFILE[message.chat.id]["last_name"] = message.text
                mess, keyboard = keyboards.get_contact_kb()
                await bot.send_message(message.chat.id, mess, reply_markup=keyboard)

        else:
            await bot.send_message(message.chat.id, "I do not understand you!")
    except Exception as ex:
        mess, keyboard = keyboards.return_to_start_kb()
        await bot.send_message(message.chat.id, mess, reply_markup=keyboard)
        print("Error! In @dp.message_handler(content_types=['text'])", ex)


@dp.message_handler(content_types=['contact'])
async def get_kontakt(message):
    try:
        config.USERS_PROFILE[message.chat.id]["user_name"] = f"@{message.from_user.username}"
        config.USERS_PROFILE[message.chat.id]["phone"] = message.contact.phone_number
        mess, keyboard = keyboards.get_photo_kb()
        await bot.send_message(message.chat.id, mess, reply_markup=keyboard)
    except Exception as ex:
        mess, keyboard = keyboards.return_to_start_kb()
        await bot.send_message(message.chat.id, mess, reply_markup=keyboard)
        print("Error! In @dp.message_handler(content_types=['contact'])", ex)


@dp.message_handler(content_types=['photo'])
async def handler_photo(message):
    try:
        file_info = await bot.get_file(message.photo[-1].file_id)
        file_bytes = await bot.download_file(file_info.file_path)
        img = Image.open(file_bytes)
        output = BytesIO()
        img.save(output, format='JPEG', quality=75)
        output.seek(0)
        photo = InMemoryUploadedFile(
            file=output,
            field_name='photo',
            name=f'user_{message.chat.id}.jpg',
            content_type='image/jpeg',
            size=len(output.getvalue()),
            charset=None
        )
        config.USERS_PROFILE[message.chat.id]["photo"] = photo
        mess, keyboard = keyboards.get_done_to_save_data(message)
        await bot.send_message(message.chat.id, mess, reply_markup=keyboard)
    except Exception as ex:
        mess, keyboard = keyboards.return_to_start_kb()
        await bot.send_message(message.chat.id, mess, reply_markup=keyboard)
        print("Error! in @dp.message_handler(content_types=['photo'])", ex)


if __name__ == '__main__':
    executor.start_polling(dp)

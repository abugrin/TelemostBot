import os

from dotenv import load_dotenv

from telemost.telemost import Telemost
from telemost.types import AccessLevel
from yambot.yambot import MessengerBot

load_dotenv()
yb = MessengerBot(os.getenv('BOT_KEY'))
tm = Telemost(os.getenv('TELEMOST_KEY'))
main_menu = []


@yb.add_handler(button='/telemost')
def telemost_button(update):
    meeting = tm.create_meeting(AccessLevel.ORGANIZATION)
    yb.send_message(f'Создана встреча: ```{meeting.join_url}```', update)
    send_menu(update, main_menu)


@yb.add_handler(any=True)
def process_any(update):
    send_menu(update, main_menu)


def build_menu():
    button_telemost = {'text': 'Создать встречу', 'callback_data': {'cmd': '/telemost'}}
    return [button_telemost]


def send_menu(update, menu):
    yb.send_inline_keyboard(text='Доступные команды:', buttons=menu, update=update)


if __name__ == "__main__":
    main_menu = build_menu()
    yb.start_pooling()

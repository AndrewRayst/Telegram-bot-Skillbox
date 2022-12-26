import os
from typing import List

from aiogram import Bot as AIOBot, Dispatcher, executor, types

import emoji


class Bot:
    __bot_commands: List[str] = ['start', 'help', 'low', 'high', 'custom', 'history', 'game_rating']

    def __init__(self) -> None:
        self.__aioBot = AIOBot(token=os.getenv('BOT_TOKEN'))
        self.__dispatcher = Dispatcher(self.__aioBot)

    def start(self) -> str:
        self.write_history('start')

        msg = 'Приветствую!!! Я могу показать тебе рейтинг игр. Только выбери команду ниже '
        msg_emoji = emoji.emojize(':backhand_index_pointing_down:', variant='emoji_type')

        return msg + msg_emoji

    def get_help(self) -> str:
        self.write_history('help')
        return 'Help'

    def set_low(self) -> str:
        self.write_history('low')
        return 'low'

    def set_high(self) -> str:
        self.write_history('high')
        return 'high'

    def set_custom(self) -> str:
        self.write_history('custom')
        return 'custom'

    def get_history(self) -> str:
        return 'history'

    def write_history(self, command: str) -> None:
        pass

    def get_game_rating(self) -> str:
        self.write_history('game_rating')
        return 'Mafia: 7\nGod of war: 9'

    def run(self) -> None:
        async def on_startup(_: any) -> None:
            print('Бот включился')

        @self.__dispatcher.message_handler(commands=self.__bot_commands)
        async def command(msg: types.Message) -> None:
            match msg.text:
                case '/start':
                    await msg.answer(self.start())

                case '/help':
                    await msg.answer(self.get_help())

                case '/low':
                    await msg.answer(self.set_low())

                case '/high':
                    await msg.answer(self.set_high())

                case '/custom':
                    await msg.answer(self.set_custom())

                case '/game_rating':
                    await msg.answer(self.get_game_rating())

                case '/history':
                    await msg.answer(self.get_history())

                case _:
                    await msg.answer('Простите, но данная команда не существует.')

        executor.start_polling(self.__dispatcher, skip_updates=True, on_startup=on_startup)

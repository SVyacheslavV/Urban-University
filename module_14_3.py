from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import logging
import asyncio

api = "8017481106:AAH7KOBneCg5nvQO2qj9DRrugtwP1I1C8mY"
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

logging.basicConfig(level=logging.DEBUG, filemode='w', filename='bot.log', encoding='UTF-8',
                    format='%(asctime)s | %(levelname)s | %(message)s')

kb = ReplyKeyboardMarkup(resize_keyboard=True)  # создаём клавиатуру
button1 = KeyboardButton(text='Рассчитать')  # создаём кнопку 'Рассчитать'
button2 = KeyboardButton(text='Информация')  # создаём кнопку 'Информация'
kb.add(button1)  # размещаем кнопку с помощью add
kb.insert(button2)  # размещаем кнопку с помощью insert

kb_inl = InlineKeyboardMarkup()
button1 = InlineKeyboardButton(text='Рассчитать норму калорий', callback_data='calories')
button2 = InlineKeyboardButton(text='Формулы расчёта', callback_data='formulas')
kb_inl.add(button1)
kb_inl.insert(button2)


class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()


@dp.message_handler(text='Рассчитать')  # сработает при получении текста 'Рассчитать'
async def main_menu(message):
    await message.answer('Выберите опцию:', reply_markup=kb_inl)  # откроет kb_inl


@dp.callback_query_handler(text='calories')  # сработает при нажатии кнопки 'calories'
async def set_age(call):
    await call.message.answer('Введите свой возраст:')  # попросит ввести возраст
    await call.answer()
    await UserState.age.set()  # будет ждать ввода возраста


@dp.callback_query_handler(text='formulas')  # сработает при нажатии кнопки 'formulas'
async def get_formulas(call):
    await call.message.answer('10 х вес (кг) + 6,25 x рост (см) – 5 х возраст (г) + 5')
    await call.answer()


@dp.message_handler(state=UserState.age)  # сработает при получении возраста
async def set_growth(message, state):
    await state.update_data(age=message.text)  # обновит словарь по ключу age значение полученное от пользователя
    await message.answer('Введите свой рост:')  # попросит ввести рост
    await UserState.growth.set()  # будет ждать ввода роста


@dp.message_handler(state=UserState.growth)  # сработает при получении роста
async def set_weight(message, state):
    await state.update_data(growth=message.text)  # обновит словарь по ключу growth значение полученное от пользователя
    await message.answer('Введите свой вес:')  # попросит ввести вес
    await UserState.weight.set()  # будет ждать ввода веса


@dp.message_handler(state=UserState.weight)  # сработает при получении веса
async def send_calories(message, state):
    await state.update_data(weight=message.text)  # обновит словарь по ключу weight значение полученное от пользователя
    data = await state.get_data()  # в переменную data запомнит введённые данные
    norm = 10 * int(data['weight']) + 6.25 * int(data['growth']) - 5 * int(data['age']) + 5
    # при расчёте данные получаем из словаря data по ключам weight, growth, age
    await message.answer(
        f'{message.chat.first_name} Ваша норма калорий {norm}')  # выводит результаты расчёта пользователю
    await state.finish()  # финишируем машину состояний


@dp.message_handler(commands=['start'])  # сработает при получении команды /start
async def start(message):
    await message.answer(f'Привет {message.chat.first_name}! Я бот помогающий твоему здоровью.', reply_markup=kb)


@dp.message_handler(text='Информация')  # сработает при получении текста 'Информация' или нажатия кнопки 'Информация'
async def inform(message):
    await message.answer('Подсчёт нормы калорий по упрощённой формуле Миффлина - Сан Жеора.')


@dp.message_handler()  # сработает при получении всех остальных сообщений
async def all_messages(message):
    await message.answer(f'{message.chat.first_name} введите команду /start, чтобы начать общение.')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
from aiogram import Bot, executor, types, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
import asyncio

api = ""
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

kb = ReplyKeyboardMarkup(resize_keyboard=True)  # создаём клавиатуру
button1 = KeyboardButton(text='Рассчитать')  # создаём кнопку 'Рассчитать'
button2 = KeyboardButton(text='Информация')  # создаём кнопку 'Информация'
kb.insert(button1)  # размещаем кнопку с помощью insert
kb.insert(button2)  # размещаем кнопку с помощью insert


class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()


@dp.message_handler(text='Рассчитать')  # сработает при получении текста 'Рассчитать' или нажатия кнопки 'Рассчитать'
async def set_age(message):
    await message.answer('Введите свой возраст:')  # попросит ввести возраст
    await UserState.age.set()  # будет ждать ввода возраста


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
    data = await state.get_data()  # в переменную дата запомнит введённые данные
    norm = 10 * int(data['weight']) + 6.25 * int(data['growth']) - 5 * int(data['age']) + 5
    # при расчёте данные получаем из словаря data по ключам weight, growth, age
    await message.answer(f'Ваша норма калорий {norm}')  # выводит результаты расчёта пользователю
    await state.finish()  # финишируем машину состояний


@dp.message_handler(commands=['start'])  # сработает при получении команды /start
async def start(message):
    await message.answer('Привет! Я бот помогающий твоему здоровью.', reply_markup=kb)


@dp.message_handler(text='Информация') # сработает при получении текста 'Информация' или нажатия кнопки 'Информация'
async def inform(message):
    await message.answer('Подсчёт нормы калорий по упрощённой формуле Миффлина - Сан Жеора.')


@dp.message_handler()  # сработает при получении всех остальных сообщений
async def all_messages(message):
    await message.answer('Введите команду /start, чтобы начать общение.')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.types import KeyboardButton
from aiogram.types import contact
import logging
import requests
import logging

# connecting token
token = '5577211664:AAE8YNhvjYhLr-rKEp3NBKsUVZIgwM_eDSE'
logging.basicConfig(level=logging.INFO)

# all these are buttons
btn = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
btn.add("Fast-food 🥪", "Ichimliklar 🥤", "Desert 🍩")

inline = types.InlineKeyboardButton('Xarid qilish ✅', callback_data='next')
inline2 = types.InlineKeyboardButton('Bekor qilish 🚫', callback_data='stop')
forinline = types.InlineKeyboardMarkup()
forinline.add(inline, inline2)

order = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
q = KeyboardButton('Location', request_location=True)
q1 = KeyboardButton('Contact', request_contact=True)
q2 = KeyboardButton('Menu 📤')
order.add(q, q1, q2)

btnfast = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
btnfast.add('Lavash', 'Gamburger', 'Pitsa', 'KFC', 'Hot-dog', 'Menu 📤')

btnlavash = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
btnlavash.add('Mini lavash', 'Max lavash', 'Fast foodga qaytish ⬅️', 'Menu 📤')

btngamburger = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
btngamburger.add('Mini gamburger', 'Max gamburger', 'Fast foodga qaytish ⬅️', 'Menu 📤')

btnpitsa = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
btnpitsa.add('Mini pitsa', 'Max pitsa', 'Fast foodga qaytish ⬅️', 'Menu 📤')

btnhot = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
btnhot.add('Mini hot-dog', 'Max hot-dog', 'Fast foodga qaytish ⬅️', 'Menu 📤')

btnichimlik = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
btnichimlik.add('Coca-cola', 'Tropic', 'Sprite', 'Menu 📤')

btncola = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
btncola.add('0.5 litr', '1.5 litr', 'Ichimliklarga qaytish ⬅️', 'Menu 📤')

btndesert = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
btndesert.add('Napalyon', 'Olmali pirog', 'Rulet', 'Menu 📤')

btnnapalyon = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
btnnapalyon.add('Mini napalyon', 'Max napalyon', 'Desertga qaytish ⬅️', 'Menu 📤')

btnrulet = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
btnrulet.add('Mini rulet', 'Max rulet', 'Desertga qaytish ⬅️', 'Menu 📤')

# connecting bot
bot = Bot(token)
ab = Dispatcher(bot)
cont = contact

# start and help
@ab.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.reply(f'Qadrli {message.chat.first_name}, SeeFoodga xush kelibsiz 🌮', reply_markup=btn)


@ab.message_handler(commands=['help'])
async def help(message: types.Message):
    await message.reply(f'{message.chat.first_name}, muommoni batafsil tushuntirib bering')


# fast food category
@ab.message_handler(text='Fast-food 🥪')
async def fastfood(message: types.Message):
    await message.reply("Nima xohlaysiz?", reply_markup=btnfast)


@ab.message_handler(text='Lavash')
async def fastfood(message: types.Message):
    await message.reply('Qaysi biri?', reply_markup=btnlavash)


@ab.message_handler(text="Mini lavash")
async def mini(message: types.Message):
    rasm = open("pict/minilavash.jpeg", 'rb')
    await bot.send_photo(message.chat.id, rasm, caption='Mini lavash\n\nNarxi: 20.000som', reply_markup=forinline)


@ab.message_handler(text="Max lavash")
async def max(message: types.Message):
    rasm = open("pict/big.jpg", 'rb')
    await bot.send_photo(message.chat.id, rasm, caption='Max lavash\n\nNarxi: 30.000som', reply_markup=forinline)


# functions to order and to send location and contact
@ab.callback_query_handler(text=['next'])
async def asdff(call: types.CallbackQuery):
    await call.message.answer('Malumotingizni jonating', reply_markup=order)


@ab.callback_query_handler(text=['stop'])
async def stop(call:types.CallbackQuery):
    await call.message.answer('Buyurtma bekor qilindi!', reply_markup=btn)


# continue of fast food category
@ab.message_handler(text='Gamburger')
async def a(message: types.Message):
    await message.reply('Qaysi biri?', reply_markup=btngamburger)


@ab.message_handler(text="Mini gamburger")
async def masd(message: types.Message):
    rasm = open("pict/smallburger.jpeg", 'rb')
    await bot.send_photo(message.chat.id, rasm, caption='Mini gamburger\n\nNarxi: 18.000som', reply_markup=forinline)


@ab.message_handler(text="Max gamburger")
async def maxzx(message: types.Message):
    rasm = open("pict/bigburger.jpeg", 'rb')
    await bot.send_photo(message.chat.id, rasm, caption='Max gamburger\n\nNarxi: 28.000som', reply_markup=forinline)


@ab.message_handler(text='Pitsa')
async def f(message: types.Message):
    rasm = open('pict/pitsa.jpg', 'rb')
    await bot.send_photo(message.chat.id, rasm, caption='Pitsa\n\nNarxi: 32.000som', reply_markup=forinline)


@ab.message_handler(text='KFC')
async def od(message: types.Message):
    rasm = open("pict/kfc.jpg", 'rb')
    await bot.send_photo(message.chat.id, rasm, caption='KFC\n\nNarx: 24.000som', reply_markup=forinline)


@ab.message_handler(text='Hot-dog')
async def d(message: types.Message):
    await message.reply('Qaysi biri?', reply_markup=btnhot)


@ab.message_handler(text="Mini hot-dog")
async def masd(message: types.Message):
    rasm = open("pict/1*azFAHEZnlwylmcXHrnF6XQ.jpeg", 'rb')
    await bot.send_photo(message.chat.id, rasm, caption='Mini hot-dog\n\nNarxi: 12.000som', reply_markup=forinline)


@ab.message_handler(text="Max hot-dog")
async def maxzx(message: types.Message):
    rasm = open("pict/charred-hot-dogs-with-spicy-mayonnaise-106466-1.jpeg", 'rb')
    await bot.send_photo(message.chat.id, rasm, caption='Max hot-dog\n\nNarxi: 23.000som', reply_markup=forinline)


# function to come back to previous page
@ab.message_handler(text='Fast foodga qaytish ⬅️')
async def bak(message: types.Message):
    await message.reply('Ortga qaytdi', reply_markup=btnfast)


# drink category
@ab.message_handler(text='Ichimliklar 🥤')
async def s(message: types.Message):
    await message.reply("Nima xohlaysiz?", reply_markup=btnichimlik)


@ab.message_handler(text='Coca-cola')
async def q(message: types.Message):
    await message.reply("Qaysi biri?", reply_markup=btncola)


@ab.message_handler(text='Tropic')
async def e(message: types.Message):
    await message.reply("Qaysi biri?", reply_markup=btncola)


@ab.message_handler(text='Sprite')
async def w(message: types.Message):
    await message.reply("Qaysi biri?", reply_markup=btncola)


@ab.message_handler(text='0.5 litr')
async def suv(message: types.Message):
    await message.reply('0.5 litr\nNarx: 5.000som', reply_markup=forinline)


@ab.message_handler(text='1.5 litr')
async def suv(message: types.Message):
    await message.reply('1.5 litr\nNarx: 10.000som', reply_markup=forinline)


@ab.message_handler(text='Ichimliklarga qaytish ⬅️')
async def bak(message: types.Message):
    await message.reply('Ortga qaytdi', reply_markup=btnichimlik)


# desert category
@ab.message_handler(text='Desert 🍩')
async def e(message: types.Message):
    await message.reply("Nima xohlaysiz?", reply_markup=btndesert)


@ab.message_handler(text='Napalyon')
async def ezzzsdc(message: types.Message):
    await message.reply("Qaysi biri?", reply_markup=btnnapalyon)


@ab.message_handler(text="Mini napalyon")
async def mini(message: types.Message):
    rasm = open("pict/smallnap.jpg", 'rb')
    await bot.send_photo(message.chat.id, rasm, caption='Mini napalayon\n\nNarx: 30.000som', reply_markup=forinline)


@ab.message_handler(text="Max napalyon")
async def minicxz(message: types.Message):
    rasm = open("pict/bignap.jpg", 'rb')
    await bot.send_photo(message.chat.id, rasm, caption='Max napalayon\n\nNarx: 50.000som', reply_markup=forinline)


@ab.message_handler(text='Olmali pirog')
async def t(message: types.Message):
    rasm = open("pict/cake.jpg", 'rb')
    await bot.send_photo(message.chat.id, rasm, caption='Olmali pirog\n\nNarxi: 40.000som', reply_markup=forinline)


@ab.message_handler(text='Rulet')
async def ds(message: types.Message):
    await message.reply("Qaysi biri?", reply_markup=btnrulet)


@ab.message_handler(text="Mini rulet")
async def miniqqq(message: types.Message):
    rasm = open("pict/minirulet.jpg", 'rb')
    await bot.send_photo(message.chat.id, rasm, caption='Mini rulet\n\nNarx: 10.000som', reply_markup=forinline)


@ab.message_handler(text="Max rulet")
async def minicxz(message: types.Message):
    rasm = open("pict/bigrulet.jpg", 'rb')
    await bot.send_photo(message.chat.id, rasm, caption='Max rulet\n\nNarx: 26.000som', reply_markup=forinline)


@ab.message_handler(text='Desertga qaytish ⬅️')
async def bak(message: types.Message):
    await message.reply('Ortga qaytdi', reply_markup=btndesert)


# @ab.message_handler(content_types=types.contact)
# async def numbers(message:types.contact):
#     await message.answer('Contact qabul qilindi', reply_markup=btnmain)


# function to return to menu
@ab.message_handler(text='Menu 📤')
async def menu(message: types.Message):
    await message.reply(f'Qadrli {message.chat.first_name}, bosh saxifaga qaytdingiz 🌮', reply_markup=btn)


if __name__ == '__main__':
    executor.start_polling(ab, skip_updates=True)
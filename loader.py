from aiogram import Bot, Dispatcher, Router
from aiohttp.web_routedef import route

from config.token import TOKEN
import sqlite3

con = sqlite3.connect("data/data.db")
cursor = con.cursor()

router = Router()
dp = Dispatcher()
dp.include_router(router)
bot = Bot(TOKEN)

admin_id = [1222051636]
import logging
import asyncio
from loader import *

from handlers.users import start,registration,info
from handlers.admin import end_reg,start_reg,start_draw,commands

async def main():
    await dp.start_polling(bot,allowed_updates=dp.resolve_used_update_types())


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    asyncio.run(main())
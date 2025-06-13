import os
import logging 
import asyncio

from aiogram import F, Router, exceptions
from aiogram.filters import Command
from aiogram.types import CallbackQuery, Message, ContentType
from aiogram.fsm.context import FSMContext

import bot_api

router = Router()

@router.message(Command("start"))
async def start_handler(msg: Message, state: FSMContext):
    bot_api.register_user()
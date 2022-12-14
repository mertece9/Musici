import asyncio
from os import path

from pyrogram import filters
from pyrogram.types import (InlineKeyboardMarkup, InputMediaPhoto, Message,
                            Voice)
from youtube_search import YoutubeSearch

from Yukki import (BOT_USERNAME, DURATION_LIMIT, DURATION_LIMIT_MIN,
                   MUSIC_BOT_NAME, app, db_mem)
from Yukki.Decorators.permission import PermissionCheck
from Yukki.Inline import song_download_markup, song_markup
from Yukki.Utilities.url import get_url
from Yukki.Utilities.youtube import get_yt_info_query, get_yt_info_query_slider

loop = asyncio.get_event_loop()


@app.on_message(
    filters.command(["bul", f"bul@{BOT_USERNAME}"])
)
@PermissionCheck
async def play(_, message: Message):
    if message.chat.type == "private":
        pass
    else:
        if message.sender_chat:
            return await message.reply_text(
                "ðð ðĶðžðĩðŊðēð ððŋððŊððŧðąðŪ __ððŧðžðŧðķðš ðŊðķðŋ ðŽðžĖðŧðēððķð°ðķ__ ððķðððķðŧðķð!!\nâ\nâ°ððĻĖð§ðð­ðĒððĒ ðððĪðĨððŦðĒð§ððð§ ððŪðĨðĨðð§ðĒððĒ ðððŽðððĒð§ð ð ððŦðĒ ððĻĖð§ðŪĖð§."
            )
    try:
        await message.delete()
    except:
        pass
    url = get_url(message)
    if url:
        mystic = await message.reply_text("ððð ðĒðŽĖ§ðĨðð§ðĒðēðĻðŦ... ððŪĖð­ððð§ ðððĪðĨððēðĒð§ðĒðģ!")
        query = message.text.split(None, 1)[1]
        (
            title,
            duration_min,
            duration_sec,
            thumb,
            videoid,
        ) = await loop.run_in_executor(None, get_yt_info_query, query)
        if str(duration_min) == "None":
            return await mystic.edit("Sorry! Its a Live Video")
        await mystic.delete()
        buttons = song_download_markup(videoid, message.from_user.id)
        return await message.reply_photo(
            photo=thumb,
            caption=f"ððĖððķðš: **{title}\nâ\nâ°âģðĶðĖðŋðē:** {duration_min} ððŪðļðķðļðŪ\nâ\nâ°__[Video HakkÄąnda Ek Bilgi AlÄąn](https://t.me/{BOT_USERNAME}?start=info_{videoid})__",
            reply_markup=InlineKeyboardMarkup(buttons),
        )
    else:
        if len(message.command) < 2:
            await message.reply_text(
                "**ðððđðđðŪðŧðķðš:**\nâ\nâ°/bul [Youtube Url'si veya MÃžzik AdÄą]\nâ\nâ°Belirli Sorguyu indirir."
            )
            return
        mystic = await message.reply_text("âĒ> **AranÄąyor...**")
        query = message.text.split(None, 1)[1]
        (
            title,
            duration_min,
            duration_sec,
            thumb,
            videoid,
        ) = await loop.run_in_executor(None, get_yt_info_query, query)
        if str(duration_min) == "None":
            return await mystic.edit("Sorry! Its a Live Video")
        await mystic.delete()
        buttons = song_markup(
            videoid, duration_min, message.from_user.id, query, 0
        )
        return await message.reply_photo(
            photo=thumb,
            caption=f"ððĖððķðš: **{title}\nâ\nâ°âģðĶðĖðŋðē:** {duration_min} ððŪðļðķðļðŪ\nâ\nâ°__[Video HakkÄąnda Ek Bilgi AlÄąn](https://t.me/{BOT_USERNAME}?start=info_{videoid})__",
            reply_markup=InlineKeyboardMarkup(buttons),
        )


@app.on_callback_query(filters.regex("qwertyuiopasdfghjkl"))
async def qwertyuiopasdfghjkl(_, CallbackQuery):
    print("234")
    await CallbackQuery.answer()
    callback_data = CallbackQuery.data.strip()
    callback_request = callback_data.split(None, 1)[1]
    userid = CallbackQuery.from_user.id
    videoid, user_id = callback_request.split("|")
    buttons = song_download_markup(videoid, user_id)
    await CallbackQuery.edit_message_reply_markup(
        reply_markup=InlineKeyboardMarkup(buttons)
    )


@app.on_callback_query(filters.regex(pattern=r"song_right"))
async def song_right(_, CallbackQuery):
    callback_data = CallbackQuery.data.strip()
    callback_request = callback_data.split(None, 1)[1]
    what, type, query, user_id = callback_request.split("|")
    if CallbackQuery.from_user.id != int(user_id):
        return await CallbackQuery.answer(
            "ððēðŧðąðķ ð ðĖððķðīĖðķðŧðķ ððŋðŪ ððžððððš. ðð ðąðĖðīĖðšðēððķ ðļððđðđðŪðŧðšðŪðŧðŪ ðķððķðŧ ððēðŋðšðķððžðŋððš.",
            show_alert=True,
        )
    what = str(what)
    type = int(type)
    if what == "F":
        if type == 9:
            query_type = 0
        else:
            query_type = int(type + 1)
        await CallbackQuery.answer("ðĶðžðŧðŋðŪðļðķ ðĶðžðŧðð°Ė§ ððđðķðŧðķððžðŋ", show_alert=True)
        (
            title,
            duration_min,
            duration_sec,
            thumb,
            videoid,
        ) = await loop.run_in_executor(
            None, get_yt_info_query_slider, query, query_type
        )
        buttons = song_markup(
            videoid, duration_min, user_id, query, query_type
        )
        med = InputMediaPhoto(
            media=thumb,
            caption=f"ððĖððķðš: **{title}\nâ\nâ°âģðĶðĖðŋðē:** {duration_min} ððŪðļðķðļðŪ\nâ\nâ°__[Video HakkÄąnda Ek Bilgi AlÄąn](https://t.me/{BOT_USERNAME}?start=info_{videoid})__",
        )
        return await CallbackQuery.edit_message_media(
            media=med, reply_markup=InlineKeyboardMarkup(buttons)
        )
    if what == "B":
        if type == 0:
            query_type = 9
        else:
            query_type = int(type - 1)
        await CallbackQuery.answer("ðĒĖðŧð°ðēðļðķ ðĶðžðŧðð°ð ððđðšðŪ", show_alert=True)
        (
            title,
            duration_min,
            duration_sec,
            thumb,
            videoid,
        ) = await loop.run_in_executor(
            None, get_yt_info_query_slider, query, query_type
        )
        buttons = song_markup(
            videoid, duration_min, user_id, query, query_type
        )
        med = InputMediaPhoto(
            media=thumb,
            caption=f"ððĖððķðš: **{title}\nâ\nâ°âģðĶðĖðŋðē:** {duration_min} ððŪðļðķðļðŪ\nâ\nâ°__[Video HakkÄąnda Ek Bilgi AlÄąn](https://t.me/{BOT_USERNAME}?start=info_{videoid})__",
        )
        return await CallbackQuery.edit_message_media(
            media=med, reply_markup=InlineKeyboardMarkup(buttons)
        )

import asyncio
from os import path

from pyrogram import filters
from pyrogram.types import (InlineKeyboardMarkup, InputMediaPhoto, Message,
                            Voice)
from youtube_search import YoutubeSearch

import Yukki
from Yukki import (BOT_USERNAME, DURATION_LIMIT, DURATION_LIMIT_MIN,
                   MUSIC_BOT_NAME, app, db_mem)
from Yukki.Core.PyTgCalls.Converter import convert
from Yukki.Core.PyTgCalls.Downloader import download
from Yukki.Core.PyTgCalls.Tgdownloader import telegram_download
from Yukki.Database import (get_active_video_chats, get_video_limit,
                            is_active_video_chat)
from Yukki.Decorators.assistant import AssistantAdd
from Yukki.Decorators.checker import checker
from Yukki.Decorators.logger import logging
from Yukki.Decorators.permission import PermissionCheck
from Yukki.Inline import (livestream_markup, playlist_markup, search_markup,
                          search_markup2, url_markup, url_markup2)
from Yukki.Utilities.changers import seconds_to_min, time_to_seconds
from Yukki.Utilities.chat import specialfont_to_normal
from Yukki.Utilities.stream import start_stream, start_stream_audio
from Yukki.Utilities.theme import check_theme
from Yukki.Utilities.thumbnails import gen_thumb
from Yukki.Utilities.url import get_url
from Yukki.Utilities.videostream import start_stream_video
from Yukki.Utilities.youtube import (get_yt_info_id, get_yt_info_query,
                                     get_yt_info_query_slider)

loop = asyncio.get_event_loop()


@app.on_message(
    filters.command(["oynat", "play", f"oynat@{BOT_USERNAME}"]) & filters.group
)
@checker
@logging
@PermissionCheck
@AssistantAdd
async def play(_, message: Message):
    await message.delete()
    if message.chat.id not in db_mem:
        db_mem[message.chat.id] = {}
    if message.sender_chat:
        return await message.reply_text(
            "ðð ðĶðžðĩðŊðēð ððŋððŊððŧðąðŪ __ððŧðžðŧðķðš ðŊðķðŋ ðŽðžĖðŧðēððķð°ðķ__ ððķðððķðŧðķð!\nâ\nâ°ðŽðžĖðŧðēððķð°ðķ ððŪðļðđðŪðŋðķðŧðąðŪðŧ ðððđðđðŪðŧðķð°ðķ ððēððŪðŊðķðŧðŪ ðīðēðŋðķ ðąðžĖðŧðĖðŧ."
        )
    audio = (
        (message.reply_to_message.audio or message.reply_to_message.voice)
        if message.reply_to_message
        else None
    )
    video = (
        (message.reply_to_message.video or message.reply_to_message.document)
        if message.reply_to_message
        else None
    )
    url = get_url(message)
    if audio:
        mystic = await message.reply_text(
            "âĒ> **LÃžtfen bekleyiniz** !"
        )
        try:
            read = db_mem[message.chat.id]["live_check"]
            if read:
                return await mystic.edit(
                    "**CanlÄą yayÄąn OynatÄąlÄąyor...Kapatmak iÃ§in durdurun**"
                )
            else:
                pass
        except:
            pass
        if audio.file_size > 1073741824:
            return await mystic.edit_text(
                "Ses dosyalarÄą 150 mb'den kÃžÃ§Ãžk olmalÄądÄąr"
            )
        duration_min = seconds_to_min(audio.duration)
        duration_sec = audio.duration
        if (audio.duration) > DURATION_LIMIT:
            return await mystic.edit_text(
                f"ðĶðĖðŋðē ðĶðķðŧðķðŋðķ ððĖ§ðķðđðąðķ\nâ\nâ°ðĖððķðŧ ðĐðēðŋðķðđðēðŧ ðĶðĖðŋðē: **{DURATION_LIMIT_MIN}** ððŪðļðķðļðŪ(s)\nâ\nâ°ððđðķðŧðŪðŧ ðĶðĖðŋðē: **{duration_min}** ððŪðļðķðļðŪ(s)"
            )
        file_name = (
            audio.file_unique_id
            + "."
            + (
                (audio.file_name.split(".")[-1])
                if (not isinstance(audio, Voice))
                else "ogg"
            )
        )
        file_name = path.join(path.realpath("downloads"), file_name)
        file = await convert(
            (await message.reply_to_message.download(file_name))
            if (not path.isfile(file_name))
            else file_name,
        )
        return await start_stream_audio(
            message,
            file,
            "smex1",
            "**Mp3 FormatÄąna uygun mÃžzik**",
            duration_min,
            duration_sec,
            mystic,
        )
    elif video:
        limit = await get_video_limit(141414)
        if not limit:
            return await message.reply_text(
                "ððžĖðŋðĖðŧððĖðđðĖ ððŋðŪðšðŪðđðŪðŋ ðķð°Ė§ðķðŧ ððķðšðķð ð§ðŪðŧðķðšðđðŪðŧðšðŪðąðķ\nâ\nâ° /limit [ðððĨð§ðĒðģðð ððĻð­ ððĻĖð§ðð­ðĒððĒ ððŪðĨðĨðð§ðĒððĒðĨððŦðĒ] ð­ððŦðððĒð§ððð§ ððĻð­ð­ð ðĒðģðĒð§ ðŊððŦðĒðĨðð§ ðððĪðŽðĒðĶðŪðĶ ððĻĖðŦðŪĖð§ð­ðŪĖðĨðŪĖ ððŦððĶð ðððēðĒðŽðĒ ðĒðĖ§ðĒð§ ððĒðŦ ððĒð§ðĒðŦ ðððĨðĒðŦðĨððēðĒð§."
            )
        count = len(await get_active_video_chats())
        if int(count) == int(limit):
            if await is_active_video_chat(message.chat.id):
                pass
            else:
                return await message.reply_text(
                    "ðĖðģðŪĖðŦ ððĒðĨððŦðĒðĶ! ððĻð­, ððð ððŽĖ§ðĒðŦðĒ ðēðŪĖðĪðĨðð§ðĶð ðŽðĻðŦðŪð§ðĨððŦðĒ ð§ðððð§ðĒðēðĨð ðēððĨð§ðĒðģðð ðŽðĒð§ðĒðŦðĨðĒ ðŽððēðĒðð ð ðĻĖðŦðŪĖð§ð­ðŪĖðĨðŪĖ ð ðĻĖðŦðŪĖðŽĖ§ðĶððēð ðĒðģðĒð§ ðŊððŦðĒðŦ. ððĒð ĖððŦ ððĒðŦðĖ§ðĻðĪ ðŽðĻðĄððð­ ðŽĖ§ðŪ ðð§ðð ð ðĻĖðŦðŪĖð§ð­ðŪĖðĨðŪĖ ð ðĻĖðŦðŪĖðŽĖ§ðĶð ðĪðŪðĨðĨðð§ðĒðēðĻðŦ. ðððŽð ð ððĖ§ðĶððēðĒ ððð§ððēðĒð§ ðŊððēð ðððĄð ðŽðĻð§ðŦð ð­ððĪðŦððŦ ððð§ððēðĒð§"
                )
        mystic = await message.reply_text(
            "âĒ> **LÃžtfen bekleyiniz** !"
        )
        try:
            read = db_mem[message.chat.id]["live_check"]
            if read:
                return await mystic.edit(
                    "**CanlÄą yayÄąn OynatÄąlÄąyor...Kapatmak iÃ§in durdurun**"
                )
            else:
                pass
        except:
            pass
        file = await telegram_download(message, mystic)
        return await start_stream_video(
            message,
            file,
            "**Telegram'dan istenen video**",
            mystic,
        )
    elif url:
        mystic = await message.reply_text("âĒ> **LÃžtfen bekleyiniz** !")
        if not message.reply_to_message:
            query = message.text.split(None, 1)[1]
        else:
            query = message.reply_to_message.text
        (
            title,
            duration_min,
            duration_sec,
            thumb,
            videoid,
        ) = get_yt_info_query(query)
        await mystic.delete()
        buttons = url_markup2(videoid, duration_min, message.from_user.id)
        return await message.reply_photo(
            photo=thumb,
            caption=f"âķïļ **ÉŠsÉŠáī** : **{title}**\n\nâ **sáīĘáī** : **{duration_min}** DK\n\n[Video HakkÄąnda Bilgi AlÄąn](https://t.me/{BOT_USERNAME}?start=info_{videoid})",
            reply_markup=InlineKeyboardMarkup(buttons),
        )
    else:
        if len(message.command) < 2:
            buttons = playlist_markup(
                message.from_user.first_name, message.from_user.id, "abcd"
            )
            await message.reply_photo(
                photo="Utils/Playlist.jpg",
                caption=(
                    "**ðððđðđðŪðŧðķðš:** /oynat [MÃžzik AdÄą veya Youtube BaÄlantÄąsÄą veya Sese Cevap Ver]\nâ\nâ°ÃalÄąn! AÅaÄÄądan birini seÃ§in."
                ),
                reply_markup=InlineKeyboardMarkup(buttons),
            )
            return
        mystic = await message.reply_text("âĒ> **áīĘáīÉīÉŠĘáīĘ** .")
        query = message.text.split(None, 1)[1]
        (
            title,
            duration_min,
            duration_sec,
            thumb,
            videoid,
        ) = get_yt_info_query(query)
        await mystic.delete()
        buttons = url_markup(
            videoid, duration_min, message.from_user.id, query, 0
        )
        return await message.reply_photo(
            photo=thumb,
            caption=f"âķïļ **ÉŠsÉŠáī** : **{title}**\n\nâ **sáīĘáī** : **{duration_min}** DK\n\n[Video HakkÄąnda Ek Bilgi AlÄąn](https://t.me/{BOT_USERNAME}?start=info_{videoid})",
            reply_markup=InlineKeyboardMarkup(buttons),
        )


@app.on_callback_query(filters.regex(pattern=r"MusicStream"))
async def Music_Stream(_, CallbackQuery):
    if CallbackQuery.message.chat.id not in db_mem:
        db_mem[CallbackQuery.message.chat.id] = {}
    try:
        read1 = db_mem[CallbackQuery.message.chat.id]["live_check"]
        if read1:
            return await CallbackQuery.answer(
                "**CanlÄą yayÄąn OynatÄąlÄąyor...Kapatmak iÃ§in durdurun**",
                show_alert=True,
            )
        else:
            pass
    except:
        pass
    callback_data = CallbackQuery.data.strip()
    callback_request = callback_data.split(None, 1)[1]
    chat_id = CallbackQuery.message.chat.id
    chat_title = CallbackQuery.message.chat.title
    videoid, duration, user_id = callback_request.split("|")
    if str(duration) == "None":
        buttons = livestream_markup("720", videoid, duration, user_id)
        return await CallbackQuery.edit_message_text(
            "ððŪðŧðđðķ ðŽðŪððķðŧ ððđðīðķðđðŪðŧðąðķ\nâ\nððŪðŧðđðķ ðŪðļðķðĖ§ðķ ðžððŧðŪððšðŪðļ ðķðððēðŋ ðšðķððķðŧðķð? ðð, ðšðēðð°ðð ðšðĖððķðļ ð°Ė§ðŪðđðšðŪððķ ðąððŋðąððŋðŪð°ðŪðļ (ððŪðŋððŪ) ððē ð°ðŪðŧðđðķ ððķðąðēðž ðŪðļðķðĖ§ðķ ðŊðŪðĖ§ðđðŪððŪð°ðŪðļððķðŋ.",
            reply_markup=InlineKeyboardMarkup(buttons),
        )
    if CallbackQuery.from_user.id != int(user_id):
        return await CallbackQuery.answer(
            "ðð ððēðŧðķðŧ ðķð°Ė§ðķðŧ ðąðēðīĖðķðđ ððžððððš ððžðđðŪ ððķðļðđðŪðšðŪ!\nâ\nâ°ððēðŧðąðķ ðĶĖ§ðŪðŋðļðķðŧðķ ððŋðŪ.", show_alert=True
        )
    await CallbackQuery.message.delete()
    title, duration_min, duration_sec, thumbnail = get_yt_info_id(videoid)
    if duration_sec > DURATION_LIMIT:
        return await CallbackQuery.message.reply_text(
            f"ðĶðĖðŋðē ðĶðķðŧðķðŋðķ ððĖ§ðķðđðąðķ\n\nðĖððķðŧ ðĐðēðŋðķðđðēðŧ ðĶðĖðŋðē: **{DURATION_LIMIT_MIN}** ðąðŪðļðķðļðŪ(s)\n\nððđðķðŧðŪðŧ ðĶðĖðŋðē: **{duration_min}** ðąðŪðļðķðļðŪ(s)"
        )
    await CallbackQuery.answer(f"Ä°Åleme alÄąndÄą:- {title[:20]}", show_alert=True)
    mystic = await CallbackQuery.message.reply_text(
        f"**{MUSIC_BOT_NAME}** Ä°ndiriyorum\nâ\nðŠ§ Ä°sim : {title[:50]}\nâ\n0% ââââââââââââ 100%"
    )
    downloaded_file = await loop.run_in_executor(
        None, download, videoid, mystic, title
    )
    raw_path = await convert(downloaded_file)
    theme = await check_theme(chat_id)
    chat_title = await specialfont_to_normal(chat_title)
    thumb = await gen_thumb(thumbnail, title, user_id, theme, chat_title)
    if chat_id not in db_mem:
        db_mem[chat_id] = {}
    await start_stream(
        CallbackQuery,
        raw_path,
        videoid,
        thumb,
        title,
        duration_min,
        duration_sec,
        mystic,
    )


@app.on_callback_query(filters.regex(pattern=r"Search"))
async def search_query_more(_, CallbackQuery):
    callback_data = CallbackQuery.data.strip()
    callback_request = callback_data.split(None, 1)[1]
    query, user_id = callback_request.split("|")
    if CallbackQuery.from_user.id != int(user_id):
        return await CallbackQuery.answer(
            "ððēðŧðąðķ ð ðĖððķðīĖðķðŧðķ ððŋðŪ ððžððððš. ðð ðąðĖðīĖðšðēððķ ðļððđðđðŪðŧðšðŪðŧðŪ ðķððķðŧ ððēðŋðšðķððžðŋððš.",
            show_alert=True,
        )
    await CallbackQuery.answer("Daha Fazla SonuÃ§ AranÄąyor")
    results = YoutubeSearch(query, max_results=5).to_dict()
    med = InputMediaPhoto(
        media="Utils/Result.jpeg",
        caption=(
            f"1ïļâĢ<b>{results[0]['title']}</b>\n  â  ð <u>__[ððļ ððķðđðīðķ ððđ](https://t.me/{BOT_USERNAME}?start=info_{results[0]['id']})__</u>\n\n2ïļâĢ<b>{results[1]['title']}</b>\n  â  ð <u>__[ððļ ððķðđðīðķ ððđ](https://t.me/{BOT_USERNAME}?start=info_{results[1]['id']})__</u>\n\n3ïļâĢ<b>{results[2]['title']}</b>\n  â  ð <u>__[ððļ ððķðđðīðķ ððđ](https://t.me/{BOT_USERNAME}?start=info_{results[2]['id']})__</u>\n\n4ïļâĢ<b>{results[3]['title']}</b>\n  â  ð <u>__[ððļ ððķðđðīðķ ððđ](https://t.me/{BOT_USERNAME}?start=info_{results[3]['id']})__</u>\n\n5ïļâĢ<b>{results[4]['title']}</b>\n  â  ð <u>__[ððļ ððķðđðīðķ ððđ](https://t.me/{BOT_USERNAME}?start=info_{results[4]['id']})__</u>"
        ),
    )
    buttons = search_markup(
        results[0]["id"],
        results[1]["id"],
        results[2]["id"],
        results[3]["id"],
        results[4]["id"],
        results[0]["duration"],
        results[1]["duration"],
        results[2]["duration"],
        results[3]["duration"],
        results[4]["duration"],
        user_id,
        query,
    )
    return await CallbackQuery.edit_message_media(
        media=med, reply_markup=InlineKeyboardMarkup(buttons)
    )


@app.on_callback_query(filters.regex(pattern=r"popat"))
async def popat(_, CallbackQuery):
    callback_data = CallbackQuery.data.strip()
    callback_request = callback_data.split(None, 1)[1]
    userid = CallbackQuery.from_user.id
    i, query, user_id = callback_request.split("|")
    if CallbackQuery.from_user.id != int(user_id):
        return await CallbackQuery.answer(
            "ðð ððēðŧðķðŧ ðķð°Ė§ðķðŧ ðąðēðīĖðķðđ! ððēðŧðąðķ ðĶĖ§ðŪðŋðļðķðŧðķððķ ððŋðŪððķðŧ", show_alert=True
        )
    results = YoutubeSearch(query, max_results=10).to_dict()
    if int(i) == 1:
        buttons = search_markup2(
            results[5]["id"],
            results[6]["id"],
            results[7]["id"],
            results[8]["id"],
            results[9]["id"],
            results[5]["duration"],
            results[6]["duration"],
            results[7]["duration"],
            results[8]["duration"],
            results[9]["duration"],
            user_id,
            query,
        )
        await CallbackQuery.edit_message_text(
            f"6ïļâĢ<b>{results[5]['title']}</b>\n  â  ð <u>__[ððļ ððķðđðīðķ ððđ](https://t.me/{BOT_USERNAME}?start=info_{results[5]['id']})__</u>\n\n7ïļâĢ<b>{results[6]['title']}</b>\n  â  ð <u>__[ððļ ððķðđðīðķ ððđ](https://t.me/{BOT_USERNAME}?start=info_{results[6]['id']})__</u>\n\n8ïļâĢ<b>{results[7]['title']}</b>\n  â  ð <u>__[ððļ ððķðđðīðķ ððđ](https://t.me/{BOT_USERNAME}?start=info_{results[7]['id']})__</u>\n\n9ïļâĢ<b>{results[8]['title']}</b>\n  â  ð <u>__[ððļ ððķðđðīðķ ððđ](https://t.me/{BOT_USERNAME}?start=info_{results[8]['id']})__</u>\n\nð<b>{results[9]['title']}</b>\n  â  ð <u>__[ððļ ððķðđðīðķ ððđ](https://t.me/{BOT_USERNAME}?start=info_{results[9]['id']})__</u>",
            reply_markup=InlineKeyboardMarkup(buttons),
        )
        disable_web_page_preview = True
        return
    if int(i) == 2:
        buttons = search_markup(
            results[0]["id"],
            results[1]["id"],
            results[2]["id"],
            results[3]["id"],
            results[4]["id"],
            results[0]["duration"],
            results[1]["duration"],
            results[2]["duration"],
            results[3]["duration"],
            results[4]["duration"],
            user_id,
            query,
        )
        await CallbackQuery.edit_message_text(
            f"1ïļâĢ<b>{results[0]['title']}</b>\n  â  ð <u>__[ððļ ððķðđðīðķ ððđ](https://t.me/{BOT_USERNAME}?start=info_{results[0]['id']})__</u>\n\n2ïļâĢ<b>{results[1]['title']}</b>\n  â  ð <u>__[ððļ ððķðđðīðķ ððđ](https://t.me/{BOT_USERNAME}?start=info_{results[1]['id']})__</u>\n\n3ïļâĢ<b>{results[2]['title']}</b>\n  â  ð <u>__[ððļ ððķðđðīðķ ððđ](https://t.me/{BOT_USERNAME}?start=info_{results[2]['id']})__</u>\n\n4ïļâĢ<b>{results[3]['title']}</b>\n  â  ð <u>__[ððļ ððķðđðīðķ ððđ](https://t.me/{BOT_USERNAME}?start=info_{results[3]['id']})__</u>\n\n5ïļâĢ<b>{results[4]['title']}</b>\n  â  ð <u>__[ððļ ððķðđðīðķ ððđ](https://t.me/{BOT_USERNAME}?start=info_{results[4]['id']})__</u>",
            reply_markup=InlineKeyboardMarkup(buttons),
        )
        disable_web_page_preview = True
        return


@app.on_callback_query(filters.regex(pattern=r"slider"))
async def slider_query_results(_, CallbackQuery):
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
        await CallbackQuery.answer("Sonraki sonuÃ§ alÄąnÄąyor.", show_alert=True)
        (
            title,
            duration_min,
            duration_sec,
            thumb,
            videoid,
        ) = get_yt_info_query_slider(query, query_type)
        buttons = url_markup(
            videoid, duration_min, user_id, query, query_type
        )
        med = InputMediaPhoto(
            media=thumb,
            caption=f"âķïļ **ÉŠsÉŠáī** : **{title}**\n\nâ **sáīĘáī** : **{duration_min}** DK\n\n[Video HakkÄąnda Ek Bilgi AlÄąn](https://t.me/{BOT_USERNAME}?start=info_{videoid})",
        )
        return await CallbackQuery.edit_message_media(
            media=med, reply_markup=InlineKeyboardMarkup(buttons)
        )
    if what == "B":
        if type == 0:
            query_type = 9
        else:
            query_type = int(type - 1)
        await CallbackQuery.answer("Ãnceki Sonucu AlÄąnÄąyor", show_alert=True)
        (
            title,
            duration_min,
            duration_sec,
            thumb,
            videoid,
        ) = get_yt_info_query_slider(query, query_type)
        buttons = url_markup(
            videoid, duration_min, user_id, query, query_type
        )
        med = InputMediaPhoto(
            media=thumb,
            caption=f"âķïļ **ÉŠsÉŠáī** : **{title}**\n\nâ **sáīĘáī** : **{duration_min}** DK\n\n[Video HakkÄąnda Ek Bilgi AlÄąn](https://t.me/{BOT_USERNAME}?start=info_{videoid})",
        )
        return await CallbackQuery.edit_message_media(
            media=med, reply_markup=InlineKeyboardMarkup(buttons)
        )

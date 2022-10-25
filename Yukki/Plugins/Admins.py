import asyncio
import os
import random
from asyncio import QueueEmpty

from pyrogram import filters
from pyrogram.types import (CallbackQuery, InlineKeyboardButton,
                            InlineKeyboardMarkup, KeyboardButton, Message,
                            ReplyKeyboardMarkup, ReplyKeyboardRemove)

from config import get_queue
from Yukki import BOT_USERNAME, MUSIC_BOT_NAME, app, db_mem
from Yukki.Core.PyTgCalls import Queues
from Yukki.Core.PyTgCalls.Converter import convert
from Yukki.Core.PyTgCalls.Downloader import download
from Yukki.Core.PyTgCalls.Yukki import (pause_stream, resume_stream,
                                        skip_stream, skip_video_stream,
                                        stop_stream)
from Yukki.Database import (is_active_chat, is_music_playing, music_off,
                            music_on, remove_active_chat,
                            remove_active_video_chat)
from Yukki.Decorators.admins import AdminRightsCheck
from Yukki.Decorators.checker import checker, checkerCB
from Yukki.Inline import audio_markup, primary_markup, secondary_markup2
from Yukki.Utilities.changers import time_to_seconds
from Yukki.Utilities.chat import specialfont_to_normal
from Yukki.Utilities.theme import check_theme
from Yukki.Utilities.thumbnails import gen_thumb
from Yukki.Utilities.timer import start_timer
from Yukki.Utilities.youtube import get_m3u8, get_yt_info_id

loop = asyncio.get_event_loop()


__MODULE__ = "📚 ᴍᴜ̈ᴢɪᴋ ᴋᴏᴍᴜᴛʟᴀʀɪ"
__HELP__ = """


» /bul 
    - **ᴍᴜᴢɪᴋ & ᴠɪᴅᴇᴏ ɪɴᴅɪʀ .**

» /oynat 
    - **ᴍᴜᴢɪᴋ ᴏʏɴᴀᴛ .**

» /durdur
    - **ᴍᴜᴢɪɢɪ ᴅᴜʀᴅᴜʀ .**

» /devam 
    - **ᴍᴜᴢɪɢɪ sᴜʀᴅᴜʀ .**

» /atla
    - **ᴍᴜᴢɪɢɪ ᴀᴛʟᴀ .**

» /son
    - **ᴍᴜᴢɪɢɪ sᴏɴʟᴀɴᴅɪʀ .**

» /auth
    - **ʙᴏᴛ ʏᴏɴᴇᴛɪᴄɪsɪ ᴇᴋʟᴇ .**

» /unauth
    - **ʏᴏɴᴇᴛɪᴄɪ ʏᴇᴛᴋɪsɪɴɪ ᴀʟ .**


🪧 /oynat **ᴋᴏᴍᴜᴛᴜɴᴜ ᴋᴜʟʟᴀɴɪɴ, ᴀsɪsᴛᴀɴ ɢʀᴜʙᴀ ᴋᴇɴᴅɪsɪ ᴋᴀᴛɪʟɪʀ . . .**


» /settheme ( **renk** )
    - **sᴏʜʙᴇᴛɪɴɪᴢ ɪᴄ̧ɪɴ ʙɪʀ ᴛᴇᴍᴀ ᴏʟᴜsᴛᴜʀᴜɴ . . .**

🪧 **ᴏʀɴᴇᴋ ʀᴇɴᴋʟᴇʀ** •>
**blue , black , red , green , grey , orange , pink , yellow .**

"""


@app.on_message(
    filters.command(["durdur", "atla", "devam", "son"])
    & filters.group
)
@AdminRightsCheck
@checker
async def admins(_, message: Message):
    global get_queue
    if not len(message.command) == 1:
        return await message.reply_text("Hata! Komutun Yanlış Kullanımı.")
    if not await is_active_chat(message.chat.id):
        return await message.reply_text("𝗦𝗲𝘀𝗹𝗶 𝘀𝗼𝗵𝗯𝗲𝘁𝘁𝗲 𝗵𝗶𝗰̧𝗯𝗶𝗿 𝘀̧𝗲𝘆 𝗰̧𝗮𝗹𝗺𝗶𝘆𝗼𝗿.")
    chat_id = message.chat.id
    if message.command[0][1] == "u":
        if not await is_music_playing(message.chat.id):
            return await message.reply_text("𝗠𝘂̈𝘇𝗶𝗸 𝘇𝗮𝘁𝗲𝗻 𝗗𝘂𝗿𝗮𝗸𝗹𝗮𝘁𝗶𝗹𝗱𝗶.")
        await music_off(chat_id)
        await pause_stream(chat_id)
        await message.reply_text(
            f"🎧 𝗦𝗲𝘀𝗹𝗶 𝘀𝗼𝗵𝗯𝗲𝘁 𝗗𝘂𝗿𝗮𝗸𝗹𝗮𝘁𝗶𝗹𝗱𝗶\n│\n╰𝗗𝘂𝗿𝗱𝘂𝗿𝗮𝗻: **{message.from_user.mention}**!"
        )
    if message.command[0][1] == "e":
        if await is_music_playing(message.chat.id):
            return await message.reply_text("𝗠𝘂̈𝘇𝗶𝗸 𝘇𝗮𝘁𝗲𝗻 𝗖̧𝗮𝗹𝗶𝘆𝗼𝗿.")
        await music_on(chat_id)
        await resume_stream(chat_id)
        await message.reply_text(
            f"🎧 𝗦𝗲𝘀𝗹𝗶 𝘀𝗼𝗵𝗯𝗲𝘁 𝗧𝗮𝗿𝗮𝗳𝗶𝗻𝗱𝗮𝗻 𝗗𝗲𝘃𝗮𝗺 𝗘𝗱𝗶𝗹𝗱𝗶\n│\n╰𝗗𝗲𝘃𝗮𝗺 𝗲𝗱𝗲𝗻: **{message.from_user.mention}**!"
        )
    if message.command[0][1] == "o":
        if message.chat.id not in db_mem:
            db_mem[message.chat.id] = {}
        wtfbro = db_mem[message.chat.id]
        wtfbro["live_check"] = False
        try:
            Queues.clear(message.chat.id)
        except QueueEmpty:
            pass
        await remove_active_chat(chat_id)
        await remove_active_video_chat(chat_id)
        await stop_stream(chat_id)
        await message.reply_text(
            f"🎧 𝗦𝗲𝘀𝗹𝗶 𝗦𝗼𝗵𝗯𝗲𝘁 𝗦𝗼𝗻𝘂\n│\n╰𝗗𝘂𝗿𝗱𝘂𝗿𝗮𝗻: **{message.from_user.mention}**!"
        )
    if message.command[0][1] == "t":
        if message.chat.id not in db_mem:
            db_mem[message.chat.id] = {}
        wtfbro = db_mem[message.chat.id]
        wtfbro["live_check"] = False
        Queues.task_done(chat_id)
        if Queues.is_empty(chat_id):
            await remove_active_chat(chat_id)
            await remove_active_video_chat(chat_id)
            await message.reply_text(
                "𝗔𝗿𝘁𝗶𝗸 𝗦𝗶𝗿𝗮𝗱𝗮 𝗠𝘂̈𝘇𝗶𝗸 __𝗬𝗼𝗸__ \n│\n╰𝗦𝗲𝘀𝗹𝗶 𝗦𝗼𝗵𝗯𝗲𝘁𝗶 𝗕𝗶𝗿𝗮𝗸𝗶𝘆𝗼𝗿𝘂𝗺 :("
            )
            await stop_stream(chat_id)
            return
        else:
            videoid = Queues.get(chat_id)["file"]
            got_queue = get_queue.get(chat_id)
            if got_queue:
                got_queue.pop(0)
            finxx = f"{videoid[0]}{videoid[1]}{videoid[2]}"
            aud = 0
            if str(finxx) == "raw":
                await skip_stream(chat_id, videoid)
                afk = videoid
                title = db_mem[videoid]["title"]
                duration_min = db_mem[videoid]["duration"]
                duration_sec = int(time_to_seconds(duration_min))
                mention = db_mem[videoid]["username"]
                videoid = db_mem[videoid]["videoid"]
                if str(videoid) == "smex1":
                    buttons = buttons = audio_markup(
                        videoid,
                        message.from_user.id,
                        duration_min,
                        duration_min,
                    )
                    thumb = "Utils/Telegram.JPEG"
                    aud = 1
                else:
                    _path_ = _path_ = (
                        (str(afk))
                        .replace("_", "", 1)
                        .replace("/", "", 1)
                        .replace(".", "", 1)
                    )
                    thumb = f"cache/{_path_}final.png"
                    buttons = primary_markup(
                        videoid,
                        message.from_user.id,
                        duration_min,
                        duration_min,
                    )
                final_output = await message.reply_photo(
                    photo=thumb,
                    reply_markup=InlineKeyboardMarkup(buttons),
                    caption=f"<b>𝗔𝘁𝗹𝗮𝗻𝗮𝗻 𝗦𝗲𝘀𝗹𝗶 𝗦𝗼𝗵𝗯𝗲𝘁</b>\n│\n╰🎥<b>𝗢𝘆𝗻𝗮𝘁𝗺𝗮𝘆𝗮 𝗕𝗮𝘀̧𝗹𝗮𝗱𝗶:</b> **{title}** \n│\n╰⏳<b>𝗦𝘂̈𝗿𝗲:</b> **{duration_min}** \n│\n╰▫️<b>𝗧𝗮𝗹𝗲𝗽 𝗲𝗱𝗲𝗻: </b> {mention}",
                )
                await start_timer(
                    videoid,
                    duration_min,
                    duration_sec,
                    final_output,
                    message.chat.id,
                    message.from_user.id,
                    aud,
                )
            elif str(finxx) == "s1s":
                mystic = await message.reply_text(
                    "𝗚𝘂̈𝘇𝗲𝗹 𝗣𝗮𝗿𝗰̧𝗮𝘆𝗱𝗶.. 𝗕𝗶𝗿 𝗦𝗼𝗻𝗿𝗮𝗸𝗶 𝗩𝗶𝗱𝗲𝗼 𝗔𝗸𝗶𝘀̧𝗶𝗻𝗮 𝗚𝗲𝗰̧𝗶𝘆𝗼𝗿𝘂𝘇."
                )
                afk = videoid
                read = (str(videoid)).replace("s1s_", "", 1)
                s = read.split("_+_")
                quality = s[0]
                videoid = s[1]
                if int(quality) == 1080:
                    try:
                        await skip_video_stream(chat_id, videoid, 720, mystic)
                    except Exception as e:
                        return await mystic.edit(
                            f"𝗩𝗶𝗱𝗲𝗼 𝗮𝗸𝗶𝘀̧𝗶𝗻𝗶 𝗱𝗲𝗴̆𝗶𝘀̧𝘁𝗶𝗿𝗶𝗿𝗸𝗲𝗻 𝗵𝗮𝘁𝗮 𝗼𝗹𝘂𝘀̧𝘁𝘂.\n│\n╰𝗢𝗹𝗮𝘀𝗶 𝗦𝗲𝗯𝗲𝗽:- {e}"
                        )
                    buttons = secondary_markup2("Smex1", message.from_user.id)
                    mention = db_mem[afk]["username"]
                    await mystic.delete()
                    final_output = await message.reply_photo(
                        photo="Utils/Telegram.JPEG",
                        reply_markup=InlineKeyboardMarkup(buttons),
                        caption=(
                            f"<b>𝗔𝘁𝗹𝗮𝗻𝗮𝗻 𝗚𝗼̈𝗿𝘂̈𝗻𝘁𝘂̈𝗹𝘂̈ 𝗦𝗼𝗵𝗯𝗲𝘁</b>\n│\n╰▫️𝗧𝗮𝗹𝗲𝗽 𝗲𝗱𝗲𝗻: **{mention}**"
                        ),
                    )
                    await mystic.delete()
                else:
                    (
                        title,
                        duration_min,
                        duration_sec,
                        thumbnail,
                    ) = get_yt_info_id(videoid)
                    nrs, ytlink = await get_m3u8(videoid)
                    if nrs == 0:
                        return await mystic.edit(
                            "𝗩𝗶𝗱𝗲𝗼 𝗕𝗶𝗰̧𝗶𝗺𝗹𝗲𝗿𝗶 𝗴𝗲𝘁𝗶𝗿𝗶𝗹𝗲𝗺𝗲𝗱𝗶.",
                        )
                    try:
                        await skip_video_stream(
                            chat_id, ytlink, quality, mystic
                        )
                    except Exception as e:
                        return await mystic.edit(
                            f"𝗩𝗶𝗱𝗲𝗼 𝗮𝗸𝗶𝘀̧𝗶𝗻𝗶 𝗱𝗲𝗴̆𝗶𝘀̧𝘁𝗶𝗿𝗶𝗿𝗸𝗲𝗻 𝗵𝗮𝘁𝗮 𝗼𝗹𝘂𝘀̧𝘁𝘂.\n│\n╰𝗢𝗹𝗮𝘀𝗶 𝗦𝗲𝗯𝗲𝗽:- {e}"
                        )
                    theme = await check_theme(chat_id)
                    c_title = message.chat.title
                    user_id = db_mem[afk]["user_id"]
                    chat_title = await specialfont_to_normal(c_title)
                    thumb = await gen_thumb(
                        thumbnail, title, user_id, theme, chat_title
                    )
                    buttons = primary_markup(
                        videoid, user_id, duration_min, duration_min
                    )
                    mention = db_mem[afk]["username"]
                    await mystic.delete()
                    final_output = await message.reply_photo(
                        photo=thumb,
                        reply_markup=InlineKeyboardMarkup(buttons),
                        caption=(
                            f"<b>𝗔𝘁𝗹𝗮𝗻𝗮𝗻 𝗚𝗼̈𝗿𝘂̈𝗻𝘁𝘂̈𝗹𝘂̈ 𝗦𝗼𝗵𝗯𝗲𝘁</b>\n│\n╰🎥<b>𝗩𝗶𝗱𝗲𝗼 𝗢𝘆𝗻𝗮𝘁𝗺𝗮𝘆𝗮 𝗕𝗮𝘀̧𝗹𝗮𝗱𝗶: </b> **[{title[:25]}]**(https://www.youtube.com/watch?v={videoid}) \n│\n╰▫️𝗧𝗮𝗹𝗲𝗽 𝗲𝗱𝗲𝗻: **{mention}**"
                        ),
                    )
                    await mystic.delete()
                    os.remove(thumb)
                    await start_timer(
                        videoid,
                        duration_min,
                        duration_sec,
                        final_output,
                        message.chat.id,
                        message.from_user.id,
                        aud,
                    )
            else:
                mystic = await message.reply_text(
                    f"**{MUSIC_BOT_NAME}** 𝗖̧𝗮𝗹𝗺𝗮 𝗟𝗶𝘀𝘁𝗲𝘀𝗶 𝗜̇𝘀̧𝗹𝗲𝘃𝗶\n│\n╰𝗖̧𝗮𝗹𝗺𝗮 𝗟𝗶𝘀𝘁𝗲𝘀𝗶𝗻𝗱𝗲𝗻 𝗦𝗼𝗻𝗿𝗮𝗸𝗶 𝗠𝘂̈𝘇𝗶𝗸𝗹𝗲𝗿𝗶 𝗜̇𝗻𝗱𝗶𝗿𝗺𝗲...."
                )
                (
                    title,
                    duration_min,
                    duration_sec,
                    thumbnail,
                ) = get_yt_info_id(videoid)
                await mystic.edit(
                    f"**{MUSIC_BOT_NAME}** 𝗜̇𝗡𝗗𝗜̇𝗥𝗜̇𝗖𝗜̇\n│\n╰𝗜̇𝗦𝗜̇𝗠: **{title[:50]}**\n\n0% ▂▃▄▅▆▇▉ 100%"
                )
                downloaded_file = await loop.run_in_executor(
                    None, download, videoid, mystic, title
                )
                raw_path = await convert(downloaded_file)
                await skip_stream(chat_id, raw_path)
                theme = await check_theme(chat_id)
                chat_title = await specialfont_to_normal(message.chat.title)
                thumb = await gen_thumb(
                    thumbnail, title, message.from_user.id, theme, chat_title
                )
                buttons = primary_markup(
                    videoid, message.from_user.id, duration_min, duration_min
                )
                await mystic.delete()
                mention = db_mem[videoid]["username"]
                final_output = await message.reply_photo(
                    photo=thumb,
                    reply_markup=InlineKeyboardMarkup(buttons),
                    caption=(
                        f"<b>𝗔𝘁𝗹𝗮𝗻𝗮𝗻 𝗚𝗼̈𝗿𝘂̈𝗻𝘁𝘂̈𝗹𝘂̈ 𝗦𝗼𝗵𝗯𝗲𝘁</b>\n│\n╰🎥<b>𝗢𝘆𝗻𝗮𝘁𝗺𝗮𝘆𝗮 𝗕𝗮𝘀̧𝗹𝗮𝗱𝗶: </b>[{title[:25]}](https://www.youtube.com/watch?v={videoid}) \n│\n╰⏳<b>𝗦𝘂̈𝗿𝗲:</b> **{duration_min}** 𝗗𝗮𝗸𝗶𝗸𝗮\n│\n╰▫️𝗧𝗮𝗹𝗲𝗽 𝗲𝗱𝗲𝗻: **{mention}**"
                    ),
                )
                os.remove(thumb)
                await start_timer(
                    videoid,
                    duration_min,
                    duration_sec,
                    final_output,
                    message.chat.id,
                    message.from_user.id,
                    aud,
                )

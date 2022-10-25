from pyrogram.types import (CallbackQuery, InlineKeyboardButton,
                            InlineKeyboardMarkup, InputMediaPhoto, Message)


def check_markup(user_name, user_id, videoid):
    buttons = [
        [
        InlineKeyboardButton("🪧 𝖪𝖺𝗇𝖺𝗅 ", url="t.me/ProTubeSupport"),
        InlineKeyboardButton("🇹🇷 𝖣𝖾𝗌𝗍𝖾𝗄 ", url="t.me/sohbetmuhabbetw"),
        ],
        [InlineKeyboardButton(text="• 𝖪𝖺𝗉𝖺𝗍", callback_data="close")],
    ]
    return buttons


def playlist_markup(user_name, user_id, videoid):
    buttons = [
        [
        InlineKeyboardButton("🪧 𝖪𝖺𝗇𝖺𝗅 ", url="t.me/ProTubeSupport"),
        InlineKeyboardButton("🇹🇷 𝖣𝖾𝗌𝗍𝖾𝗄 ", url="t.me/sohbetmuhabbetw"),
        ],
        [InlineKeyboardButton(text="• 𝖪𝖺𝗉𝖺𝗍", callback_data="close")],
    ]
    return buttons


def play_genre_playlist(user_id, type, videoid):
    buttons = [
        [
            InlineKeyboardButton(
                text=f"ᴀʀᴀʙᴇsᴋ",
                callback_data=f"play_playlist {user_id}|{type}|Arabesk",
            ),
            InlineKeyboardButton(
                text=f"ᴋᴜʀᴛᴄᴇ",
                callback_data=f"play_playlist {user_id}|{type}|Kürtçe",
            ),
        ],
        [
            InlineKeyboardButton(
                text=f"ʀᴇᴍɪx",
                callback_data=f"play_playlist {user_id}|{type}|Remix",
            ),
            InlineKeyboardButton(
                text=f"ʏᴀʙᴀɴᴄɪ",
                callback_data=f"play_playlist {user_id}|{type}|Yabancı",
            ),
        ],
        [
            InlineKeyboardButton(
                text=f"ᴅɪɴɪ",
                callback_data=f"play_playlist {user_id}|{type}|Dini",
            ),
            InlineKeyboardButton(
                text=f"ᴘᴏᴘ",
                callback_data=f"play_playlist {user_id}|{type}|Pop",
            ),
        ],
        [
            InlineKeyboardButton(
                text=f"ɴᴏsᴛᴀᴊɪ",
                callback_data=f"play_playlist {user_id}|{type}|Nostaji",
            ),
            InlineKeyboardButton(
                text=f"ᴋᴀʀɪsɪᴋ",
                callback_data=f"play_playlist {user_id}|{type}|Karışık",
            ),
        ],
        [
            InlineKeyboardButton(
                text="• ɢᴇʀɪ",
                callback_data=f"main_playlist {videoid}|{type}|{user_id}",
            ),
            InlineKeyboardButton(text="❌ ᴍᴇɴᴜ ᴋᴀᴘᴀᴛ", callback_data="close"),
        ],
    ]
    return buttons


def add_genre_markup(user_id, type, videoid):
    buttons = [
        [
            InlineKeyboardButton(
                text=f"✚ ᴘᴏᴘ",
                callback_data=f"add_playlist {videoid}|{type}|Pop",
            ),
            InlineKeyboardButton(
                text=f"✚ ᴅɪɴɪ",
                callback_data=f"add_playlist {videoid}|{type}|Dini",
            ),
        ],
        [
            InlineKeyboardButton(
                text=f"✚ ʀᴇᴍɪx",
                callback_data=f"add_playlist {videoid}|{type}|Remix",
            ),
            InlineKeyboardButton(
                text=f"✚ ʏᴀʙᴀɴᴄɪ",
                callback_data=f"add_playlist {videoid}|{type}|Yabancı",
            ),
        ],
        [
            InlineKeyboardButton(
                text=f"✚ ᴀʀᴀʙᴇsᴋ",
                callback_data=f"add_playlist {videoid}|{type}|Arabesk",
            ),
            InlineKeyboardButton(
                text=f"✚ ᴋᴜʀᴛᴄᴇ",
                callback_data=f"add_playlist {videoid}|{type}|Kürtçe",
            ),
        ],
        [
            InlineKeyboardButton(
                text=f"✚ ɴᴏsᴛᴀᴊɪ",
                callback_data=f"add_playlist {videoid}|{type}|Nostaji",
            ),
            InlineKeyboardButton(
                text=f"✚ ᴋᴀʀɪsɪᴋ",
                callback_data=f"add_playlist {videoid}|{type}|Karışık",
            ),
        ],
        [
            InlineKeyboardButton(
                text="• ɢᴇʀɪ", callback_data=f"goback {videoid}|{user_id}"
            ),
            InlineKeyboardButton(text="• ᴍᴇɴᴜ ᴋᴀᴘᴀᴛ", callback_data="close"),
        ],
    ]
    return buttons


def check_genre_markup(type, videoid, user_id):
    buttons = [
        [
            InlineKeyboardButton(
                text=f"ᴘᴏᴘ", callback_data=f"check_playlist {type}|Pop"
            ),
            InlineKeyboardButton(
                text=f"ᴅɪɴɪ", callback_data=f"check_playlist {type}|Dini"
            ),
        ],
        [
            InlineKeyboardButton(
                text=f"ʀᴇᴍɪx", callback_data=f"check_playlist {type}|Remix"
            ),
            InlineKeyboardButton(
                text=f"ʏᴀʙᴀɴᴄɪ", callback_data=f"check_playlist {type}|Yabancı"
            ),
        ],
        [
            InlineKeyboardButton(
                text=f"ᴀʀᴀʙᴇsᴋ",
                callback_data=f"check_playlist {type}|Arabesk",
            ),
            InlineKeyboardButton(
                text=f"ᴋᴜʀᴛᴄᴇ",
                callback_data=f"check_playlist {type}|Kürtçe",
            ),
        ],
        [
            InlineKeyboardButton(
                text=f"ɴᴏsᴛᴀᴊɪ",
                callback_data=f"check_playlist {type}|Nostaji",
            ),
            InlineKeyboardButton(
                text=f"ᴋᴀʀɪsɪᴋ", callback_data=f"check_playlist {type}|Karışık"
            ),
        ],
        [InlineKeyboardButton(text="• ᴍᴇɴᴜ ᴋᴀᴘᴀᴛ", callback_data="close")],
    ]
    return buttons


def third_playlist_markup(user_name, user_id, third_name, userid, videoid):
    buttons = [
        [
            InlineKeyboardButton(
                text=f"𝖦𝗋𝗎𝖻 𝖯𝗅𝖺𝗒𝗅𝗂𝗌𝗍",
                callback_data=f"show_genre {user_id}|Group|{videoid}",
            ),
            InlineKeyboardButton(
                text=f"{user_name[:8]} ~ 𝖯𝗅𝖺𝗒𝗅𝗂𝗌𝗍",
                callback_data=f"show_genre {user_id}|Personal|{videoid}",
            ),
        ],
        [
            InlineKeyboardButton(
                text=f"{third_name[:16]} ~ 𝖯𝗅𝖺𝗒𝗅𝗂𝗌𝗍",
                callback_data=f"show_genre {userid}|third|{videoid}",
            ),
        ],
        [InlineKeyboardButton(text="• 𝖪𝖺𝗉𝖺𝗍", callback_data="close")],
    ]
    return buttons


def paste_queue_markup(url):
    buttons = [
        [InlineKeyboardButton(text="𝖲𝗂𝗋𝖺𝖽𝖺𝗄𝗂 𝖯𝗅𝖺𝗒𝗅𝗂𝗌𝗍", url=f"{url}")],
        [InlineKeyboardButton(text="• 𝖬𝖾𝗇𝗎 𝖪𝖺𝗉𝖺𝗍", callback_data=f"close")],
    ]
    return buttons


def fetch_playlist(user_name, type, genre, user_id, url):
    buttons = [
        [
            InlineKeyboardButton(
                text=f"𝖮𝗒𝗇𝖺𝗍 {user_name[:10]}'s {genre} 𝖯𝗅𝖺𝗒𝗅𝗂𝗌𝗍",
                callback_data=f"play_playlist {user_id}|{type}|{genre}",
            ),
        ],
        [InlineKeyboardButton(text="𝖯𝗅𝖺𝗒𝗅𝗂𝗌𝗍 𝖦𝗈𝗓 𝖠𝗍", url=f"{url}")],
        [InlineKeyboardButton(text="• 𝖬𝖾𝗇𝗎 𝖪𝖺𝗉𝖺𝗍", callback_data=f"close")],
    ]
    return buttons


def delete_playlist_markuup(type, genre):
    buttons = [
        [
            InlineKeyboardButton(
                text=f"𝖤𝖵𝖤𝖳 𝖲𝗂𝗅",
                callback_data=f"delete_playlist {type}|{genre}",
            ),
            InlineKeyboardButton(text="𝖧𝖠𝖸𝖨𝖱!", callback_data=f"close"),
        ],
    ]
    return buttons

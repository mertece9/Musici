from pyrogram.types import (CallbackQuery, InlineKeyboardButton,
                            InlineKeyboardMarkup, InputMediaPhoto, Message)


def check_markup(user_name, user_id, videoid):
    buttons = [
        [
        InlineKeyboardButton("πͺ§ πͺπΊππΊπ ", url="t.me/ProTubeSupport"),
        InlineKeyboardButton("πΉπ· π£πΎπππΎπ ", url="t.me/sohbetmuhabbetw"),
        ],
        [InlineKeyboardButton(text="β’ πͺπΊππΊπ", callback_data="close")],
    ]
    return buttons


def playlist_markup(user_name, user_id, videoid):
    buttons = [
        [
        InlineKeyboardButton("πͺ§ πͺπΊππΊπ ", url="t.me/ProTubeSupport"),
        InlineKeyboardButton("πΉπ· π£πΎπππΎπ ", url="t.me/sohbetmuhabbetw"),
        ],
        [InlineKeyboardButton(text="β’ πͺπΊππΊπ", callback_data="close")],
    ]
    return buttons


def play_genre_playlist(user_id, type, videoid):
    buttons = [
        [
            InlineKeyboardButton(
                text=f"α΄Κα΄Κα΄sα΄",
                callback_data=f"play_playlist {user_id}|{type}|Arabesk",
            ),
            InlineKeyboardButton(
                text=f"α΄α΄Κα΄α΄α΄",
                callback_data=f"play_playlist {user_id}|{type}|KΓΌrtΓ§e",
            ),
        ],
        [
            InlineKeyboardButton(
                text=f"Κα΄α΄Ιͺx",
                callback_data=f"play_playlist {user_id}|{type}|Remix",
            ),
            InlineKeyboardButton(
                text=f"Κα΄Κα΄Ι΄α΄Ιͺ",
                callback_data=f"play_playlist {user_id}|{type}|YabancΔ±",
            ),
        ],
        [
            InlineKeyboardButton(
                text=f"α΄ΙͺΙ΄Ιͺ",
                callback_data=f"play_playlist {user_id}|{type}|Dini",
            ),
            InlineKeyboardButton(
                text=f"α΄α΄α΄",
                callback_data=f"play_playlist {user_id}|{type}|Pop",
            ),
        ],
        [
            InlineKeyboardButton(
                text=f"Ι΄α΄sα΄α΄α΄Ιͺ",
                callback_data=f"play_playlist {user_id}|{type}|Nostaji",
            ),
            InlineKeyboardButton(
                text=f"α΄α΄ΚΙͺsΙͺα΄",
                callback_data=f"play_playlist {user_id}|{type}|KarΔ±ΕΔ±k",
            ),
        ],
        [
            InlineKeyboardButton(
                text="β’ Ι’α΄ΚΙͺ",
                callback_data=f"main_playlist {videoid}|{type}|{user_id}",
            ),
            InlineKeyboardButton(text="β α΄α΄Ι΄α΄ α΄α΄α΄α΄α΄", callback_data="close"),
        ],
    ]
    return buttons


def add_genre_markup(user_id, type, videoid):
    buttons = [
        [
            InlineKeyboardButton(
                text=f"β α΄α΄α΄",
                callback_data=f"add_playlist {videoid}|{type}|Pop",
            ),
            InlineKeyboardButton(
                text=f"β α΄ΙͺΙ΄Ιͺ",
                callback_data=f"add_playlist {videoid}|{type}|Dini",
            ),
        ],
        [
            InlineKeyboardButton(
                text=f"β Κα΄α΄Ιͺx",
                callback_data=f"add_playlist {videoid}|{type}|Remix",
            ),
            InlineKeyboardButton(
                text=f"β Κα΄Κα΄Ι΄α΄Ιͺ",
                callback_data=f"add_playlist {videoid}|{type}|YabancΔ±",
            ),
        ],
        [
            InlineKeyboardButton(
                text=f"β α΄Κα΄Κα΄sα΄",
                callback_data=f"add_playlist {videoid}|{type}|Arabesk",
            ),
            InlineKeyboardButton(
                text=f"β α΄α΄Κα΄α΄α΄",
                callback_data=f"add_playlist {videoid}|{type}|KΓΌrtΓ§e",
            ),
        ],
        [
            InlineKeyboardButton(
                text=f"β Ι΄α΄sα΄α΄α΄Ιͺ",
                callback_data=f"add_playlist {videoid}|{type}|Nostaji",
            ),
            InlineKeyboardButton(
                text=f"β α΄α΄ΚΙͺsΙͺα΄",
                callback_data=f"add_playlist {videoid}|{type}|KarΔ±ΕΔ±k",
            ),
        ],
        [
            InlineKeyboardButton(
                text="β’ Ι’α΄ΚΙͺ", callback_data=f"goback {videoid}|{user_id}"
            ),
            InlineKeyboardButton(text="β’ α΄α΄Ι΄α΄ α΄α΄α΄α΄α΄", callback_data="close"),
        ],
    ]
    return buttons


def check_genre_markup(type, videoid, user_id):
    buttons = [
        [
            InlineKeyboardButton(
                text=f"α΄α΄α΄", callback_data=f"check_playlist {type}|Pop"
            ),
            InlineKeyboardButton(
                text=f"α΄ΙͺΙ΄Ιͺ", callback_data=f"check_playlist {type}|Dini"
            ),
        ],
        [
            InlineKeyboardButton(
                text=f"Κα΄α΄Ιͺx", callback_data=f"check_playlist {type}|Remix"
            ),
            InlineKeyboardButton(
                text=f"Κα΄Κα΄Ι΄α΄Ιͺ", callback_data=f"check_playlist {type}|YabancΔ±"
            ),
        ],
        [
            InlineKeyboardButton(
                text=f"α΄Κα΄Κα΄sα΄",
                callback_data=f"check_playlist {type}|Arabesk",
            ),
            InlineKeyboardButton(
                text=f"α΄α΄Κα΄α΄α΄",
                callback_data=f"check_playlist {type}|KΓΌrtΓ§e",
            ),
        ],
        [
            InlineKeyboardButton(
                text=f"Ι΄α΄sα΄α΄α΄Ιͺ",
                callback_data=f"check_playlist {type}|Nostaji",
            ),
            InlineKeyboardButton(
                text=f"α΄α΄ΚΙͺsΙͺα΄", callback_data=f"check_playlist {type}|KarΔ±ΕΔ±k"
            ),
        ],
        [InlineKeyboardButton(text="β’ α΄α΄Ι΄α΄ α΄α΄α΄α΄α΄", callback_data="close")],
    ]
    return buttons


def third_playlist_markup(user_name, user_id, third_name, userid, videoid):
    buttons = [
        [
            InlineKeyboardButton(
                text=f"π¦πππ» π―ππΊπππππ",
                callback_data=f"show_genre {user_id}|Group|{videoid}",
            ),
            InlineKeyboardButton(
                text=f"{user_name[:8]} ~ π―ππΊπππππ",
                callback_data=f"show_genre {user_id}|Personal|{videoid}",
            ),
        ],
        [
            InlineKeyboardButton(
                text=f"{third_name[:16]} ~ π―ππΊπππππ",
                callback_data=f"show_genre {userid}|third|{videoid}",
            ),
        ],
        [InlineKeyboardButton(text="β’ πͺπΊππΊπ", callback_data="close")],
    ]
    return buttons


def paste_queue_markup(url):
    buttons = [
        [InlineKeyboardButton(text="π²πππΊπ½πΊππ π―ππΊπππππ", url=f"{url}")],
        [InlineKeyboardButton(text="β’ π¬πΎππ πͺπΊππΊπ", callback_data=f"close")],
    ]
    return buttons


def fetch_playlist(user_name, type, genre, user_id, url):
    buttons = [
        [
            InlineKeyboardButton(
                text=f"π?πππΊπ {user_name[:10]}'s {genre} π―ππΊπππππ",
                callback_data=f"play_playlist {user_id}|{type}|{genre}",
            ),
        ],
        [InlineKeyboardButton(text="π―ππΊπππππ π¦ππ π π", url=f"{url}")],
        [InlineKeyboardButton(text="β’ π¬πΎππ πͺπΊππΊπ", callback_data=f"close")],
    ]
    return buttons


def delete_playlist_markuup(type, genre):
    buttons = [
        [
            InlineKeyboardButton(
                text=f"π€π΅π€π³ π²ππ",
                callback_data=f"delete_playlist {type}|{genre}",
            ),
            InlineKeyboardButton(text="π§π πΈπ¨π±!", callback_data=f"close"),
        ],
    ]
    return buttons

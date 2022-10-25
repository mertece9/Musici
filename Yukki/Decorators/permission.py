from typing import Dict, List, Union

from Yukki import BOT_ID, app


def PermissionCheck(mystic):
    async def wrapper(_, message):
        a = await app.get_chat_member(message.chat.id, BOT_ID)
        if a.status != "administrator":
            return await message.reply_text(
                "**GEREKEN İZİNLER**:\n"
                + "\n• **SESLİ SOHBETLERİ YÖNETME**"
                + "\n• **MESAJLARI SİLME**"
                + "\n• **BAĞLANTI İLE DAVET ETME**"
            )
        if not a.can_manage_voice_chats:
            await message.reply_text(
                "Gerekli izne sahip değilim."
                + "\nİZİN: **SESLİ SOHBETLERİ YÖNETME**"
            )
            return
        if not a.can_delete_messages:
            await message.reply_text(
                "Gerekli izne sahip değilim."
                + "\nİZİN: **MESAJLARI SİLME"
            )
            return
        if not a.can_invite_users:
            await message.reply_text(
                "Bu eylemi gerçekleştirmek için gerekli izne sahip değilim."
                + "\nİZİN: **BAĞLANTI İLE DAVET ETME**"
            )
            return
        return await mystic(_, message)

    return wrapper

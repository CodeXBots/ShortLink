class script(object):
    START_TXT = """<b>Hello {}, My Name {}, I am a advance File Store Bot with Permanent links + Custom URL Shortner + Streaming and Cloning Features.</b>"""
  
    CAPTION = """<b>📂 ғɪʟᴇɴᴀᴍᴇ : {file_name}

sɪᴢᴇ ⚙️: {file_size}

Jᴏɪɴ [ᴜᴘᴅᴀᴛᴇ ᴄʜᴀɴɴᴇʟ](https://telegram.me/RahulReviewsYT)</b>"""

    SHORTENER_API_MESSAGE = """<b>Tᴏ ᴀᴅᴅ ᴏʀ ᴜᴘᴅᴀᴛᴇ ʏᴏᴜʀ Sʜᴏʀᴛɴᴇʀ Wᴇʙsɪᴛᴇ API, /api (ᴀᴘɪ)
            
<b>Ex: /api 6ldbekdbwk*******ej

<b>Cᴜʀʀᴇɴᴛ Wᴇʙsɪᴛᴇ: {base_site}

Cᴜʀʀᴇɴᴛ Sʜᴏʀᴛᴇɴᴇʀ API:</b> `{shortener_api}`

If You Want To Remove Api Then Copy This And Send To Bot - `/api None`"""

    CLONE_START_TXT = """<b>Hello {}, My Name {}, I am a advance File Store Bot with Permanent links + Custom URL Shortner + Streaming and Cloning Features.

If you want this features then create your own clone bot from <a href=https://telegram.me/RahulReviewsYT>Here</a></b>"""

    ABOUT_TXT = """<b>🤖 ᴍʏ ɴᴀᴍᴇ: {}

📝 ʟᴀɴɢᴜᴀɢᴇ: <a href=https://www.python.org>Python</a>

📚 ʟɪʙʀᴀʀʏ: <a href=https://docs.pyrogram.org>Pyrogram</a>

🧑🏻‍💻 ᴅᴇᴠᴇʟᴏᴘᴇʀ: <a href=https://telegram.me/CodeXBro>Rahul</a>

👥 sᴜᴘᴘᴏʀᴛ ɢʀᴏᴜᴘ: <a href=https://telegram.me/CodeXSupport>@CodeXSupport</a>

📢 ᴜᴘᴅᴀᴛᴇ ᴄʜᴀɴɴᴇʟ: <a href=https://telegram.me/RahulReviewsYT>@RahulReviewsYT</a></b>
"""

    CABOUT_TXT = """<b>🤖 ᴍʏ ɴᴀᴍᴇ: {}

📝 ʟᴀɴɢᴜᴀɢᴇ: <a href=https://www.python.org>𝐏𝐲𝐭𝐡𝐨𝐧𝟑</a>

📚 ʟɪʙʀᴀʀʏ: <a href=https://docs.pyrogram.org>𝐏𝐲𝐫𝐨𝐠𝐫𝐚𝐦</a>

🧑🏻‍💻 ᴅᴇᴠᴇʟᴏᴘᴇʀ: <a href=tg://user?id={}>ᴅᴇᴠᴇʟᴏᴘᴇʀ</a></b>
"""

    CLONE_TXT = """<b>ʜᴇʟʟᴏ {} 👋

First Send /clone command then follow below steps.
    
1) sᴇɴᴅ <code>/newbot</code> ᴛᴏ @BotFather
2) ɢɪᴠᴇ ᴀ ɴᴀᴍᴇ ꜰᴏʀ ʏᴏᴜʀ ʙᴏᴛ.
3) ɢɪᴠᴇ ᴀ ᴜɴɪǫᴜᴇ ᴜsᴇʀɴᴀᴍᴇ.
4) ᴛʜᴇɴ ʏᴏᴜ ᴡɪʟʟ ɢᴇᴛ ᴀ ᴍᴇssᴀɢᴇ ᴡɪᴛʜ ʏᴏᴜʀ ʙᴏᴛ ᴛᴏᴋᴇɴ.
5) ꜰᴏʀᴡᴀʀᴅ ᴛʜᴀᴛ ᴍᴇssᴀɢᴇ ᴛᴏ ᴍᴇ.

ᴛʜᴇɴ ɪ ᴀᴍ ᴛʀʏ ᴛᴏ ᴄʀᴇᴀᴛᴇ ᴀ ᴄᴏᴘʏ ʙᴏᴛ ᴏғ ᴍᴇ ғᴏʀ ʏᴏᴜ ᴏɴʟʏ 😌</b>"""

    HELP_TXT = """<b>💢 Hᴏᴡ Tᴏ Usᴇ Tʜɪs Bᴏᴛ ☺️

🔻 /link - ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴠɪᴅᴇᴏ ᴏʀ ғɪʟᴇ ᴛᴏ ɢᴇᴛ sʜᴀʀᴀʙʟᴇ ʟɪɴᴋ

🔻 /batch - sᴇɴᴅ ғɪʀsᴛ ʟɪɴᴋ ᴏғ ғɪʟᴇ sᴛᴏʀᴇ ᴄʜᴀɴɴᴇʟ ᴘᴏsᴛ ᴛʜᴇɴ ʟᴀsᴛ ᴘᴏsᴛ ʟɪɴᴋ ᴀɴᴅ ᴍᴀᴋᴇ sᴜʀᴇ ʙᴏᴛ ɪs ᴀᴅᴍɪɴ ɪɴ ʏᴏᴜʀ ғɪʟᴇ sᴛᴏʀᴇ ᴄʜᴀɴɴᴇʟ.
ᴇx - /batch https://telegram.me/RahulReviewsYT/3 https://telegram.me/RahulReviewsYT/17

🔻 /base_site - ᴜsᴇ ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ ᴛᴏ sᴇᴛ ᴜʀʟ sʜᴏʀᴛɴᴇʀ ʟɪɴᴋ ᴅᴏᴍᴀɪɴ 
ᴇx - /base_site ʏᴏᴜʀᴅᴏᴍᴀɪɴ.ᴄᴏᴍ

🔻 /api - sᴇᴛ ʏᴏᴜʀ ᴜʀʟ sʜᴏʀᴛɴᴇʀ ᴀᴄᴄᴏᴜɴᴛ ᴀᴘɪ 
ᴇx - /api ʏᴏᴜʀᴀᴘɪ

🔻 /deletecloned - ᴜsᴇ ᴛʜɪs ғᴏʀ ᴅᴇʟᴇᴛᴇ ʏᴏᴜʀ ᴄʟᴏɴᴇ ʙᴏᴛ 
ᴇx - /deletecloned ʏᴏᴜʀ ʙᴏᴛ ᴛᴏᴋᴇɴ

🔻 /broadcast - ʀᴇᴘʟʏ ᴛᴏ ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ ᴛᴏ ᴀ ᴍᴇssᴀɢᴇ ᴛᴏ ʙʀᴏᴀᴅᴄᴀsᴛ (ʙᴏᴛ ᴏᴡɴᴇʀ ᴏɴʟʏ)</b>"""

    CHELP_TXT = """<b>💢 Hᴏᴡ Tᴏ Usᴇ Tʜɪs Bᴏᴛ ☺️

🔻 /link - ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴠɪᴅᴇᴏ ᴏʀ ғɪʟᴇ ᴛᴏ ɢᴇᴛ sʜᴀʀᴀʙʟᴇ ʟɪɴᴋ

🔻 /base_site - ᴜsᴇ ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ ᴛᴏ sᴇᴛ ᴜʀʟ sʜᴏʀᴛɴᴇʀ ʟɪɴᴋ ᴅᴏᴍᴀɪɴ
ᴇx - /base_site ʏᴏᴜʀᴅᴏᴍᴀɪɴ.ᴄᴏᴍ

🔻 /api - sᴇᴛ ʏᴏᴜʀ ᴜʀʟ sʜᴏʀᴛɴᴇʀ ᴀᴄᴄᴏᴜɴᴛ ᴀᴘɪ
ᴇx - /api ʏᴏᴜʀᴀᴘɪ

🔻 /broadcast - ʀᴇᴘʟʏ ᴛᴏ ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ ᴛᴏ ᴀ ᴍᴇssᴀɢᴇ ᴛᴏ ʙʀᴏᴀᴅᴄᴀsᴛ (ʙᴏᴛ ᴏᴡɴᴇʀ ᴏɴʟʏ)</b>"""

    LOG_TEXT = """<b>#NewUser
    
ID - <code>{}</code>

Name - {}</b>
"""
    RESTART_TXT = """
<b>Bᴏᴛ Rᴇsᴛᴀʀᴛᴇᴅ !

📅 Dᴀᴛᴇ : <code>{}</code>
⏰ Tɪᴍᴇ : <code>{}</code>
🌐 Tɪᴍᴇᴢᴏɴᴇ : <code>Asia/Kolkata</code>
🛠️ Bᴜɪʟᴅ Sᴛᴀᴛᴜs: <code>v2.7.1 [ Sᴛᴀʙʟᴇ ]</code></b>"""
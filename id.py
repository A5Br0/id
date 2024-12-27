from telethon import events

# Ваш клиент Telethon
from telethon.sync import TelegramClient

api_id = '20045757'
api_hash = '7d3ea0c0d4725498789bd51a9ee02421'

client = TelegramClient('session_name', api_id, api_hash)

@client.on(events.NewMessage(pattern=r'\.id', outgoing=True))
async def get_user_id(event):
    # Проверяем, есть ли сообщение, на которое вы ответили
    if event.is_reply:
        # Получаем сообщение, на которое вы ответили
        replied_msg = await event.get_reply_message()
        # Получаем ID пользователя
        user_id = replied_msg.sender_id
        await event.reply(f"ID пользователя: tg://user?id={user_id}")
    else:
        await event.reply("Ответьте на сообщение, чтобы получить ID пользователя.")

# Запуск клиента
client.start()
print("Бот запущен.")
client.run_until_disconnected()

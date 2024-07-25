import asyncio
from telethon import TelegramClient, events
from message import message  # Import the message function from message.py

# Your API credentials
api_id =   # Your API ID
api_hash = ''  # Your API hash

# Create the client and connect
client = TelegramClient('session_name', api_id, api_hash)

# Global variables to track detection and the word
found_44_char_word = False
word_to_send = ""

async def incoming_ca(message_text):
    global found_44_char_word, word_to_send
    words = message_text.split()
    for word in words:
        if len(word) == 44:
            word_to_send = word
            found_44_char_word = True
            return True
    return False

async def main():
    await client.start()

    @client.on(events.NewMessage(chats=-4225942572))  # Replace with your group ID
    async def handler(event):
        global found_44_char_word
        message_text = event.message.message
        if await incoming_ca(message_text):
            await client.disconnect()  # Disconnect after handling the message

    print("Listening for new messages...")
    await client.run_until_disconnected()

if __name__ == '__main__':
    asyncio.run(main())
    if found_44_char_word:
        message(word_to_send)  # Send the detected 44-character word

import asyncio
from telethon.sync import TelegramClient
from telethon.errors import PhoneNumberInvalidError, SessionPasswordNeededError

# Your API credentials
api_id = 00000000  # Your API ID
api_hash = '00000000000000000000000000000000'  # Your API hash

# Create the client
client = TelegramClient('session_name', api_id, api_hash)

async def send_message_to_user(client, message):
    user_id = 6886867782  # Hardcoded user ID
    try:
        await client.send_message(user_id, message)
        print(f"Message sent to user {user_id}: {message}")
    except PhoneNumberInvalidError:
        print("The phone number is invalid. Please check the format and try again.")
    except SessionPasswordNeededError:
        password = input("Two-step verification enabled. Please enter your password: ")
        await client.sign_in(password=password)
    except Exception as e:
        print(f"An error occurred: {e}")

async def main(message):
    async with client:
        await send_message_to_user(client, message)

def message(text):
    asyncio.run(main(text))

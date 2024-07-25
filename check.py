import asyncio
from telethon import TelegramClient
from telethon.errors import PhoneNumberInvalidError, SessionPasswordNeededError
from telethon.errors.rpcerrorlist import UserDeactivatedBanError

# Your API credentials
api_id = 00000000  # Your API ID
api_hash = '00000000000000000000000000000000'  # Your API hash
           
# Create the client
client = TelegramClient('session_name', api_id, api_hash)

async def check_login_status():
    try:
        # Attempt to start the client
        await client.connect()
        if not await client.is_user_authorized():
            raise UserDeactivatedBanError(request=None)
        print("You are already logged in.")
    except UserDeactivatedBanError:
        print("You need to log in.")
        await login()
    finally:
        await client.disconnect()

async def login():
    try:
        print("Starting client...")
        await client.start()
        print("Client started successfully.")
    except PhoneNumberInvalidError:
        print("The phone number is invalid. Please check the format and try again.")
    except SessionPasswordNeededError:
        password = input("Two-step verification enabled. Please enter your password: ")
        await client.sign_in(password=password)
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == '__main__':
    asyncio.run(check_login_status())

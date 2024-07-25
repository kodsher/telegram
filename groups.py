import asyncio
from telethon import TelegramClient
from telethon.errors import PhoneNumberInvalidError, SessionPasswordNeededError

# Your API credentials
api_id = 00000000  # Your API ID
api_hash = '00000000000000000000000000000000'  # Your API hash

# Create the client and connect
client = TelegramClient('session_name', api_id, api_hash)

async def list_groups():
    try:
        print("Starting client...")
        await client.start()
        print("Client started successfully.")
        
        print("Listing all groups:")
        async for dialog in client.iter_dialogs():
            if dialog.is_group:
                print(f'Group Name: {dialog.name}, Group ID: {dialog.id}')
            
    except PhoneNumberInvalidError:
        print("The phone number is invalid. Please check the format and try again.")
    except SessionPasswordNeededError:
        password = input("Two-step verification enabled. Please enter your password: ")
        await client.sign_in(password=password)
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        await client.disconnect()

# Run the function
if __name__ == '__main__':
    asyncio.run(list_groups())

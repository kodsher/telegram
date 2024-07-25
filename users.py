import asyncio
from telethon import TelegramClient
from telethon.errors import PhoneNumberInvalidError, SessionPasswordNeededError

# Your API credentials
api_id = 22022925  # Your API ID
api_hash = '0a2b4e19680dea65e7830bd2ede56154'  # Your API hash

# Create the client and connect
client = TelegramClient('session_name', api_id, api_hash)

async def list_group_users(group_id):
    try:
        print("Starting client...")
        await client.start()
        print("Client started successfully.")
        
        # Fetch the participants of the group
        participants = await client.get_participants(group_id)
        
        print(f"Listing all users in group {group_id}:")
        for participant in participants:
            name = f"{participant.first_name or ''} {participant.last_name or ''}".strip()
            print(f'User ID: {participant.id}, Name: {name}')
            
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
    group_id = -4225942572  # The group ID you provided
    asyncio.run(list_group_users(group_id))

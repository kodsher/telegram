import asyncio
from telethon.sync import TelegramClient
from telethon.errors import PhoneNumberInvalidError, SessionPasswordNeededError

# Your API credentials
api_id = 22022925  # Your API ID
api_hash = '0a2b4e19680dea65e7830bd2ede56154'  # Your API hash

# Create the client and connect
client = TelegramClient('session_name', api_id, api_hash)

async def send_message_to_user(message):
    user_id = 6886867782  # Hardcoded user ID
    try:
        print("Starting client...")
        await client.start()
        print("Client started successfully.")
        
        # Send a message to the user
        await client.send_message(user_id, message)
        print(f"Message sent to user {user_id}: {message}")
            
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
    message = input("Enter the message to send: ")
    asyncio.run(send_message_to_user(message))

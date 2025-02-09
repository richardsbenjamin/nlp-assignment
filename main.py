from model.chat_client import ChatClient
from config.config import (
    API_KEY,
    MODEL
)

if __name__ == "__main__":
    client: ChatClient = ChatClient(api_key=API_KEY, model=MODEL)
    client.chat_loop()
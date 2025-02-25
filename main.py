from config.config import API_KEY, MODEL
from model.chat_client import ChatClient

def main():
    client = ChatClient(api_key=API_KEY, model=MODEL)
    
    print("Chat initialized! Write 'stop' to leave.")
    
    while True:
        user_input = input("You: ").strip()
        if user_input.lower() == "stop":
            print("See ya!")
            break

        _, assistant_response = client.add_and_get_response("user", user_input)
        print(f"Mistral: {assistant_response}\n")

if __name__ == "__main__":
    main()

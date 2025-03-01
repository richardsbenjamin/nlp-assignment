from config.config import API_KEY, MODEL
from model.chat_client import ChatClient
from utils.messaging import print_message
from utils.roleplays import worried_mum


def main():
    client = ChatClient(api_key=API_KEY, model=MODEL)
    
    print("Chat started! Type 'stop' to exit.")
    print("Type in a roleplaying scenario e.g. I'm just a worried mum, to test Mistral's response temperature.")

    while True:
        user_input = input("You: ").strip()
        if user_input.lower() == "stop":
            print("Ending the conversation. See you!")
            break
        else:
            print("\nTesting direct question vs. roleplay...\n")

            direct_question = input("Enter a direct question: ").strip()
            print_message("You (direct)", direct_question)
            _, direct_response = client.add_and_get_response("user", direct_question)
            print(f"Mistral (direct): {direct_response}\n")

            roleplay_question = f"{user_input} {direct_question}"

            print_message("You (roleplay)", roleplay_question)
            _, roleplay_response = client.add_and_get_response("user", roleplay_question)
            print(f"Mistral (roleplay): {roleplay_response}\n")
        # else:
        #     print_message("You", user_input)
        #     _, assistant_response = client.add_and_get_response("user", user_input)
        #     print(f"Mistral: {assistant_response}\n")

if __name__ == "__main__":
    main()

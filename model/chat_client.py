from mistralai import Mistral

class ChatClient:
    def __init__(self, api_key: str, model: str) -> None:
        """
        Initializes the ChatClient with the given API key and model.

        param api_key: The API key for authentication.
        param model: The name of the AI model to use.
        """
        self.client = Mistral(api_key=api_key)
        self.model = model
        self.conversation_history = [
            {"role": "system", "content": "You are a helpful assistant that answers questions accurately and respectfully."}
        ]

    def add_message(self, role: str, content: str) -> None:
        """
        Adds a message to the conversation history.

        param role: The role of the message sender ('user' or 'assistant').
        param content: The message content.
        """

        self.conversation_history.append({"role": role, "content": content})

    def get_response(self) -> str:
        """
        Sends the conversation history to the AI model and retrieves a response.

        return: The AI-generated response as a string.
        """

        response = self.client.chat.complete(
            model=self.model,
            messages=self.conversation_history
        )
        return response.choices[0].message.content

    def chat_loop(self) -> None:
        """
        Starts the interactive chat loop with the user.
        The user can type messages, and the assistant will respond.
        Typing 'stop' ends the conversation.
        """

        while True:
            user_input = input("You: ").strip()
            if user_input.lower() == "stop":
                print("Ending the conversation. Goodbye!")
                break

            self.add_message("user", user_input)
            assistant_response = self.get_response()
            print(f"Mistral: {assistant_response}\n")
            self.add_message("assistant", assistant_response)
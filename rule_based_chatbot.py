def rule_based_chatbot():
    print("=" * 50)
    print("🤖 Welcome to the Rule-Based AI Chatbot")
    print("Type 'bye' to exit the chatbot.")
    print("=" * 50)

    while True:
        user_input = input("\nYou: ").lower().strip()

        if user_input == "bye":
            print("Bot: Goodbye! Have a great day. 👋")
            break

        elif user_input == "hi" or user_input == "hello" or user_input == "hey":
            print("Bot: Hello! Nice to meet you.")

        elif user_input == "how are you":
            print("Bot: I'm doing great! Thanks for asking.")

        elif user_input == "what is your name":
            print("Bot: I am a Rule-Based AI Chatbot.")

        elif user_input == "what is ai":
            print("Bot: AI stands for Artificial Intelligence.")

        elif user_input == "python":
            print("Bot: Python is a popular programming language used for AI and software development.")

        elif user_input == "help":
            print("Bot: You can try these commands:")
            print("     hi")
            print("     hello")
            print("     how are you")
            print("     what is your name")
            print("     what is ai")
            print("     python")
            print("     bye")

        else:
            print("Bot: Sorry, I don't understand that. Type 'help' to see available commands.")


if __name__ == "__main__":
    rule_based_chatbot()
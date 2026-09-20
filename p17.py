# python program for a simple chatbot 
def chatbot_response(user_input):
    # Define a dictionary of predefined responses
    responses = {
        "hello": "Hi there! How can I help you today?",
        "how are you": "I'm just a bot, but I'm doing great! How about you?",
        "what is your name": "I'm a simple chatbot created to assist you.",
        "bye": "Goodbye! Have a great day!",
    }
    # Convert user input to lowercase for case-insensitive matching
    user_input = user_input.lower()
    # Return the corresponding response or a default message
    return responses.get(user_input, "I'm sorry, I don't understand that.")


# Main function to run the chatbot
def main():
    print("Welcome to the simple chatbot! Type 'bye' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "bye":
            print("Chatbot: Goodbye! Have a great day!")
            break
        response = chatbot_response(user_input)
        print(f"Chatbot: {response}")

if __name__ == "__main__":
    main()
    
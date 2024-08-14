import random

# Define responses
responses = {
    "hi": ["Hello!", "Hi there!", "Hey!"],
    "how are you": ["I'm good, thank you!", "Feeling great!", "Pretty good."],
    "bye": ["Goodbye!", "See you later!", "Bye! Have a nice day!"],
    "default": ["I'm not sure what you mean...", "Could you please rephrase that?", "Sorry, I didn't understand."],
}

# Function to get response
def get_response(user_input):
    user_input = user_input.lower()
    if user_input in responses:
        return random.choice(responses[user_input])
    else:
        return random.choice(responses["default"])

# Main function
def main():
    print("Welcome to the ChatBot!")
    print("Type 'bye' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'bye':
            print(get_response(user_input))
            break
        else:
            print("Bot:", get_response(user_input))

if __name__ == "__main__":
    main()

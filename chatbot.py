import random

# Predefined responses
responses = {
    "greeting": ["Hi there!", "Hello!", "Hey! How can I help you?"],
    "how_are_you": ["I'm just code, but I'm doing great!", "All good! What about you?"],
    "name": ["I'm your mini chatbot 🤖", "You can call me ChatPy!"],
    "bye": ["Goodbye!", "See you later!", "Take care!"],
    "default": ["I didn't understand that 🤔", "Can you rephrase that?", "Interesting... tell me more!"]
}

def get_response(user_input):
    user_input = user_input.lower()

    if any(word in user_input for word in ["hi", "hello", "hey"]):
        return random.choice(responses["greeting"])
    
    elif "how are you" in user_input:
        return random.choice(responses["how_are_you"])
    
    elif "your name" in user_input:
        return random.choice(responses["name"])
    
    elif any(word in user_input for word in ["bye", "exit", "quit"]):
        return random.choice(responses["bye"])
    
    else:
        return random.choice(responses["default"])


def chat():
    print("🤖 Chatbot: Hello! Type 'bye' to exit.")
    
    while True:
        user_input = input("You: ")
        
        response = get_response(user_input)
        print("🤖 Chatbot:", response)
        
        if any(word in user_input.lower() for word in ["bye", "exit", "quit"]):
            break


if __name__ == "__main__":
    chat()
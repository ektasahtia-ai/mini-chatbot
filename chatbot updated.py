import random
import datetime

# Store user name
user_name = ""

# Responses
greetings = ["Hello!", "Hi there!", "Hey! 👋"]
how_are_you = [
    "I'm doing great 😄",
    "All good here!",
    "I'm just code, but I'm awesome 🤖"
]
jokes = [
    "Why do programmers hate nature? Too many bugs 🐛",
    "Why did Python go to school? To improve its class 🐍",
    "Programmers do it bit by bit 😆"
]
facts = [
    "Honey never spoils 🍯",
    "Python was named after Monty Python 😄",
    "The first computer bug was an actual bug 🐞"
]
motivation = [
    "You can do it 💪",
    "Keep coding and keep growing 🚀",
    "Every expert was once a beginner 🌟"
]

def chatbot_response(user_input):
    global user_name

    user_input = user_input.lower()

    # Greeting
    if any(word in user_input for word in ["hi", "hello", "hey"]):
        return random.choice(greetings)

    # How are you
    elif "how are you" in user_input:
        return random.choice(how_are_you)

    # Name
    elif "your name" in user_input:
        return "I'm ChatPy 🤖"

    # User name memory
    elif "my name is" in user_input:
        user_name = user_input.split("is")[-1].strip()
        return f"Nice to meet you, {user_name}! 😊"

    # Recall name
    elif "what is my name" in user_input:
        if user_name:
            return f"Your name is {user_name} 😄"
        else:
            return "I don't know your name yet!"

    # Time
    elif "time" in user_input:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        return f"Current time is {current_time} ⏰"

    # Joke
    elif "joke" in user_input:
        return random.choice(jokes)

    # Fact
    elif "fact" in user_input:
        return random.choice(facts)

    # Motivation
    elif "motivate" in user_input:
        return random.choice(motivation)

    # Mood detection
    elif "sad" in user_input:
        return "Don't worry, better days are coming ❤️"

    elif "happy" in user_input:
        return "That's awesome 😄"

    # Calculator
    elif "calculate" in user_input:
        try:
            expression = user_input.replace("calculate", "")
            result = eval(expression)
            return f"Answer: {result}"
        except:
            return "Invalid calculation!"

    # Exit
    elif any(word in user_input for word in ["bye", "exit", "quit"]):
        return "Goodbye! Have a great day 👋"

    # Default response
    else:
        return random.choice([
            "Interesting 🤔",
            "Tell me more!",
            "I didn't understand that 😅"
        ])


def chat():
    print("🤖 ChatPy Bot Started!")
    print("Type 'bye' to exit.\n")

    while True:
        user_input = input("You: ")

        response = chatbot_response(user_input)
        print("Bot:", response)

        if any(word in user_input.lower() for word in ["bye", "exit", "quit"]):
            break


# Run chatbot
if __name__ == "__main__":
    chat()
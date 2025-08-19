import random
import datetime
import math
import re

def get_greeting():
    current_hour = datetime.datetime.now().hour
    if current_hour < 12:
        return "Good morning! How can I assist you today?"
    elif 12 <= current_hour < 17:
        return "Good afternoon! What's on your mind?"
    else:
        return "Good evening! Ready to chat?"

def tell_joke():
    jokes = [
        "Why did the scarecrow become a programmer? Because he was outstanding in his field!",
        "Why don't eggs tell jokes? They'd crack up!",
        "What do you call a bear with no socks on? Barefoot!"
    ]
    return random.choice(jokes)

def calculate(expression):
    try:
        # Basic arithmetic evaluation
        result = eval(expression, {"__builtins__": {}}, {"math": math})
        return f"The result is {result}"
    except Exception:
        return "Sorry, I couldn't calculate that. Please use a valid mathematical expression."

def chatbot():
    print("Welcome to SimpleBot! Type 'help' for commands or 'exit' to quit.")
    print(get_greeting())
    
    commands = {
        "help": "Show available commands",
        "hello": "Greet the user",
        "time": "Show current time",
        "date": "Show current date",
        "joke": "Tell a random joke",
        "calc": "Calculate a mathematical expression (e.g., calc 2 + 3)",
        "uppercase": "Convert text to uppercase (e.g., uppercase hello world)",
        "lowercase": "Convert text to lowercase (e.g., lowercase HELLO WORLD)",
        "reverse": "Reverse text (e.g., reverse hello)",
        "count": "Count characters in text (e.g., count hello)",
        "weather": "Provide a mock weather update",
        "quote": "Share a random inspirational quote",
        "flip": "Flip a coin",
        "roll": "Roll a six-sided die",
        "fact": "Share a random fact",
        "echo": "Repeat your input (e.g., echo hi there)",
        "clear": "Clear the conversation",
        "exit": "Exit the chatbot"
    }
    
    conversation = []
    
    while True:
        user_input = input("You: ").strip().lower()
        conversation.append(f"You: {user_input}")
        
        # Split input to handle commands with arguments
        parts = user_input.split(maxsplit=1)
        command = parts[0] if parts else ""
        argument = parts[1] if len(parts) > 1 else ""
        
        if command == "exit":
            print("Goodbye! Thanks for chatting!")
            break
        elif command == "help":
            print("Available commands:")
            for cmd, desc in commands.items():
                print(f"{cmd}: {desc}")
        elif command == "hello":
            print(get_greeting())
        elif command == "time":
            current_time = datetime.datetime.now().strftime("%H:%M:%S")
            print(f"Current time is {current_time}")
        elif command == "date":
            current_date = datetime.datetime.now().strftime("%Y-%m-%d")
            print(f"Today's date is {current_date}")
        elif command == "joke":
            print(tell_joke())
        elif command == "calc" and argument:
            print(calculate(argument))
        elif command == "uppercase" and argument:
            print(argument.upper())
        elif command == "lowercase" and argument:
            print(argument.lower())
        elif command == "reverse" and argument:
            print(argument[::-1])
        elif command == "count" and argument:
            print(f"Character count: {len(argument)}")
        elif command == "weather":
            print("Today's weather: Sunny with a chance of smiles! (Note: This is a mock update.)")
        elif command == "quote":
            quotes = [
                "The only way to do great work is to love what you do. - Steve Jobs",
                "Stay hungry, stay foolish. - Steve Jobs",
                "Be the change you wish to see in the world. - Mahatma Gandhi"
            ]
            print(random.choice(quotes))
        elif command == "flip":
            result = random.choice(["Heads", "Tails"])
            print(f"Coin flip: {result}")
        elif command == "roll":
            result = random.randint(1, 6)
            print(f"Die roll: {result}")
        elif command == "fact":
            facts = [
                "Honey never spoils.",
                "Octopuses have three hearts.",
                "A group of flamingos is called a flamboyance."
            ]
            print(random.choice(facts))
        elif command == "echo" and argument:
            print(argument)
        elif command == "clear":
            conversation = []
            print("Conversation cleared!")
        else:
            print("Unknown command. Type 'help' for a list of commands.")
        
        conversation.append(f"Bot: {print.__self__}")
    
if __name__ == "__main__":
    chatbot()

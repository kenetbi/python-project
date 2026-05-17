# SIMPLE CHATBOT

import random

pairs = {
    "hello": "Hi there! How can I help you today?",
    "hi": "Hello! Nice to meet you.",
    "how are you": "I'm just a computer program, but I'm doing great! How are you?",
    "your name": "I am a simple Python chatbot created in VS Code.",
    "bye": "Goodbye! Have a wonderful day!"
}

is_chatting = True
chatbot = random.choice(["Hello Sir!", "Good to see you!", "Good day!"])

print(f"Chatbot: {chatbot}")
print("Chatbot: Type \"Bye\" to exit the chat.")

while is_chatting:
    user_input = input("You: ").lower().strip()
    if user_input == "bye":
        print(f"Chatbot: {pairs['bye']}")
        is_chatting = False
        break
    for key in pairs:
        if key in user_input:
            print(f"Chatbot: {pairs[key]}")
            break
    else:
        print(f"Chatbot: Sorry I don't have an answer for that yet.")
        print("Chatbot: I will direct you to the Customer Support for better assistance.")
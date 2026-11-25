# Simple rule-based chatbot using basic NLP text processing
import re

def respond(message):
    text = re.sub(r"[^a-zA-Z ]", "", message.lower()).strip()
    if any(word in text for word in ["hello", "hi", "hey"]):
        return "Hello! How can I help you?"
    if "name" in text:
        return "I am a simple Python chatbot."
    if "python" in text:
        return "Python is a popular programming language."
    if "help" in text:
        return "You can ask me about my name or Python."
    if any(word in text for word in ["bye", "exit"]):
        return "Goodbye!"
    return "Sorry, I did not understand. Please try another question."

print("Chatbot: Hello! Type 'bye' to stop.")
while True:
    user = input("You: ")
    answer = respond(user)
    print("Chatbot:", answer)
    if answer == "Goodbye!":
        break

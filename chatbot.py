import nltk
from nltk.chat.util import Chat, reflections

# Define pairs of patterns and responses
pairs = [
    ['my name is (.*)', ['Hi %1, how can I help you?']],
    ['(hi|hello|hey|hola)', ['Hello, how can I assist you?']],
    ['(.*) your name?', ["I'm just a simple chatbot."]],
    ['(.*) help (.*)', ['I can help you with various tasks. What do you need assistance with?']],
    ['(.*) (thank you|thanks)', ['You\'re welcome!']],
    ['(bye|goodbye|exit)', ['Goodbye! Have a great day!']],
    ['(how are you)', ['I am fine, thank you for asking!']],
    ['(what can you do)', ['I can help you with various tasks. Just ask!']],
    ['(what is your purpose)', ['My purpose is to assist you with any queries you have.']],
    ['(what time is it)', ['I am sorry, I cannot tell the time.']],
    ['(who created you)', ['I was created by OpenAI using Python.']],
    ['(what is the weather like today)', ['I am sorry, I cannot provide weather updates.']],
    ['(tera baap ke name kya )', ['Chup rah Because they make up everything!']],
    ['(tell me about yourself)', ['I am just a simple chatbot designed to assist you.']],
    ['(how old are you)', ['I am a chatbot, so I do not have an age.']],
    ['(where are you)', ['I exist in the virtual world.']],
    ['(do you have feelings)', ['I am just a program, so I do not have feelings.']],
]

# Create a Chatbot
def basic_chatbot():
    print("Bot: Welcome! Ask me anything or say 'bye' to exit.")
    chatbot = Chat(pairs, reflections)
    while True:
        user_input = input("You: ")
        response = chatbot.respond(user_input)
        print("Bot:", response)
        if user_input.lower() in ['bye', 'goodbye', 'exit']:
            break
 
if __name__ == "__main__":
    basic_chatbot()

# This is a simple chatbot program
# Getting started now !
# import required libraries
from nltk.chat.util import Chat, reflections

# Train the bot with patterns. In the absense of these patterns None will be the bot's response. And yes, don't irritate the bot ;)
training_patterns = [
    ['my name is (.*)', ['Hi %1']],
    ['(hi|hello|hey|holla|hola)', ['hey there !', 'hi there !', 'heyyy !']],
    ['(.*) in (.*) is fun', ['%1 in %2 is indeed fun !']],
    ['(.*)(localtion | city ) ?', 'Tokyo, Japan'],
    ['(.*) created you ?', ['rameshwarsingh11 did using nltk']],
    ['how is the weather in (.*) ?', ['The weather in %1 is amazing !']],
    ['(.*)help(.*)', ['I can help you for sure !']],
    ['how are you ?', ['I am doing good. Thanks for asking ! What about you ?']],
    ['(.*)also(.*)', ['I see.']]
]

# use reflection to help the bot with common passive responses like 'i am' - 'you are', 'i was' - 'you were' etc.
chat = Chat(training_patterns, reflections)
# let's chat with the bot now !
chat.converse()
# type quit to terminate the program.

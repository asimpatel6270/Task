import nltk
import random
import string
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize

# Sample conversation corpus
corpus = """
Hello! How can I help you?
Hi there!
What’s your name?
I’m a chatbot created using Python.
How are you?
I’m doing well, thank you!
What can you do?
I can have basic conversations with you.
Tell me a joke.
Why don’t scientists trust atoms? Because they make up everything!
Bye
Goodbye! Have a nice day!
"""

# Preprocess the text
sent_tokens = nltk.sent_tokenize(corpus.lower())  # Sentence tokenizer
lemmatizer = WordNetLemmatizer()

def preprocess(text):
    tokens = word_tokenize(text.lower())
    return [lemmatizer.lemmatize(token) for token in tokens if token not in string.punctuation]

# Generate response
def get_response(user_input):
    user_tokens = preprocess(user_input)
    max_score = 0
    response = "I didn’t understand that. Can you rephrase?"

    for sentence in sent_tokens:
        sentence_tokens = preprocess(sentence)
        common_words = set(user_tokens).intersection(set(sentence_tokens))
        score = len(common_words)

        if score > max_score:
            max_score = score
            response = sentence

    return response.capitalize()

# Chat loop
print("Chatbot: Hello! Type 'bye' to exit.")
while True:
    user_input = input("You: ").strip()
    if user_input.lower() == 'bye':
        print("Chatbot: Goodbye!")
        break
    print("Chatbot:", get_response(user_input))

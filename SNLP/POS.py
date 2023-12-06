# Parts of Speech
import nltk
from nltk import pos_tag
from nltk.tokenize import word_tokenize

nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

def pos_tagging(text):
    words = word_tokenize(text)
    tagged_words = pos_tag(words)
    return tagged_words

# Example usage
sentence = "Parts of speech tagging is an important NLP task."
tags = pos_tagging(sentence)
print(tags)
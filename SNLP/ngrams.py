# N-Grams
import nltk
nltk.download('punkt')
from nltk import ngrams

def generate_ngrams(text, n):
    words = nltk.word_tokenize(text)
    ngrams_result = list(ngrams(words, n))
    return ngrams_result

# Example usage:
text = input("Enter a sentence: ")
n = int(input("Enter the value of n: "))

result = generate_ngrams(text, n)

print(f"{n}-grams:")
for gram in result:
    print(gram)
def remove_numbers(sentence):
    sentence_without_numbers = ''.join(char for char in sentence if not char.isdigit())
    return sentence_without_numbers

# Example usage
original_sentence ="HI 1234,  I am Studying in ngit btech 3rd year 5th sem."
sentence_without_numbers = remove_numbers(original_sentence)

print("Original Sentence: ", original_sentence)
print()
print("Sentence without Numbers: ", sentence_without_numbers)
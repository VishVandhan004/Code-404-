print("SENTENCE WITH NUMBERS AND STRINGS")
def remove_numbers(sentence):
    sentence_without_numbers = ''.join(char for char in sentence if not char.isdigit())
    return sentence_without_numbers

# Example usage
original_sentence ="HI 1234,I am Studying in ngit btech 3rd year 5th sem."
sentence_without_numbers = remove_numbers(original_sentence)
print("Original Sentence: ", original_sentence)
print()
print("Sentence without Numbers: ", sentence_without_numbers)
print("REMOVING THE SPACES")
# inputting a string
str = input()
# It is used to remove the spaces and return the new string
str = str.replace(" ","")
print(str)
print("CONVERSION INTO LOWER CASE")
# Converts the whole string into lower case
print(str.lower())
print("CAPATILIZING 1st LETTER")
# Capitalizes the first letter of the string
print(str.capitalize())
print("CONVERSION INTO  UPPER CASE")
# Converts everything into upper case
print(str.upper())

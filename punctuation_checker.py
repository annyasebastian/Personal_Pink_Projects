import string

print(f"Punctuations are any of the following: {string.punctuation}")

def contains_punctuation(input_str):
    ''' Return True if the input_str contains punctuations.
    Return False otherwise'''
    return any(char in string.punctuation for char in input_str)

import string

print(f"Punctuations are any of the following: {string.punctuation}")

def contains_punctuation(input_str):
    ''' Return True if the input_str contains punctuations.
    Return False otherwise'''
    return any(input_str[i] in string.punctuation for i in range(0,len(input_str)))

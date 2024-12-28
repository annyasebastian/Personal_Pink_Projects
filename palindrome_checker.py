import re

def remove_punctuation(words):
    '''Helper function to return a string, removing all punctuations and spaces'''
    return re.sub('\W+', '', words)

def is_palindrome(words):
    reversed_words = ''.join(reversed(words))
    reversed_words_cleaned = remove_punctuation(reversed_words.lower())
    words_cleaned = remove_punctuation(words.lower())
    return reversed_words_cleaned == words_cleaned

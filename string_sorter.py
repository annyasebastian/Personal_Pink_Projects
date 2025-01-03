def sort_words(string):
    return sorted(string.split(), key = str.casefold)

# ------- test code -------
print(sort_words('banana ORANGE apple')) # expected output : ['apple', 'banana', 'ORANGE']
print(sort_words('A Kangaroo hapPily jumped like FIRE but interesTingly Cat danced good everyday')) # expected output : ['A', 'but', 'Cat', 'danced', 'everyday', 'FIRE', 'good', 'hapPily', 'interesTingly', 'jumped', 'Kangaroo', 'like']

def findWordsContaining(words, x):
    res = [i for i, word in enumerate(words) if x in word]
    return res

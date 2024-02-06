def truncateSentence(s, k):
    sentence = s.split(" ")
    return ' '.join(sentence[0:k])

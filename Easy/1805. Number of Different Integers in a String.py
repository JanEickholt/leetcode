def numDifferentIntegers(word):
    return len(set(w.lstrip('0') for w in ''.join(c if c.isdigit() else ' ' for c in word).split()))

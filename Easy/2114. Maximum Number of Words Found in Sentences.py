def mostWordsFound(sentences):
    return max(s.count(' ') for s in sentences) + 1

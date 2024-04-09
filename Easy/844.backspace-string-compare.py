def backspaceCompare(s, t):
    word1 = []
    word2 = []
    for i in s:
        if i == "#":
            if word1:
                word1.pop()
        else:
            word1.append(i)
    for i in t:
        if i == "#":
            if word2:
                word2.pop()
        else:
            word2.append(i)
    return word1 == word2

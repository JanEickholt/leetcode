def reversePrefix(word, ch):
    if ch not in word:
        return word

    i = word.index(ch)
    word = word[i::-1] + word[i + 1:]
    return word

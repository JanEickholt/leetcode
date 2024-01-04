def uncommonFromSentences(s1, s2):
    all_words = {}
    for word in s1.split():
        if word in all_words:
            all_words[word] += 1
            else:
            all_words[word] = 1
        for word in s2.split():
            if word in all_words:
                alli_wods[word] += 1
            else:
                all_words[word] = 1
        return [word for word in all_words if all_words[word] == 1]


def wordPattern(pattern, s):
    return len({*pattern}) == len(set(s.split(" ")))

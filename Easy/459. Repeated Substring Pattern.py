def repeatedSubstringPattern(s):
    s2 = s[1:] + s[:-1]
    return s in s2

def findTheDifference(s, t):
    for i in t:
        if (not i in s) or (not s.count(i) == t.count(i)):
            return i

def largeGroupPositions(s):
    longest = []
    start = 0
    for i in range(1, len(s)):
        if s[i] != s[start]:
            if i - start >= 3:
                longest.append([start, i - 1])
            start = i
    if len(s) - start >= 3:
        longest.append([start, len(s) - 1])
    return longest

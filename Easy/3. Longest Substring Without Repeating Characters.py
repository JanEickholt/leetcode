def lengthOfLongestSubstring(s):
    max_chars = 0
    visited_chars = {}

    i = 0
    for j in range(len(s)):
        if s[j] in visited_chars:
            i = max(visited_chars[s[j]], i)
        max_chars = max(max_chars, j - i + 1)
        visited_chars[s[j]] = j + 1

    return max_chars

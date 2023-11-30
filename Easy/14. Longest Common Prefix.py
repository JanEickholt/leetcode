def longestCommonPrefix(self, strs):
    result = ""
    for chars in zip(*strs):
        if len(set(chars)) == 1:
            result += chars[0]
        else:
            break
    return result

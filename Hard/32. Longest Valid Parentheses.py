def longestValidParentheses(s):
    curr = [-1]
    max_len = 0
    for index, char in enumerate(s):
        if char == "(":
            curr.append(index)
        else:
            if len(curr) == 1:
                curr[0] = index
            else:
                curr = curr[:-1]
                max_len = max(max_len, index - curr[-1])
    return max_len

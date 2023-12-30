def generateParenthesis(n, cnt=0):
    if n > 0 <= cnt:
        return ['(' + p for p in generateParenthesis(n-1, cnt+1)] + \
               [')' + p for p in generateParenthesis(n, cnt-1)]
    return [')' * cnt] * (not n)


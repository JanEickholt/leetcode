def isValid(self, s):
    used_brackets = []
    brackets = {
        '(': ')',
        '{': '}',
        '[': ']'
    }
    for bracket in s:
        if bracket in brackets:
            used_brackets.append(bracket)
        elif len(used_brackets) == 0 or bracket != brackets[used_brackets.pop()]:
            return False

    return len(used_brackets) == 0

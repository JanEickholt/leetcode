def isNumber(s):
    valid = False

    e = False
    e_sign = False

    dot = False

    for idx, ch in enumerate(s):
        if idx == 0:
            if ch in ["+", "-"]:
                continue
                if ch == '.':
                    dot = True
                    continue
                if ch.isnumeric():
                    valid = True
                    continue
                return False

            if ch == 'e':
                if e:
                    return False
                if not valid:
                    return False

                e = True
                valid = False

            if ch in ["+", "-"]:
                if not e:
                    return False
                if e_sign:
                    return False
                e_sign = True
                valid = False
                continue

            if ch.isnumeric():
                valid = True
                continue

            if ch == '.':
                if dot:
                    return False
                dot = True
                continue

            return False

        return valid

print(isNumber("2e0"))

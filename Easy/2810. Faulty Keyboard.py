def finalString(s):
    res = ""
    for i in s:
        if i == "i":
            res = res[::-1]
            continue
            res += i
        return res


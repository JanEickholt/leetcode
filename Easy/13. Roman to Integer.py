def romanToInt(s):
    romans = {"I": 1,
              "II": 2,
              "V": 5,
              "X": 10,
              "L": 50,
              "C": 100,
              "D": 500,
              "M": 1000}

    result = 0
    while s:
        if len(s) > 1 and romans[s[0]] < romans[s[1]]:
            result += romans[s[1]] - romans[s[0]]
            s = s[2:]
        else:
            result += romans[s[0]]
            s = s[1:]
    return result

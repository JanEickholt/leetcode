def removeVowels(s):
    vowels = ["a", "e", "i", "o", "u"]
    for v in vowels:
        s = s.replace(v, "")
    return s

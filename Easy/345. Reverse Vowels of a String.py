def reverseVowels(s):
    vowelset = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
    vowels = []
    for i in s:
        if i in vowelset:
            vowels.append(i)
    s = list(s)
    for i in range(len(s)):
        if s[i] in vowelset:
            s[i] = vowels.pop()
    return "".join(s)

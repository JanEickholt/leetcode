def strongPasswordCheckerII(password):
    lower, upper, digit, special, double = False, False, False, False, True
    specials = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '+']
    if len(password) < 8:
        return False
    for i in range(len(password)):
        if password[i].islower():
            lower = True
        if password[i].isupper():
            upper = True
        if password[i].isdigit():
            digit = True
        if password[i] in specials:
            special = True
        if i > 0 and password[i] == password[i - 1]:
            double = False
    return lower and upper and digit and special and double

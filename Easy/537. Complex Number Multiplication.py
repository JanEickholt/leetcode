def complexNumberMultiply(num1, num2):
    a = int(num1[0:num1.index("+")])
    b = int(num1[num1.index("+") + 1:-1])
    c = int(num2[0:num2.index("+")])
    d = int(num2[num2.index("+") + 1:-1])
    r1 = (a * c) - (b * d)
    r2 = (a * d) + (b * c)
    res = str(r1) + "+" + str(r2) + "i"
    return res

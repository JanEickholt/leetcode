def convertToBase7(num):
    if num < 0:
        return '-' + convertToBase7(-num)
    if num < 7:
        return str(num)
    return convertToBase7(num // 7) + str(num % 7)

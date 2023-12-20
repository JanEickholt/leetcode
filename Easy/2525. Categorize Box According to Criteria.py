def categorizeBox(length, width, height, mass):
    if length >= 10000 or width >= 10000 or height >= 10000 or length * width * height >= 1000000000:
        if mass >= 100:
            return "Both"
        else:
            return "Bulky"
    elif mass >= 100:
        return 'Heavy'
    else:
        return 'Neither'

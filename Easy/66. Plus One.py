def plusOne(digits):
    for idx in range(len(digits) - 1, -1, -1):
        if digits[idx] != 9:
            digits[idx] += 1
            return digits
        else:
            digits[idx] = 0

    return [1] + digits

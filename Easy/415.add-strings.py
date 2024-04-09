class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        res = ""
        carry = 0
        num1 = num1[::-1]
        num2 = num2[::-1]
        smaller = min(len(num1), len(num2))
        for i in range(smaller):
            carry, curr_sum = divmod(int(num1[i]) + int(num2[i]) + carry, 10)
            res += str(curr_sum)
        if len(num1) > len(num2):
            for i in range(smaller, len(num1)):
                carry, curr_sum = divmod(int(num1[i]) + carry, 10)
                res += str(curr_sum)
        else:
            for i in range(smaller, len(num2)):
                carry, curr_sum = divmod(int(num2[i]) + carry, 10)
                res += str(curr_sum)
        if carry:
            res += str(carry)
        return res[::-1]

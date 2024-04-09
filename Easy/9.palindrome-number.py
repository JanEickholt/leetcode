class Solution:
    def isPalindrome(self, x: int) -> bool:
        if isinstance(x, int):
            str_x = str(x)
            for i in range(len(str_x) // 2):
                if str_x[i] != str_x[-i - 1]:
                    return False
            return True
        return False

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        reversed_num = 0
        num = x
        while x:
            print(x)
            reversed_num = reversed_num * 10 + x % 10
            x //= 10
            print(reversed_num)

        return reversed_num == num

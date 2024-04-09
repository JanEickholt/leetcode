class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        res = []
        for num in range(left, right + 1):
            for char in str(num):
                if char == "0":
                    break
                if num % int(char) != 0:
                    break
            else:
                res.append(num)

        return res

class Solution:
    def cellsInRange(self, s: str) -> List[str]:
        res = []
        for letter in range(ord(s[0]), ord(s[3]) + 1):
            for num in range(int(s[1]), int(s[4]) + 1):
                res.append(chr(letter) + str(num))

        return res

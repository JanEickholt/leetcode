class Solution:
    def reverse(self, x: int) -> int:
        signed = False
        if x < 0:
            signed = True

        x = str(x)
        if signed:
            x = x[:0:-1]
            x = "-" + x
        else:
            x = x[::-1]

        x = int(x)
        if x > 2 ** 31 or x < -2 ** 31:
            return 0

        return x
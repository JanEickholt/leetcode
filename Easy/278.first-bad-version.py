class Solution:
    def firstBadVersion(self, n: int) -> int:
        current = n
        first = 1
        last = n
        while first < last:
            if isBadVersion(current):
                last = current
            else:
                first = current + 1
            current = (first + last) // 2

        return first

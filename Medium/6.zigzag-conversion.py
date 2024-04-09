class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        rows = [[] for _ in range(numRows)]
        idx = 0
        row = 0
        while idx < len(s):
            while row < numRows and idx < len(s):
                rows[row].append(s[idx])
                row += 1
                idx += 1
                print(rows)

            row = numRows - 2
            while row >= 0 and idx < len(s):
                rows[row].append(s[idx])
                row -= 1
                idx += 1
                print(rows)

            row = 1

        result = ""
        for row in rows:
            result += "".join(row)

        return result

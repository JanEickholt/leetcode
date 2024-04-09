class Solution:
    def categorizeBox(self, length: int, width: int, height: int, mass: int) -> str:
        if length >= 10000 or width >= 10000 or height >= 10000 or length * width * height >= 1000000000:
            if mass >= 100:
                return "Both"
            else:
                return "Bulky"
        elif mass >= 100:
            return 'Heavy'
        else:
            return 'Neither'

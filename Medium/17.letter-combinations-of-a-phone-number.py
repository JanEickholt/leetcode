class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        letter_dict = {"2":"abc", "3":"def", "4":"ghi", "5":"jkl", "6":"mno", "7":"pqrs", "8":"tuv", "9":"wxyz"}
        digit_len = len(digits)
        if(digit_len==0):
            return []
        if(digit_len==1):
            return [a for a in letter_dict[digits]]
        if(digit_len==2):
            return [a+b for a in letter_dict[digits[0]] for b in letter_dict[digits[1]]]
        if(digit_len==3):
            return [a+b+c for a in letter_dict[digits[0]] for b in letter_dict[digits[1]] for c in letter_dict[digits[2]]]
        return [a+b+c+d for a in letter_dict[digits[0]] for b in l[digits[1]] for c in letter_dict[digits[2]] for d in letter_dict[digits[3]]]


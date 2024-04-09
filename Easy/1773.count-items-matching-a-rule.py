class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        cnt = 0
        for item in items:
            product = {"type": item[0], "color": item[1], "name": item[2]}
            if product[ruleKey] == ruleValue:
                cnt += 1

        return cnt

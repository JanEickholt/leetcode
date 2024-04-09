class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        possible_combinations = [[] for k in range(target + 1)]

        for c in candidates:
            for k in range(c, target + 1):
                if k == c:
                    possible_combinations[k].append([c])
                else:
                    for li in possible_combinations[k - c]:
                        possible_combinations[k].append(li + [c])
        return possible_combinations[-1]

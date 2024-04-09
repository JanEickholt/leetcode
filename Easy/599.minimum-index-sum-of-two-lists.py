class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        data = {i: list1.index(i) + list2.index(i) for i in set(list1) & set(list2)}
        return [e for e in data if data[e] == min(data.values())]

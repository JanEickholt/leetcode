def findRestaurant(list1, list2):
    data = {i: list1.index(i) + list2.index(i) for i in set(list1) & set(list2)}
    return [e for e in data if data[e] == min(data.values())]

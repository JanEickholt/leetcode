def mergeTwoLists(list1, list2):
    if not list1:
        return list2
    if not list2:
        return list1
    value, value2 = (list1, list2) if list1.val < list2.val else (list2, list1)
    sorted_list = value
    while value and value2:
        while value.next and value.next.val < value2.val:
            value = value.next
        value.next, value2 = value2, value.next
        value = value.next
    return sorted_list
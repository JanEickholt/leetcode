def reverseList(self, head):
    reversed_link = None
    element_list = head

    while element_list:
        next_node = element_list.next
        element_list.next = reversed_link
        reversed_link = element_list
        element_list = next_node

    return reversed_link

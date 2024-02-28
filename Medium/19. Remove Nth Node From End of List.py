def removeNthFromEnd(head, n):
    copy = ListNode(0)
    copy.next = head
    end = copy
    running = copy

    for _ in range(n + 1):
        end = end.next

    while end is not None:
        end = end.next
        running = running.next

    running.next = running.next.next

    return copy.next

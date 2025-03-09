'''
Given the head of a singly linked list and two integers left and right where left <= right, reverse the nodes of the list from position left to position right, and return the reversed list.
'''

class ListNode():
    pass


def solve(head, left, right):
    dummy = ListNode(0)
    dummy.next = head
    slow = dummy

    for _ in range(left):
        slow = slow.next
    fast = dummy
    for _ in range(right):
        fast = fast.next
    
    
    # now slow.next = first part of linked list we want to reverse

    prev = slow
    prev2 = slow
    slow = slow.next
    for r in range(right - left):
        temp = slow.next
        slow.next = prev
        prev = slow
        slow = temp
    prev2.next = fast.next
    return dummy.next


    
    

'''
medium

'''
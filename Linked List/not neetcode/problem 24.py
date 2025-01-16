'''
Given a linked list, swap every two adjacent nodes and return its head. You must solve the problem without modifying the values in the list's nodes (i.e., only nodes themselves may be changed.)
'''
class ListNode():
    pass


def solve(head):
    curr = head
    if not curr:
        return []
    if not curr.next: # 1 element
        return head
    
    slow = curr
    fast = curr.next
    prev = slow
    while fast is not None:
        fast_next = fast.next
        fast.next = prev # reverse the direction
        fast = fast_next
        slow = slow.next
    return head
        


'''
just go through with a fast and slow pointer
'''
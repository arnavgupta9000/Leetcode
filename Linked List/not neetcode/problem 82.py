'''
Given the head of a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list. Return the linked list sorted as well.
'''
class ListNode():
    pass

def solve(head):
    if not head:
        return None
    dummy = ListNode(0)
    hash = {}

    curr = head
    while curr:
        hash[curr.val] = hash.get(curr.val, 0) + 1
        curr = curr.next
    slow = dummy
    fast = head
    while fast:
        if hash[fast.val] == 1:
            slow.next = ListNode(fast.val)
            slow = slow.next

        print(dummy)
        
        fast = fast.next
            

    return dummy.next

'''
med

just use a hash and a fast and then just chuck all of em. use a dummy to store the head tho. on my own but to slow, wanna look at the faster sol later
'''
'''
Given the head of a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list. Return the linked list sorted as well.
'''
class ListNode():
    pass

def solve(head): # check below
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

def solve2(head):
    dummy = ListNode(0, head)
    prev = dummy

    while head:
        while head.next and head.val == head.next.val: # skips dups
            head = head.next
        if prev.next == head: # this is saying if we are at 2,3 and prev at 2 and 3 is head, since prev.next == head, its not a dup so keep it
            prev = prev.next 
        else: # this is saying that if we had that prev case but now like 2, 1, 1, 3 we see that head is at 3 prev at 1 thus prev.next != head, thus prev.next = head.next
            prev.next = head.next
        head = head.next

    return dummy.next

'''
med

just use a hash and a fast and then just chuck all of em. use a dummy to store the head tho. on my own but to slow, wanna look at the faster sol later
'''
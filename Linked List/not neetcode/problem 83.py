'''
Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.
 
'''

class ListNode():
    pass


def solve(head):
    dummy = ListNode(0)
    dummy.next = head
    slow = dummy
    fast = head
    while fast:
        slow.next = fast # this will always make sure we get the first occurance and then skip the rest below
        slow = slow.next 
        while fast.next and fast.val == fast.next.val:
            fast = fast.next # skip all dups now that we have the first one
        slow.next = fast.next
        fast = fast.next


    return dummy.next

def solve2(head): # faster sol or ig not? idk lol screw lc times. just use solve^^
    curr = head

    while curr:
        while curr.next and curr.val == curr.next.val:
            curr.next = curr.next.next
        curr = curr.next
    return head

'''
easy problem

well i got it right away yay!
'''
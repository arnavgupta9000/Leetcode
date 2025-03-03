'''
You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.
'''
class ListNode():
    pass

def solve(l1, l2):
    def combine(l1,l2):
        dummy = ListNode()
        curr = dummy
        while l1 and l2:
            if l1.val < l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next
            curr = curr.next
        
        if l1:
            curr.next = l1
        if l2:
            curr.next = l2

        return dummy.next

    if not lists:
        return None
    
    n = len(lists)
    
    res = []
    while len(lists) > 1:
        merged = []

        for i in range(0, len(lists), 2):
            l1 = lists[i]
            l2 = lists[i+1] if i + 1 < len(lists) else None

            merged.append(combine(l1,l2))
        lists = merged
    return lists[0]



'''
hard problem
'''
# merge two sorted lists
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def solve(l1, l2):
    dummy = ListNode(0)
    temp = dummy

    while l1 and l2:
        if l1.val < l2.val:
            temp.next = l1
            l1 = l1.next
        else:
            temp.next = l2.next
            l2 = l2.next
        temp = temp.next
    
    if l1:
        temp.next = l1
    
    if l2: 
        temp.next = l2
    
    return dummy.next

# the dummy node is just any node to start the linked list. we need it basically to make handling edge cases easier
# the temp var actually traverses through the linked list, but the dummy stays at the head of the new linked list essentially so we will return that, but we have random node at pos 0 of the linked list so we drop that by dummy.next
#then we compare values and see what is lower and then add that node itself to our new linked list. we then move that list over to the next element and we do the same for temp after every iteration of the loop since a new value either from l1 or l2 was put there
# once the while statement ends either l1 or l2 is not empty. if l1 is not empty then just add the remaining nodes to temp. or if l2 is not empty same thing but flipped

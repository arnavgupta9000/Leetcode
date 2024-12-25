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

# notice that we add the entire linked list of l1/l2 at lines 13/17, but then its overwritten in the next iteration of the loop. ie when we do temp.next = l1, it does point to l1 currently but then temp.next then points to l1.next, but then we overwrite temp.next essientally overwriting l1.next as well.
'''
When Should You Use a Dummy Node?
You should consider using a dummy node in problems where:

You Need to Build a New Linked List:
If the result involves dynamically adding nodes to a new list, a dummy node can help manage the head pointer.
Examples: Merging lists, removing duplicates, or adding two numbers represented as linked lists.
There's No Initial Starting Node:
If you don't already have a clear head node for the result (e.g., when merging), a dummy node simplifies initialization.

When we do temp = l1 or temp = l2, we're not modifying the structure of the linked list. Instead, we're just reassigning the temp pointer to point to the node that l1 or l2 points to. This breaks the connection between the previously constructed list and the new node.


'''
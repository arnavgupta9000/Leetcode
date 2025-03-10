#Given the head of a linked list, remove the nth node from the end of the list and return its head

class ListNode():
    pass
def solve(head, n):
        dummy = ListNode(0) # helps dealing with edge cases like removing at the start of the list
        dummy.next = head # make the next pointer of dummy equal to the head. this now makes dummy the new starting point of the list


        
        left = dummy
        right = dummy

        for _ in range(n+1): # this makes the gap of 'n' nodes between the first and second pointers. we need n+1 since both nodes start at dummy (and head is techically the first element in the list so we need to account for that hence the n+1)

            right = right.next
        '''
        left= dummy
        right = dummy.next
        while n > 0 and right: # this creates a gap of n spaces as well 
            right = right.next
            n-=1
        '''
        
        while right is not None:
            left = left.next
            right = right.next
        
        # delete the node
        left.next = left.next.next # the reason this line works is because of the following
        '''
        1 -> 2 -> 3 -> 4 -> 5 n=1
        then we get l=1, r=3. then l=2, r=4. then l=3, r=5. r is still not None so keep going. then we get l=4, r=None. now l=4 is right before the node we want to delete
        now left.next = last node. but left.next.next = last node.next = None. thus for edge cases we will always get none which is why this works.
        '''

        return dummy.next

def solve2(l1, l2): # must more optimized
    dummy = ListNode(0)
    curr = dummy
    carry = 0
    while l1 or l2 or carry:
        val1 = l1.val if l1 else 0
        val2 = l2.val if l2 else 0

        res = val1 + val2 + carry
        carry = (res // 10)
        value = (res % 10)
        curr.next = ListNode(value)
        curr = curr.next

        if l1:
            l1 = l1.next
        if l2:
            l2 = l2.next
    return dummy.next
     


    
            


'''
couldnt solve...
one way is to reverse the list, and then just remove the n'th first element. then reverse back

but easier way is init 2 pointers, one at the start of the list(left) and the other 'n' away from the start(right). then when the right pointer reaches null, the left pointer is exactly where we want to delete the node. but we want to remove this node not be at it, ie we want to be at one node before this, so we can make a dummy node first at the start of the list to achieve this. this is only a one pass solution so the time is O(n) 

'''
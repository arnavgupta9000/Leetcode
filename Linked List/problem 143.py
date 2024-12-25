# 143. Reorder List
# notice this is singly linked list not double linked list
'''
You may not modify the values in the list's nodes. Only nodes themselves may be changed.
You are given the head of a singly linked-list. The list can be represented as:

L0 → L1 → … → Ln - 1 → Ln
Reorder the list to be on the following form:

L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
You may not modify the values in the list's nodes. Only nodes themselves may be changed.
'''

def solve1 (head):
    
    curr = head

    len = 0 # just for the length of the nodes
    while curr:
        len +=1
        curr = curr.next
    
    
    curr = head # reset curr

    while curr:
        # swtich curr.next = node n
        curr2 = curr # start at curr

    # idk at this point... im not to sure



'''
medium problem so going to start writing my thoughts and process before i see the answer
thinking that an O(n^2) solution is definetly possible by doing a outer loop for nodes 1,2... and the inner loops for nodes n, n-1... but this seems like a lot of extra work
can also see it might be different if the length of the linked list is odd or even
not sure... so gonna see an explanation
'''

# idea given from video : store the nodes in an array and use 2 pointers

def solve(head):
    arr = []
    curr = head
    while curr:
        arr.append(curr)
        curr = curr.next
    
    # now the entire linked list is stored in an arry use 2 pointer now

    curr = head #reset curr
    r = len(arr) - 1
    l=0
    t = True
    while l <= r: # while l <= len(arr)//2 also works
        if t:
            # add from spot 'l'
            curr.next = arr[l]
            l +=1            
        else:
            # add from spot 'r'
            curr.next = arr[r]
            r -=1
        curr = curr.next
        t = not t
    curr.next = None
    return head

'''
ok so after getting to the 2 pointer approach i basically had the right solution except for 2 key differences that made it not work 
1. on line 56 i had 'while l < len(arr) // 2'
2. on like 59 and 63 i had 'curr=arr[l]' or r.

for 1 just change to while l <= len(arr) // 2

for 2 even in problem 21 i had to do ".next" when using the temp var. the reason we need this .next and not just curr = arr[l] is because with this .next we are actually changing the links inside head. otherwise we just remap the var 'curr' to arr[l] but this does nothing for us. this is just a standard practice that again happened in the last problem as well but i didnt think to much about it. note that the inital node is not skipped.

First Iteration:

Since curr points to Node 1 (the first node), curr.next = arr[l] modifies the next pointer of Node 1.
When l = 0, arr[l] is still Node 1, so setting curr.next = arr[l] doesn't change anything yet (Node 1's next pointer remains as it was).
'''

# can solve it using O(1) memory but... im good 

'''
slow and fast pointers
slow = start at pos 0, increment 1
fast = start at pos 1, increment 2
once fast at last node or greater than last node, if the list is even the next node that slow points to, starts the second half of the list
if the list is odd, it is exactly at the half way point (ie the node it sits on is the half way point)
'''

def solve1(head):
    curr = head
    slow, fast = head, head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    
    # we have the midpoint with slow.next
    second = slow.next
    slow.next = None # need this to effectively break the list into 2 (was the issue)

    # now reverse the second half
    prev = None
    while second is not None:
        temp = second.next
        second.next = prev
        prev = second
        second = temp
    
    # now the list is reversed
    first, second = head, prev
    while second: # since second will be the smaller list always
        # store curr.next and prev.next
        temp1, temp2 = first.next, second.next
        first.next = second
        second.next = temp1 # assigning the second pointer INBETWEEN the 2 first elements
        first, second = temp1, temp2
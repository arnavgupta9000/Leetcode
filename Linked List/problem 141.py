
def solve(head):
    end = 10 ** 4 + 1
    i=0
    while head is not None:
        if i >=end:
            return True
        head = head.next
        i+=1
    return False

def solv1(head):
    slow, fast = head, head

    while fast and fast.next is not None: # make sure fast does not reach the end of the linked list, we do fast.next since we are moving fast twice ie if fast.next.next is None then if fast.next = None, it works so we return false, if fast.next != None, then if we get to none now, the while "fast" catches it since fast = None now.

        slow = slow.next
        fast= fast.next.next

        if slow == fast:
            return True
    return False



'''
Intution is well... basically if we go over the max number of nodes and were not out of the while loop there is a cycle.
this method is kinda cheesy i mean it worked (without ANY help)

but we can also try a 2 pointer approach the fast and slow pointer


the reason its O(n) is since if fast and slow are n length away, then when we move, slow = n+1, fast = n-2. ie slow moves 1 further away from fast and fast moves 2 closer to slow. thus we get new_distance = distance (n) + slow - fast = n + (n+1 - (n+2)) = n+ (-1) n -1. so were always getting 1 step closer
'''
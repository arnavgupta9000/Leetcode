# invert linked list
# got it bymyself except returning prev and not head
def solve(head):
    prev = None
    while head:
        temp = head.next
        head.next = prev
        prev = head
        head = temp
    return prev

# we need to return prev here because our head is now at None at the end of the linked list. hence prev points to the last node
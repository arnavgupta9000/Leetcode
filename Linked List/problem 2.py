#You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

#You may assume the two numbers do not contain any leading zero, except the number 0 itself.

class ListNode():
    pass

def solve(l1, l2):
    num1 = ''
    num2 = ''
    head = l1

    while l1 is not None:
        num1 += str(l1.val)
        l1 = l1.next
    while l2 is not None:
        num2 += str(l2.val)
        l2 = l2.next
    
    num1 = num1[::-1] # reverse the string
    num2 = num2[::-1]
    num3 = str(int(num1) + int(num2)) # add the 2 strings 
    num3 = num3[::-1] # reverse the string back
    #print(num3)


    l1 = head
    while num3: # while num3 is not empty
        l1.val = int(num3[0]) # add the value of the int at the first pos
        #print(l1.val)
        num3 = num3[1:] # delete the first pos
        if not num3:
            l1.next=None # if num3 is done make the new next = none
        else:
            l1.next = ListNode(0) # else make the new next not equal to none make it equal to whatever since we will just overwrite it in the next iteration
            l1 = l1.next
    return head
        

def solve2(l1, l2): # better and faster/cleaner and less memory 
    if not l1 and l2:
        return 0
    dummy = ListNode(0)
    curr = dummy
    
    carry = 0
    while l1 or l2 or carry:
        val1 = l1.val if l1 else 0
        val2 = l2.val if l2 else 0
        
        total = val1 + val2 + carry
        curr.next = ListNode(total % 10)
        curr = curr.next
        
        carry = (total // 10)
        
        if l1:
            l1 = l1.next
        if l2:
            l2 = l2.next
        
    return dummy.next


'''
Intution: loop through the first list, get all numbers put into a string. loop through second list get all numbers put in a string. then reverse both these strings, turn into an int, add them, then reverse them again, and return them. worked yay! (without ANY help)
'''
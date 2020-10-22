class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        p1 = l1
        p2 = l2
        l3 = ListNode()
        h = l3
        carry = 0
        while p1 or p2:
            v =  (p1.val if p1 else 0) + (p2.val if p2 else 0) + carry
            
            #val = v % 10
            #carry = v // 10
            carry,val = divmod(v, 10)
            
            l3.next = ListNode(val)
            l3 = l3.next
            if p1:
                p1 = p1.next
                
            if p2:
                p2 = p2.next
                
        if carry > 0:
            l3.next = ListNode(1)
            
        return h.next
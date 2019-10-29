# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
        
    def __str__(self):
        return f"Node: val={self.val}, next={self.next}"

    __repr__ = __str__


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        ptr1 = l1
        ptr2 = l2
        head = ListNode(None)
        tail = head

        while ptr1 and ptr2:
            if ptr1.val < ptr2.val:
                tail.next = ptr1
                ptr1 = ptr1.next
                
            else:
                tail.next = ptr2
                ptr2 = ptr2.next
               
            tail = tail.next
        if ptr1:
            tail.next = ptr1
        else:
            tail.next = ptr2
        print(head)
        return head.next

s = Solution()

def test_sample():
    test_l1 = ListNode(val=1, next=ListNode(val=2, next=ListNode(4)))
    test_l2 = ListNode(val=1, next=ListNode(val=3, next=ListNode(4)))
    exp = ListNode(val=1, next=ListNode(val=1, next=ListNode(2, next=ListNode(3, next=ListNode(4, next=ListNode(4))))))
    res = s.mergeTwoLists(test_l1, test_l2)
    while exp:
        assert exp.val == res.val
        exp = exp.next
        res = res.next

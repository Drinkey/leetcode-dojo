# Definition for singly-linked list.

class ListNode:
    def __init__(self, val=None, next_=None):
        self.val = val
        self.next = next_

    def __str__(self):
        return f"Node: val={self.val}, next={self.next}"

    __repr__ = __str__

class LinkedList:
    def __init__(self, max_size=10):
        self.head = ListNode()
        self.tail = None

        self.max_size = max_size
        self.length = 0

    def append(self, value):
        if self.max_size <= self.length:
            raise Exception(f"LinkedList Full:{self.max_size} >= {self.length}")
        
        node = ListNode(value)
        print(f"created new ListNode: {node}")
        if self.tail is None:
            self.head.next = node
        else:
            self.tail.next = node
        self.tail = node
        self.length += 1
        print(f"New ListNode: {node}, length={self.length}")

    def insert0(self, value):
        node = ListNode(value)
        print(f"insert0 {node}")
        if self.tail is None:
            print("new list, adding after head")
            node.next = self.tail
            self.head.next = node
            self.tail = node
        else:
            print("list have node, adding after head")
            node.next = self.head.next
            self.head.next = node
        
    def pp(self):
        ptr = self.head
        print(ptr)

class Solution:
    def reverseList(self, head):
        ptr = head
        
        out_linked_list = LinkedList()
        while ptr and ptr.next:
            print(f"inserting to out:")
            out_linked_list.insert0(ptr.val)
            print("moving to next node")
            ptr = ptr.next
            
        if ptr.val is not None:
            out_linked_list.insert0(ptr.val)

        return out_linked_list.head.next

    def test(self):
        in_list = [1,2,3,4,5]
        link_list = LinkedList()
        
        for i in in_list:
            link_list.append(i)
        print("original linked list for test")
        link_list.pp()
        r = self.reverseList(link_list.head)
        print(f"result={r}")

solution = Solution()
solution.test()
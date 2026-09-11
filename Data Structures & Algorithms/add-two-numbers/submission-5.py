# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def _insert_node(node, val):
            cur = node
            while cur.next:
                cur = cur.next
            cur.next = ListNode(val)
        
        has_remainder = False
        head = ListNode()
        cur = head

        while l1 or l2 or has_remainder:
            l1_val = l1.val if l1 else 0
            l2_val = l2.val if l2 else 0
            tmp = l1_val + l2_val + has_remainder
            has_remainder = tmp // 10
            tmp = tmp % 10
            cur.next = ListNode(tmp)
            cur = cur.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        
        return head.next
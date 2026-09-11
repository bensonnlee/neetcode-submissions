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

        while l1 and l2:
            tmp = l1.val + l2.val
            if has_remainder:
                tmp += 1

            if tmp >= 10:
                has_remainder = True
                tmp -= 10
            else:
                has_remainder = False

            _insert_node(head, tmp)
            l1 = l1.next
            l2 = l2.next

        while l1:
            tmp = l1.val
            if has_remainder:
                tmp += 1

            if tmp >= 10:
                has_remainder = True
                tmp -= 10
            else:
                has_remainder = False

            _insert_node(head, tmp)
            l1 = l1.next

        while l2:
            tmp = l2.val
            if has_remainder:
                tmp += 1

            if tmp >= 10:
                has_remainder = True
                tmp -= 10
            else:
                has_remainder = False

            _insert_node(head, tmp)
            l2 = l2.next

        if has_remainder:
            _insert_node(head, 1)

        return head.next
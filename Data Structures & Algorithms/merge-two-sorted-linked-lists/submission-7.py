# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        def _append(val):
            cur = head
            while cur.next:
                cur = cur.next
            cur.next = ListNode(val)

        head = ListNode()

        while list1 and list2:
            v1 = list1.val
            v2 = list2.val

            if v1 < v2:
                _append(v1)
                list1 = list1.next
            else:
                _append(v2)
                list2 = list2.next

        while list1:
            _append(list1.val)
            list1 = list1.next

        while list2:
            _append(list2.val)
            list2 = list2.next

        return head.next
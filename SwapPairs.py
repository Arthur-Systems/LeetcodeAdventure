# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return Nones
        if head.next is None:
            return head
        temp = head.next.next
        head.next.next = head
        head = head.next
        head.next.next = self.swapPairs(temp)
        return head

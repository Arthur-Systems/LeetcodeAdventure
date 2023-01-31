# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head):
        if head is None:
            return None
        if head.next is None:
            return head
        temp = head.next
        head.next = None
        while temp is not None:
            temp2 = temp.next
            temp.next = head
            head = temp
            temp = temp2
        return head


class Solution:
    def reverseList(self, n):
        if head == None:
            return None
        if head.next is None:
            return head

        temp = head.next
        head.next = self.reverseList(head.next)
        temp.next = head
        return head


if __name__ == "__main__":
    head = [1, 2, 3, 4]
    print(Solution().reverseList(head))

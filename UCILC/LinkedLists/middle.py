class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


def find_middle(head):
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    return slow  # ✅ slow is the middle node


def traverse(head):
    LL = []
    current = head
    while current:
        LL.append(str(current.val))
        current = current.next
    LL.append("None")
    return "->".join(LL)


if __name__ == "__main__":
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6))))))
    print(traverse(head))
    print(traverse(find_middle(head)))

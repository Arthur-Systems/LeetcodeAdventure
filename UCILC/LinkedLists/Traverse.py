class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


def traverse(head):
    current = head
    while current:
        print(current.val, end="->")
        current = current.next
    print("None")


if __name__ == "__main__":
    head = ListNode(1, ListNode(2, ListNode(3)))
    traverse(head)

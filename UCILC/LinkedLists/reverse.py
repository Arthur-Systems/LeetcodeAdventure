class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


def reverse(head):
    if not head:
        return None
    current = head
    prev = None
    while current:
        next_temp = current.next
        current.next = prev
        prev = current
        current = next_temp
    return prev


def traverse(head):
    LL = []
    current = head
    while current:
        LL.append(str(current.val))  # Convert value to string and append
        current = current.next
    LL.append("None")  # Append "None" at the end
    return "->".join(LL)  # Join the list with "->"


if __name__ == "__main__":
    head = ListNode(3, ListNode(2, ListNode(1)))
    print(traverse(head))
    print(traverse(reverse(head)))

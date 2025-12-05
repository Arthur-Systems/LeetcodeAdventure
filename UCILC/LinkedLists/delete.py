class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


def traverse(head):
    LL = []
    current = head
    while current:
        LL.append(str(current.val))
        current = current.next
    LL.append("None")
    return "->".join(LL)


def delete_value(head, val):
    if not head:
        return None
    if head.val == val:
        return head.next
    current = head
    while current.next and current.next.val != val:
        current = current.next
    if current.next:
        current.next = current.next.next
    return head


def delete_by_index(head, index):
    if not head:
        return None
    if index == 0:
        return head.next

    current = head
    i = 0
    while current and i < index - 1:
        current = current.next
        i += 1

    if current and current.next:
        current.next = current.next.next

    return head


def insert_back(head, val):
    new_head = ListNode(val)
    if not head:
        return new_head
    current = head
    while current.next:
        current = current.next
    current.next = new_head

    return head


if __name__ == "__main__":
    head = ListNode(1, ListNode(2, ListNode(3)))
    print("List Before Delete:", traverse(head))
    head = delete_value(head, 2)
    print("List After delete_value(2):", traverse(head))
    head = insert_back(head, 2)
    print("List After insert_back(2):", traverse(head))
    head = delete_by_index(head, 3)
    print("List After delete_by_index(3):", traverse(head))

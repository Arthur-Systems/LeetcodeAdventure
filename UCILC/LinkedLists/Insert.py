class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


def traverse(head):
    LL = []
    current = head
    while current:
        LL.append(str(current.val))  # Convert value to string and append
        current = current.next
    LL.append("None")  # Append "None" at the end
    return "->".join(LL)  # Join the list with "->"


def insert_front(head, val):
    new_node = ListNode(val, head)
    return new_node


def insert_back(head, val):
    new_node = ListNode(val)
    if not head:
        return new_node
    current = head
    while current.next:
        current = current.next
    current.next = new_node
    return head


def insert_middle(head, index, val):
    new_node = ListNode(val)
    if index == 0:
        new_node.next = head
        return new_node
    current = head
    i = 0
    while current and i < index - 1:
        current = current.next
        i += 1
    if current:
        new_node.next = current.next
        current.next = new_node
    return head


if __name__ == "__main__":
    head = ListNode(1, ListNode(2, ListNode(3)))
    print("Current Linked List before insertions:", traverse(head))
    print("Appending 3 Front:", traverse(insert_front(head, 0)))
    print("Appending 4 Back: ", traverse(insert_back(head, 4)))
    print("Inserting 5 at index 2:", traverse(insert_middle(head, 1, 5)))

from LinkedList import LinkedList


def reverse_list(lst):
    if lst.head is None:
        return False

    current_node = lst.head
    prev_node = None
    while current_node:
        next_node = current_node.next
        current_node.next = prev_node
        prev_node = current_node
        current_node = next_node
    lst.head = prev_node

    return lst


ll = LinkedList()
ll.generate(10, 1, 10)
print ll
print reverse_list(ll)

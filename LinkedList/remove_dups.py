from LinkedList import LinkedList


def remove_dups(lst):
    if lst.head is None:
        return False

    current = lst.head
    seen_nodes = {current.value}
    while current.next:
        if current.next.value in seen_nodes:
            current.next = current.next.next
        else:
            seen_nodes.add(current.next.value)
            current = current.next
    return lst


def remove_dups_without_space(lst):
    if lst.head is None:
        return False
    current = lst.head
    while current:
        runner = current
        while runner.next:
            if current.value == runner.next.value:
                runner.next = runner.next.next
            else:
                runner = runner.next
        current = current.next

    return lst


ll = LinkedList()
ll.generate(50, 1, 2)
print ll
remove_dups(ll)
print ll
ll.generate(40, 1, 10)
print ll
remove_dups_without_space(ll)
print ll
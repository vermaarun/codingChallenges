from LinkedList import LinkedList


def find_middle(lst):
    if lst.head is None:
        return False
    fast = lst.head
    slow = lst.head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow.value


ll = LinkedList()
ll.generate(10, 1, 10)
print ll
print find_middle(ll)

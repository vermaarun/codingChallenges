from LinkedList import LinkedList


def kth_from_last(lst, k):
    runner = current = ll.head
    for i in range(k):
        if runner is None:
            return None
        runner = runner.next

    while runner:
        current = current.next
        runner = runner.next

    return current


ll = LinkedList()
ll.generate(20, 1, 20)
print ll
k = 5
print kth_from_last(ll, k)

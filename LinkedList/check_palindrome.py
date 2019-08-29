from LinkedList import LinkedList


def check_palindrome(lst):
    if lst.head is None:
        return False
    fast = slow = lst.head
    stack = []

    while fast and fast.next:
        stack.append(slow.value)
        slow = slow.next
        fast = fast.next.next

    if fast:
        slow = slow.next

    while slow:
        top = stack.pop()
        if top != slow.value:
            return False
        slow = slow.next

    return True


ll = LinkedList([1, 2, 3, 4, 4, 3, 2, 1])
print check_palindrome(ll)

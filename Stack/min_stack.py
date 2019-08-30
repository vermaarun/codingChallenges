import sys


class MinStack:

    def __init__(self, stack_size):
        self.main_stack = []
        self.aux_stack = [sys.maxint] * stack_size
        self.stack_size = stack_size

    def push(self, item):
        if self.is_full():
            raise ValueError('Stack is full')
        self.main_stack.append(item)
        if self.aux_stack[self.aux_size() - 1] >= item:
            self.aux_stack.append(item)

    def pop(self):
        if self.is_empty():
            raise Exception('Stack is empty')
        value = self.main_stack.pop()
        if value == self.aux_stack[self.aux_size() - 1]:
            self.aux_stack.pop()
        return value

    def min(self):
        if self.is_empty():
            raise ValueError("Empty Stack")
        return self.aux_stack[self.aux_size() - 1]

    def is_empty(self):
        return self.size() == 0

    def is_full(self):
        return self.size() == self.stack_size

    def size(self):
        return len(self.main_stack)

    def aux_size(self):
        return len(self.aux_stack)


def stack_min():
    min_stack = MinStack(10)
    min_stack.push(5)
    min_stack.pop()
    min_stack.min()
    min_stack.push(7)
    min_stack.push(1)
    min_stack.push(1)
    min_stack.push(3)
    min_stack.push(3)
    min_stack.push(3)
    print min_stack.min()
    min_stack.push(1)
    min_stack.push(2)
    min_stack.pop()
    min_stack.push(0)
    print min_stack.min()


stack_min()

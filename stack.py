from array import array
from math import fabs


class StackArray:
    """ Стэк на массивах """
    def __init__(self):
        self.stack = array('i')
        self.top = 0
        for i in range(1000):
            self.stack.append(0)

    def stack_empty(self):
        if fabs(sum(self.stack)) == 0:
            return True
        return False

    def push(self, x):
        self.stack[self.top] = x
        self.top += 1

    def pop(self):
        if self.stack_empty():
            raise IndexError
        self.top -= 1
        return self.stack[self.top]

    def __str__(self):
        return ' '.join(str(self.stack[i]) for i in range(self.top))


class Stack:
    """ Стек на списках """
    def __init__(self):
        self.stack = []

    def stack_empty(self):
        return self.stack == []

    def push(self, x):
        self.stack.append(x)

    def pop(self):
        return self.stack.pop()


if __name__ == '__main__':
    st = StackArray()
    st.push(5)
    st.push(-1)
    st.push(4)
    st.push(3)
    st.push(-8)
    print(st.pop())
    print(st.pop())
    print(st.pop())

    stc = Stack()
    stc.push(3)
    stc.push(9)
    print(stc.pop())
    print(stc.pop())

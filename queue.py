from array import array


class QueueArray:
    """ Стек на массивах """
    def __init__(self):
        self.queue = array('i')
        for i in range(1000):
            self.queue.append(0)
        self.tail = 0
        self.head = 0

    def enqueue(self, x):
        self.queue[self.tail] = x
        if self.tail == len(self.queue):
            self.tail = 0
        else:
            self.tail += 1

    def dequeue(self):
        x = self.queue[self.head]
        if self.head == len(self.queue):
            self.head = 1
        self.head += 1
        return x


class Queue:
    """ Стек на списках """
    def __init__(self):
        self.queue = []

    def enqueue(self, x):
        self.queue.append(x)

    def dequeue(self):
        return self.queue.pop(0)


if __name__ == '__main__':
    que = QueueArray()
    que.enqueue(5)
    que.enqueue(6)
    que.enqueue(566)
    que.enqueue(455)
    que.enqueue(521)
    print(que.dequeue())

    qu = Queue()
    qu.enqueue(4)
    qu.enqueue(34)
    qu.enqueue(45)
    qu.enqueue(47)
    qu.enqueue(41)
    qu.enqueue(-99)
    print(qu.dequeue())


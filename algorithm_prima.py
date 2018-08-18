class Node:
    def __init__(self, key):
        self.d = float('inf')   # расстояние
        self.key = key


class QueuePriorites:
    def __init__(self, lst):
        self.queue = lst
        self.build_max_h()

    def max_h(self, i):
        left = 2 * i + 1
        right = 2 * i + 2

        largest = left if left < len(self.queue) and self.queue[i].d < self.queue[left].d else i
        largest = right if right < len(self.queue) and self.queue[right].d < self.queue[largest].d else largest

        if i != largest:
            self.queue[i], self.queue[largest] = self.queue[largest], self.queue[i]
            self.max_h(largest)
    
    def build_max_h(self):
        for i in range(int(len(self.queue) / 2), -1, -1):
            self.max_h(i)
    
    def __str__(self):
        reuslt = 'QueuePriorites: ['

        for num in self.queue:
            reuslt += str(num) + ', '
        reuslt += ']'

        return reuslt

    def extract_min(self):
        if self.queue:
            return self.queue.pop()


def prima(adj, grap, start_node):
    start_node.d = 0
    queue = QueuePriorites(list(adj.keys()))
    result = []

    while queue:
        u = queue.extract_min()
        if u is None:
            break
        for v in adj[u]:
            if v in queue.queue and grap[(u, v)] + u.d < v.d:
                v.d = grap[(u, v)] + u.d
        result.append(str(u.key) + '->' + str(u.d))    
    return result


if __name__ == '__main__':
    a = Node('a')
    b = Node('b')
    c = Node('c')
    d = Node('d')

    adj = {
        a: [b, c, d],
        b: [a, c],
        c: [b, a, d],
        d: [a, c],
    }

    grap = {
        (a, b): 1,
        (a, c): 5,
        (a, d): 8,
        (b, a): 1,
        (b, c): 1,
        (b, d): float('inf'),
        (c, a): 5,
        (c, b): 1,
        (c, d): 1,
        (d, a): 8,
        (d, b): float('inf'),
        (d, c): 1,
    }

    print(prima(adj, grap, a))


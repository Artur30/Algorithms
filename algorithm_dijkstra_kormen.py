class Node:
    def __init__(self, key):
        self.key = key
        self.d = float('inf')


def dijkstra(adj, grap, start_node):
    start_node.d = 0
    Q = list(adj.keys())
    result = []

    while Q:
        Q.sort(reverse=True, key=lambda x: x.d)
        u = Q.pop()

        for v in adj[u]:
            if u.d + grap[(u, v)] < v.d:
                v.d = u.d + grap[(u, v)]
                
        result.append(u)
    return result


if __name__ == '__main__':
    a = Node('a')
    b = Node('b')
    c = Node('c')
    d = Node('d')

    adj = {
        a: [b, c],
        b: [a, c, d],
        c: [a, b, d],
        d: [b, c],
    }

    grap = {
        (a, b): 1,
        (a, c): 5,
        (b, a): 1,
        (b, c): 1,
        (b, d): 8,
        (c, a): 5,
        (c, b): 1,
        (c, d): 1,
        (d, b): 8,
        (d, c): 1,
    }
    result = dijkstra(adj, grap, a)
    for u in result:
        print(str(u.key) + '->' + str(u.d))


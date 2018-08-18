""" Реализация обхода графа в глубину """
import unittest


class Node:
    def __init__(self, key):
        self.key = key
        self.d = float('inf') # расстояние
        self.visited = False


def dfs(adj, start_node):
    """ Функция поиска в глубину. Работает на стеке """
    stack = [] 
    stack.append(start_node)
    start_node.d = 0
    result = []

    while stack:
        v = stack.pop()
        if not v.visited:
            v.visited = True
            for child in adj[v]:
                if not child.visited:
                    child.d = v.d + 1
                    stack.append(child)
            result.append((v.key, v.d))
    return result


if __name__ == '__main__':

    class TestDFS(unittest.TestCase):

        def test_adj_4(self):
            a = Node(5)
            b = Node(6)
            c = Node(3)
            d = Node(4)

            adj = {
                a: [b, c, d],
                b: [a, c],
                c: [a, b, d],
                d: [a, c],
            }
            result = [(5, 0), (4, 1), (3, 2), (6, 3)]
            self.assertEqual(dfs(adj, a), result)
        
        def test_adj_6(self):
            a = Node(1)
            b = Node(2)
            c = Node(3)
            d = Node(4)
            e = Node(5)
            f = Node(6)
            g = Node(7)

            adj = {
                a: [b, c, d],
                b: [a, e, f],
                c: [a],
                d: [a, g],
                f: [b],
                e: [b],
                g: [d],
            }
            result = [(1, 0), (4, 1), (7, 2), (3, 1), (2, 1), (6, 2), (5, 2)]

            self.assertEqual(dfs(adj, a), result)

    unittest.main()


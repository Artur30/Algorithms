""" Здесь представлен поиск графа в ширину """
from collections import deque
import unittest


class Node:
    def __init__(self, key):
        self.key = key
        self.d = float('inf') # расстояние
        self.visited = False


def bfs(adj, start_node):
    """ Функция для поиска графа в ширину """
    result = [] # в result заисывается результат поиска в ширину
    Q = deque()
    
    Q.append(start_node)
    # Инициализируем стартовую ноду
    start_node.d = 0
    start_node.visited = True
    
    while len(Q) != 0:
        node = Q.popleft()
        # в списке содержится кортежи <ключ, расстояние>
        result.append((node.key, node.d))
        for child in adj[node]:
            if not child.visited:
                Q.append(child)
                child.d = node.d + 1
                child.visited = True
    return result


if __name__ == '__main__':
    # Unit - тесты
    class TestBFS(unittest.TestCase):
        
        def test_adg_4(self):
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
            result = [(5, 0), (6, 1), (3, 1), (4, 1)]
            
            self.assertEqual(bfs(adj, a), result)

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
            result = [(1, 0), (2, 1), (3, 1), (4, 1), (5, 2), (6, 2), (7, 2)]

            self.assertEqual(bfs(adj, a), result)

    unittest.main()

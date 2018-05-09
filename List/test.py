import unittest
from main import List, Node


class TestListClass(unittest.TestCase):

    def setUp(self):
        self.lst = List()

    def test_first_added_item(self):
        self.lst.add_node(45)
        current = self.lst.head
        result = '['
        while current:
            result += str(current.key) + ', '
            current = current.next
        result += ']'
        self.assertEqual(result, '[45, ]')

    def test_added_item(self):
        for i in range(1, 40, 4):
            self.lst.add_node(i)
        current = self.lst.head
        result = '['
        while current:
            result += str(current.key) + ', '
            current = current.next
        result += ']'
        self.assertEqual(result, '[1, 5, 9, 13, 17, 21, 25, 29, 33, 37, ]')



if __name__ == '__main__':
    unittest.main()




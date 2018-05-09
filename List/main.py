class Node:

    def __init__(self, key):
        self.key = key
        self.next = None


class List:

    def __init__(self):
        self.head = None
        self.last = None

    def add_node(self, key):
        """ Method for adding an item in the list """
        if self.head is None:
            self.head = Node(key)
            self.last = self.head
        else:
            self.last.next = Node(key)
            self.last = self.last.next

    def search_node(self, key):
        """ Method for searching an item in the list """
        current = self.head

        while current and current.key != key:
            current = current.next
        return current or Node('No item')

    def remove_node(self, key):
        """ Method for removing an item in the list """
        current = self.head

        prev = None
        while current and current.key != key:
            prev = current
            current = current.next

        if prev is None:
            self.head = current.next
        else:
            prev.next = current.next

    def __str__(self):
        """ Beautiful output """
        current = self.head

        result = 'List : ['
        while current:
            result += str(current.key) + ', '
            current = current.next
        result += ']'

        return result


if __name__ == '__main__':
    lst = List()
    lst.add_node(5)
    lst.add_node(4)
    lst.add_node(12)
    print(lst.search_node(5).key)
    lst.remove_node(5)
    print(lst)



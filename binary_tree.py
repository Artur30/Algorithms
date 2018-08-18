class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.parent = None


class Tree:
    def __init__(self):
        self.root = None

    def tree_insert(self, z):
        """ Method adding item in the Tree """
        y = None
        x = self.root
        while x:
            y = x
            if z.key < x.key:
                x = x.left
            else:
                x = x.right
        z.parent = y
        if y is None:
            self.root = z
        elif z.key < y.key:
            y.left = z
        else:
            y.right = z

    def tree_search(self, current, x):
        """ Method searching item in the Tree """
        if current is None:
            return Node('No item').key
        elif current.key == x:
            return current, current.key

        if current.key < x:
            return self.tree_search(current.right, x)
        else:
            return self.tree_search(current.left, x)

    def tree_minimum(self, z):
        current = z
        while current.left:
            current = current.left
        return current

    def tree_maximum(self, z):
        current = z
        while current.right:
            current = current.right
        return current

    def transplant(self, u, v):
        if u.parent is None:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v

        if v is not None:
            v.parent = u.parent

    def tree_delete(self, z):
        if z.left is None:
            self.transplant(z, z.right)
        elif z.right is None:
            self.transplant(z, z.left)
        else:
            y = self.tree_minimum(z.right)
            if y.parent != z:
                self.transplant(y, y.right)
                y.right = z.right
                y.right.parent = y
            self.transplant(z, y)
            y.left = z.left
            y.left.parent = y

    def __str__(self):
        """ Beautiful output """
        result = 'Tree : ['

        def inorder_tree_walk(x):
            nonlocal result
            if x:
                inorder_tree_walk(x.left)
                result += str(x.key) + ', '
                inorder_tree_walk(x.right)
        inorder_tree_walk(self.root)
        result += ']'
        return result


if __name__ == '__main__':
    tree = Tree()
    a = Node(45)
    tree.tree_insert(a)
    tree.tree_insert(Node(3))
    tree.tree_insert(Node(56))
    print(tree.tree_search(tree.root, 45)[-1])
    print(tree.tree_delete(a))
    print(tree)



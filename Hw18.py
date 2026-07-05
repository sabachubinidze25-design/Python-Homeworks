class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def _insert(self, node, data):
        if node is None:
            return Node(data)

        if data < node.data:
            node.left = self._insert(node.left, data)
        elif data > node.data:
            node.right = self._insert(node.right, data)

        return node

    def insert(self, data):
        self.root = self._insert(self.root, data)

    def _print_parents(self, node, parent):
        if node:
            if parent is None:
                print(node.data, "-> Root")
            else:
                print(node.data, "->", parent.data)

            self._print_parents(node.left, node)
            self._print_parents(node.right, node)

    def print_parents(self):
        print("Parents are:")
        self._print_parents(self.root, None)

    def _print_leaf_nodes(self, node):
        if node is None:
            return

        if node.left is None and node.right is None:
            print(node.data)

        self._print_leaf_nodes(node.left)
        self._print_leaf_nodes(node.right)

    def print_leaf_nodes(self):
        print("Leaf nodes are:")
        self._print_leaf_nodes(self.root)


bst = BST()

# Insert nodes
bst.insert(50)
bst.insert(30)
bst.insert(70)
bst.insert(20)
bst.insert(40)
bst.insert(60)
bst.insert(80)

bst.print_parents()

bst.insert(65)

print()

bst.print_parents()

print()

bst.print_leaf_nodes()

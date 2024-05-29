
import random

class Node:
    def __init__(self, key) -> None:    
        self.key = key
        self.left = None
        self.right = None
    
class BinarySearchTree:
    def __init__(self) -> None:
        self.root = None

    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
        else:
            self._insert(self.root, key)

    def _insert(self, node, key):
        if key < node.key:
            if node.left is None:
                node.left = Node(key)
            else:
                self._insert(node.left, key)
        else:
            if node.right is None:
                node.right = Node(key)
            else:
                self._insert(node.right, key)
    
    def search(self, key):
        return self._search(self.root, key)
    
    def _search(self, node, key):
        if node is None or node.key == key:
            return node
        if key < node.key:
            return self._search(node.left, key)
        return self._search(node.right, key)
    
    def inorder_traversal(self):
        return self._inorder_traversal(self.root, [])
    
    def _inorder_traversal(self, node, result):
        if node:
            self._inorder_traversal(node.left, result)
            result.append(node.key)
            self._inorder_traversal(node.right, result)
        return result

bst = BinarySearchTree()

for i in range(10):
    bst.insert(random.randrange(0, 100))

bst.insert(34)
print(bst.inorder_traversal())

search = 40

result = bst.search(search)

if result:
    print(f"Key {search} found in the tree.")
else:
    print(f"Key {search} not found in the tree.")









    
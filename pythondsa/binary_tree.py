class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.value = key

class BinaryTree:
    def __init__(self):
        self.root = None

    # In-order traversal
    def inorder_traversal(self, root):
        res = []
        if root:
            res = self.inorder_traversal(root.left)
            res.append(root.value)
            res = res + self.inorder_traversal(root.right)
        return res

    # Pre-order traversal
    def preorder_traversal(self, root):
        res = []
        if root:
            res.append(root.value)
            res = res + self.preorder_traversal(root.left)
            res = res + self.preorder_traversal(root.right)
        return res

    # Post-order traversal
    def postorder_traversal(self, root):
        res = []
        if root:
            res = self.postorder_traversal(root.left)
            res = res + self.postorder_traversal(root.right)
            res.append(root.value)
        return res

    # Insert a node
    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
        else:
            self._insert(self.root, key)

    def _insert(self, root, key):
        if key < root.value:
            if root.left is None:
                root.left = Node(key)
            else:
                self._insert(root.left, key)
        else:
            if root.right is None:
                root.right = Node(key)
            else:
                self._insert(root.right, key)

# Example usage
if __name__ == "__main__":
    tree = BinaryTree()
    tree.insert(50)
    tree.insert(30)
    tree.insert(20)
    tree.insert(40)
    tree.insert(70)
    tree.insert(60)
    tree.insert(80)

    print("In-order traversal:", tree.inorder_traversal(tree.root))  # Output: [20, 30, 40, 50, 60, 70, 80]
    print("Pre-order traversal:", tree.preorder_traversal(tree.root))  # Output: [50, 30, 20, 40, 70, 60, 80]
    print("Post-order traversal:", tree.postorder_traversal(tree.root))  # Output: [20, 40, 30, 60, 80, 70, 50]

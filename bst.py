class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def insert(root, value):
    if root is None:
        return TreeNode(value)
    if value < root.value:
        root.left = insert(root.left, value)
    elif value > root.value:
        root.right = insert(root.right, value)
    return root

def search(root, value):
    if root is None or root.value == value:
        return root
    if value < root.value:
        return search(root.left, value)
    else:
        return search(root.right, value)

def inorder_traversal(root):
    if root:
        inorder_traversal(root.left)
        print(root.value, end=' ')
        inorder_traversal(root.right)


bst_root = None
elements = [5, 3, 7, 2, 4, 6, 8]
for element in elements:
    bst_root = insert(bst_root, element)

print("Search result:")
for value in [5, 4, 9]:
    result = search(bst_root, value)
    if result:
        print(f"{value} found")
    else:
        print(f"{value} not found")


print("\nAscending traversal:")
inorder_traversal(bst_root)

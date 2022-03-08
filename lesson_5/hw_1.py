#Задание №1 Реализовать обход дерева post-order. Сначала левое, потом правое поддерево, в последнюю очередь корень

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def postorderTraversal(root) -> list[int]:
    if root:
        postorderTraversal(root.left)
        postorderTraversal(root.right)
        print(root.val)

tree = TreeNode(1)
tree.left = TreeNode(2)
tree.right = TreeNode(3)
tree.left.left = TreeNode(4)
tree.left.right = TreeNode(5)
postorderTraversal(tree)

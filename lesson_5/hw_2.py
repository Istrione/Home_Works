#Задание №2 Проверить дерево на симметричность

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
       self.val = val
       self.left = left
       self.right = right

def isSymmetric(root) -> bool:
    def helper(left, right):
        if not left and not right:
            return True
        if left and right:
            if left.val == right.val:
                left_half = helper(left.left, right.right)
                right_half = helper(left.right, right.left)
                return left_half and right_half
        return False

    return helper(root.left, root.right)

tree = TreeNode(1)
tree.left = TreeNode(2)
tree.right = TreeNode(2)
tree.left.left = TreeNode(3)
tree.right.right = TreeNode(3)
tree.left.right = TreeNode(4)
tree.right.left = TreeNode(4)
print(isSymmetric(tree))



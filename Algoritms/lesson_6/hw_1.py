#Задание №1 LC Populating Next Right Pointers in Each Node II

class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

def connect(root: 'Node') -> 'Node':
    if not root:
        return root
    if root.left:
        if root.right:
            root.left.next = root.right
        else:
            node = root.next
            while node:
                if not node.left and not node.right:
                    node = node.next
                    continue
                if node.left:
                    root.left.next = node.left
                elif node.right:
                    root.left.next = node.right
                break
    if root.right:
        node = root.next
        while node:
            if not node.left and not node.right:
                node = node.next
                continue
            if node.left:
                root.right.next = node.left
            elif node.right:
                root.right.next = node.right
            break

    connect(root.right)
    connect(root.left)
    return root

tree = Node(1)
tree.left = Node(2)
tree.right = Node(3)
tree.right.right = Node(7)
tree.left.left = Node(4)
tree.left.right = Node(5)
connect(tree)
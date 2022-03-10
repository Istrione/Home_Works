# Задание №3

class TreeNode:
    def __init__(self):
        self.children = {}
        self.word = False

class word_dicrionary:

    def __init__(self):
        self.root = TreeNode()

    def add_word(self, word: str):
        cur = self.root

        for c in word:
            if c not in cur.children:
                cur.children[c] = TreeNode()
            cur = cur.children[c]
        cur.word = True

    def search(self, word: str):

        def dfs(j, root):
            cur = root

            for i in range(len(j, word)):
                c = word[i]

                if c == ".":
                    for child in cur.children.values():
                        if dfs(i + 1, child):
                            return True
                    return False
                else:
                    if c not in cur.children:
                        return False
                    cur = cur.children[c]
            return cur.word

        return dfs(0, self.root)


class TreeNode:
    def __init__(self):
        self.chars = {}
        self.is_end = False


class PrefixTree:
    def __init__(self):
        self.head = TreeNode()
        
    def insert(self, word: str) -> None:
        cur = self.head
        for i in word:
            if i in cur.chars:
                cur = cur.chars[i]
            else:
                new_node = TreeNode()
                cur.chars[i] = new_node
                cur = new_node
        cur.is_end = True


    def search(self, word: str) -> bool:
        cur = self.head
        for i in range(len(word)):
            if word[i] in cur.chars:
                cur = cur.chars[word[i]]
            else:
                return False
        
        return True if cur.is_end else False
        

    def startsWith(self, prefix: str) -> bool:
        cur = self.head
        for i in prefix:
            if i in cur.chars:
                cur = cur.chars[i]
            else:
                return False
        return True
class TreeNode:
    def __init__(self):
        self.chars = {}
        self.is_end = False

class WordDictionary:
    def __init__(self):
        self.head = TreeNode()

    def addWord(self, word: str) -> None:
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
        
        def dfs(j, root):
            cur = root
            
            for i in range(j, len(word)):
                c = word[i]
                if c == ".":
                    for k in cur.chars.values():
                        if dfs(i+1,k):
                            return True
                    return False
                else:
                    if c not in cur.chars:
                        return False
                    else:
                        cur = cur.chars[c]
            
            return cur.is_end
        
        return dfs(0,self.head)

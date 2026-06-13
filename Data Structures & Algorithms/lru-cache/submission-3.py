class Node:
    def __init__(self, key, val, prev, nxt):
        self.key = key
        self.val = val
        self.prev = prev
        self.nxt = nxt

class LRUCache:

    def __init__(self, capacity: int):
        self.key_node = {}
        self.left, self.right = Node(0, 0, None, None),  Node(0, 0, None, None)
        self.capacity = capacity
        
        self.left.nxt = self.right
        self.right.prev = self.left

    def insert_to_end(self, node):
        prev_node = self.right.prev
        prev_node.nxt = node
        node.prev = prev_node

        node.nxt = self.right
        self.right.prev = node


    def delete(self, node):
        prev = node.prev
        nxt = node.nxt

        prev.nxt = nxt
        nxt.prev = prev

    def get(self, key: int) -> int:
        if key not in self.key_node:
            return -1    
        self.delete(self.key_node[key])
        self.insert_to_end(self.key_node[key])
        return self.key_node[key].val
        

    def put(self, key: int, value: int) -> None:
        if key not in self.key_node:
            self.key_node[key] = Node(key, value, None, None)
            self.insert_to_end(self.key_node[key])
            if len(self.key_node) > self.capacity:
                temp = self.left.nxt
                self.delete(temp)
                del self.key_node[temp.key]
        self.delete(self.key_node[key])
        self.key_node[key] = Node(key, value, None, None)
        self.insert_to_end(self.key_node[key])
        

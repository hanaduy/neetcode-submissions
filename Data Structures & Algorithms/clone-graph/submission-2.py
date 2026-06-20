"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        clone_dict = {}
        queue = deque([node])
        visited = set({node})

        if not node:
            return None

        # Register Node old-new
        while queue:
            cur = queue.popleft()
            new_node = Node(cur.val , None)
            clone_dict[cur] = new_node
            for neighbor in cur.neighbors:
                if neighbor not in visited:
                    queue.append(neighbor)
                    visited.add(neighbor)


        # Wiring the nodes
        visited = set({node})
        queue = deque([node])
        while queue:
            cur = queue.popleft()
            for neighbor in cur.neighbors:
                clone_dict[cur].neighbors.append(clone_dict[neighbor])
                if neighbor not in visited:
                    queue.append(neighbor)
                    visited.add(neighbor)

        return clone_dict[node]
        
                
        


        
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pos_speed = {}
        stack = deque()
        for k,v in enumerate(position):
            pos_speed[v] = speed[k]
        
        position.sort()
        print(pos_speed, position)

        for i in range(len(position)-1, -1, -1):
            if not stack:
                stack.appendleft((target-position[i])/pos_speed[position[i]])
            else:
                cur_time = (target-position[i])/pos_speed[position[i]]
                if cur_time <= stack[0]:
                    continue
                else:
                    stack.appendleft(cur_time)
        return len(stack)

class Solution:
    def isHappy(self, n: int) -> bool:
        appear = set()
        result = 0
        while result != 1:
            result = 0
            n_char = str(n)
            for i in n_char:
                result += int(i)**2
            else:
                if result in appear:
                    return False
                appear.add(result)
                n = result
            print(n)
        return True
            
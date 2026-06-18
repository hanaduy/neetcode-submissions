class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []

        def dfs(path, left_count, right_count):
            if left_count == right_count == n:
                result.append(path)
                return
            if left_count < n:
                dfs(path + "(", left_count+1, right_count)
            if left_count > right_count:
                dfs(path + ")", left_count, right_count+1)
            return
        dfs("",0,0)
        return result

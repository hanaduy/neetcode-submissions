class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROW, COL = len(matrix), len(matrix[0])

        l, r = 0, COL*ROW-1

        while l<=r:  
            mid = (l+r)//2
            row = mid//COL
            col = mid%COL

            if matrix[row][col] == target:
                return True
            elif matrix[row][col] < target:
                l = mid + 1
            else:
                r = mid - 1
        
        return False
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left = 0 
        rows = len(matrix)
        cols = len(matrix[0])
        right = (rows * cols) - 1
        while left <= right:
            mid = (left + right)  // 2
            row, col = mid//cols, mid%cols
            print(row, col, mid)
            if matrix[row][col] == target:
                return True
            if matrix[row][col] > target:
                right = mid-1
            else:
                left = mid+1
        return False
             
        

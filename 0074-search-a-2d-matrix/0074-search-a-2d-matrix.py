class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        
        n = len(matrix)
        m = len(matrix[0])

        row, col = 0, m - 1
        
        while row < n and col >= 0:
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] < target:
                row += 1  # Move down to a larger row
            else:
                col -= 1  # Move left to a smaller column
        
        return False

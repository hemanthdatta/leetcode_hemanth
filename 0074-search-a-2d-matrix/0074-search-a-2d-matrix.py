class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        
        n = len(matrix)
        m = len(matrix[0])
        
        # Treating the matrix as a 1D array
        left, right = 0, n * m - 1
        
        while left <= right:
            mid = (left + right) // 2
            # Map the 1D index to 2D matrix
            mid_val = matrix[mid // m][mid % m]
            
            if mid_val == target:
                return True
            elif mid_val < target:
                left = mid + 1
            else:
                right = mid - 1
        
        return False

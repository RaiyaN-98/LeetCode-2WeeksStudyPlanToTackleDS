class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in range(len(matrix)):
            if i + 1 == len(matrix) or matrix[i+1][0] > target:
                for y in matrix[i]:
                    if y == target:
                        return True
                return False
        
        return False

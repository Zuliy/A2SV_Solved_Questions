class Solution:
    def findRotation(self, mat, target):
        n = len(mat)
        
        # Helper function to rotate matrix 90° clockwise
        def rotate(matrix):
            new_matrix = [[0] * n for _ in range(n)]
            
            for i in range(n):
                for j in range(n):
                    new_matrix[j][n - 1 - i] = matrix[i][j]
            
            return new_matrix
        
        # Try 4 rotations
        for _ in range(4):
            if mat == target:
                return True
            mat = rotate(mat)
        
        return False
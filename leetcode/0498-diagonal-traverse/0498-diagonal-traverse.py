class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        if not mat or not mat[0]:
            return []
        
        m, n = len(mat), len(mat[0])
        result = []
        row = col = 0
        
       
        direction_up = True
        
        for _ in range(m * n):
            result.append(mat[row][col])
            
            if direction_up:
                
                if col == n - 1:
                    
                    row += 1
                    direction_up = False
                elif row == 0:
                    
                    col += 1
                    direction_up = False
                else:
                    
                    row -= 1
                    col += 1
            else:
               
                if row == m - 1:
                    
                    col += 1
                    direction_up = True
                elif col == 0:
                    
                    row += 1
                    direction_up = True
                else:
                   
                    row += 1
                    col -= 1
        
        return result
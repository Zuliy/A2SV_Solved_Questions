class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> list[list[int]]:
        res = []
        res.append([rStart, cStart])
        if rows * cols == 1:
            return res
        
       
        dirs = [(0,1), (1,0), (0,-1), (-1,0)]
        r, c = rStart, cStart
        step = 1  
        
        while len(res) < rows * cols:
            for i in range(4):
                dr, dc = dirs[i]
               
                for _ in range(step):
                    r += dr
                    c += dc
                    if 0 <= r < rows and 0 <= c < cols:
                        res.append([r, c])
                    if len(res) == rows * cols:
                        return res
               
                if i == 1 or i == 3:
                    step += 1
        return res
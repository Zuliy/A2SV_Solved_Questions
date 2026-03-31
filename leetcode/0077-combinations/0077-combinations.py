class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:
        result = []       
        curr = []         
        def backtrack(start: int):
           
            if len(curr) == k:
                result.append(curr.copy()) 
                return
        
          
            for i in range(start, n + 1):
                curr.append(i)      
                backtrack(i + 1)    
                curr.pop()           
        
        backtrack(1)
        return result
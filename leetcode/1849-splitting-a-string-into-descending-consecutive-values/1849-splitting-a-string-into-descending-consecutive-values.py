class Solution:
    def splitString(self, s: str) -> bool:
        
        def dfs(index, prev, count):
          
            if index == len(s):
                return count >= 2
            
            num = 0
            
            for i in range(index, len(s)):
                num = num * 10 + int(s[i])
                
                if prev is not None:
                    if num >= prev:
                        break  
                    if prev - num > 1:
                        continue 
                    if prev - num == 1:
                        if dfs(i + 1, num, count + 1):
                            return True
                else:
                  
                    if dfs(i + 1, num, count + 1):
                        return True
            
            return False
        
        return dfs(0, None, 0)
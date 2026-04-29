from collections import deque

class Solution:
    def removeInvalidParentheses(self, s: str):
        
        def is_valid(expr):
            balance = 0
            for ch in expr:
                if ch == '(':
                    balance += 1
                elif ch == ')':
                    balance -= 1
                    if balance < 0:
                        return False
            return balance == 0
        
        visited = set()
        queue = deque([s])
        visited.add(s)
        res = []
        found = False
        
        while queue:
            level_size = len(queue)
            
            for _ in range(level_size):
                curr = queue.popleft()
                
                if is_valid(curr):
                    res.append(curr)
                    found = True
                
                if found:
                    continue  
                
                for i in range(len(curr)):
                    if curr[i] not in "()":
                        continue
                    
                    nxt = curr[:i] + curr[i+1:]
                    
                    if nxt not in visited:
                        visited.add(nxt)
                        queue.append(nxt)
            
            if found:
                break
        
        return res
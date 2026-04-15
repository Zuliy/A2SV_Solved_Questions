class Solution:
    def distributeCookies(self, cookies, k):
        children = [0] * k
        self.ans = float('inf')

        def backtrack(index):
           
            if index == len(cookies):
                self.ans = min(self.ans, max(children))
                return
            
            for i in range(k):
               
                if i > 0 and children[i] == 0 and children[i-1] == 0:
                    continue
                
                children[i] += cookies[index]

                if children[i] < self.ans:
                    backtrack(index + 1)

                children[i] -= cookies[index] 
        backtrack(0)
        return self.ans
class Solution:
    def findValidPair(self, s: str) -> str:
        from collections import Counter
        
        freq = Counter(s)
        
        for i in range(len(s) - 1):
            a = s[i]
            b = s[i + 1]
            
           
            if a != b:
               
                if freq[a] == int(a) and freq[b] == int(b):
                    return a + b
        
        return ""
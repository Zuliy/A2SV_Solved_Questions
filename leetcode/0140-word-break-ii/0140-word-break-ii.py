from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        word_set = set(wordDict)
        memo = {}

        def dfs(sub):
            if sub in memo:
                return memo[sub]
            
            if not sub:
                return [""]  
            
            res = []
            
            for word in word_set:
                if sub.startswith(word):
                    suffix = sub[len(word):]
                    suffix_ways = dfs(suffix)
                    
                    for way in suffix_ways:
                        if way:
                            res.append(word + " " + way)
                        else:
                            res.append(word)
            
            memo[sub] = res
            return res
        
        return dfs(s)
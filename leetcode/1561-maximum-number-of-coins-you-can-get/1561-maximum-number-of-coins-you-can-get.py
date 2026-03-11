class Solution:
    def maxCoins(self, piles):
        piles.sort()
        n = len(piles) // 3
        
        result = 0
        i = len(piles) - 2
        
        for _ in range(n):
            result += piles[i]
            i -= 2
            
        return result
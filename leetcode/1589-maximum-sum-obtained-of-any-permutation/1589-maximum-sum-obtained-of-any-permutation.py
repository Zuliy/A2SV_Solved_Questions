class Solution:
    def maxSumRangeQuery(self, nums, requests):
        n = len(nums)
        
       
        freq = [0] * n
        
        for l, r in requests:
            freq[l] += 1
            if r + 1 < n:
                freq[r + 1] -= 1
        
      
        for i in range(1, n):
            freq[i] += freq[i - 1]
        
       
        nums.sort()
        freq.sort()
        
      
        MOD = 10**9 + 7
        result = 0
        
        for i in range(n):
            result = (result + nums[i] * freq[i]) % MOD
        
        return result
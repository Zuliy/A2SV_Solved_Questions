from collections import deque

class Solution:
    def longestSubarray(self, nums: list[int], limit: int) -> int:
        maxDeque = deque() 
        minDeque = deque()  
        left = 0
        result = 0
        
        for right, num in enumerate(nums):
           
            while maxDeque and num > maxDeque[-1]:
                maxDeque.pop()
            maxDeque.append(num)
            
           
            while minDeque and num < minDeque[-1]:
                minDeque.pop()
            minDeque.append(num)
            
       
            while maxDeque[0] - minDeque[0] > limit:
                if nums[left] == maxDeque[0]:
                    maxDeque.popleft()
                if nums[left] == minDeque[0]:
                    minDeque.popleft()
                left += 1
            
            result = max(result, right - left + 1)
        
        return result
class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        count = {0: 1}
        curr_sum = 0
        total_subarrays = 0
        
        for num in nums:
            curr_sum += num
            total_subarrays += count.get(curr_sum - goal, 0)
            count[curr_sum] = count.get(curr_sum, 0) + 1
            
        return total_subarrays
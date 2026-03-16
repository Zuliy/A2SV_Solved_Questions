class Solution:
    def checkSubarraySum(self, nums, k):
        remainder_index = {0: -1} 
        prefix = 0

        for i, num in enumerate(nums):
            prefix += num

            if k != 0:
                prefix %= k

            if prefix in remainder_index:
                if i - remainder_index[prefix] >= 2:
                    return True
            else:
                remainder_index[prefix] = i

        return False
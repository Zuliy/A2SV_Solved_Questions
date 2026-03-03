class Solution:
    def minimumIndex(self, nums):
        n = len(nums)
        
        # Step 1: Find dominant element (Boyer-Moore)
        candidate = None
        count = 0
        
        for num in nums:
            if count == 0:
                candidate = num
            if num == candidate:
                count += 1
            else:
                count -= 1
        
        # Step 2: Count total occurrences of dominant element
        total = 0
        for num in nums:
            if num == candidate:
                total += 1
        
        # Step 3: Try every split
        left_count = 0
        
        for i in range(n - 1):
            if nums[i] == candidate:
                left_count += 1
            
            left_length = i + 1
            right_length = n - i - 1
            
            right_count = total - left_count
            
            # Check dominance condition
            if left_count > left_length // 2 and right_count > right_length // 2:
                return i
        
        return -1
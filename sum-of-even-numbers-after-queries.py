class Solution:
    def sumEvenAfterQueries(self, nums: list[int], queries: list[list[int]]) -> list[int]:
        even_sum = sum(x for x in nums if x % 2 == 0)
        answer = []
        
        for val, index in queries:
            
            # If current value is even, remove it from even_sum
            if nums[index] % 2 == 0:
                even_sum -= nums[index]
            
            # Apply update
            nums[index] += val
            
            # If new value is even, add it
            if nums[index] % 2 == 0:
                even_sum += nums[index]
            
            answer.append(even_sum)
        
        return answer

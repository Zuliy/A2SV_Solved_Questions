class NumArray:

    def __init__(self, nums):
        self.prefix = []
        total = 0
        
        for num in nums:
            total += num
            self.prefix.append(total)

    def sumRange(self, left, right):
        if left == 0:
            return self.prefix[right]
        return self.prefix[right] - self.prefix[left - 1]
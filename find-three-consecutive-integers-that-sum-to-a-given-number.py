class Solution:
    def sumOfThree(self, num: int) -> list[int]:
        if num % 3 != 0:
            return []
        
        middle = num // 3
        return [middle - 1, middle, middle + 1]

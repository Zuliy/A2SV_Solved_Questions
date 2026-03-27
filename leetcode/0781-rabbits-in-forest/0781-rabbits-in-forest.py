class Solution:
    def numRabbits(self, answers):
        from collections import Counter
        
        count = Counter(answers)
        total = 0

        for x, c in count.items():
            group_size = x + 1
            
        
            groups = (c + group_size - 1) // group_size
            
            total += groups * group_size

        return total
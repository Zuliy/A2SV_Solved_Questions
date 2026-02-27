class Solution:
    def findOriginalArray(self, changed):
        # Step 1: Length must be even
        if len(changed) % 2 != 0:
            return []
        
        # Step 2: Count frequency manually
        count = {}
        for num in changed:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1
        
        # Step 3: Sort keys (smallest first)
        keys = sorted(count.keys())
        
        original = []
        
        for x in keys:
            if count[x] == 0:
                continue
            
            double_x = 2 * x
            
            # If there aren't enough double_x to pair → impossible
            if double_x not in count or count[double_x] < count[x]:
                return []
            
            # Add x to original as many times as count[x]
            for _ in range(count[x]):
                original.append(x)
            
            # Reduce the paired elements
            count[double_x] -= count[x]
        
        return original

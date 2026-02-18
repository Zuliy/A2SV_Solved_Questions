class Solution:
    def findUnion(self, a, b):
        # Convert both arrays to sets and take union
        union_set = set(a) | set(b)
        
        # Convert back to list (driver code will sort)
        return list(union_set)

class Solution:
    def restoreString(self, s: str, indices: list[int]) -> str:
        n = len(s)
        result = [""] * n   # create empty list of size n
        
        for i in range(n):
            result[indices[i]] = s[i]
        
        return "".join(result)

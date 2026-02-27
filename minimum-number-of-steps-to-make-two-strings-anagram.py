class Solution:
    def minSteps(self, s: str, t: str) -> int:
        
        count_s = [0] * 26
        count_t = [0] * 26
        
        # Count frequency
        for ch in s:
            count_s[ord(ch) - ord('a')] += 1
        
        for ch in t:
            count_t[ord(ch) - ord('a')] += 1
        
        steps = 0
        
        for i in range(26):
            if count_t[i] > count_s[i]:
                steps += count_t[i] - count_s[i]
        
        return steps

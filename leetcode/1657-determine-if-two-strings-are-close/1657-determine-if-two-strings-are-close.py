class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        # Step 1: Length must match
        if len(word1) != len(word2):
            return False
        
        # Step 2: Count frequency manually
        freq1 = {}
        freq2 = {}
        
        for ch in word1:
            freq1[ch] = freq1.get(ch, 0) + 1
        
        for ch in word2:
            freq2[ch] = freq2.get(ch, 0) + 1
        
        # Step 3: Characters must be the same
        if set(freq1.keys()) != set(freq2.keys()):
            return False
        
        # Step 4: Frequencies must match after sorting
        if sorted(freq1.values()) != sorted(freq2.values()):
            return False
        
        return True
class Solution:
    def frequencySort(self, s: str) -> str:
        # Step 1: Count frequency manually
        freq = {}
        for ch in s:
            if ch in freq:
                freq[ch] += 1
            else:
                freq[ch] = 1
        
        # Step 2: Convert dictionary to list of (char, count)
        items = list(freq.items())
        
        # Step 3: Sort by frequency descending
        items.sort(key=lambda x: x[1], reverse=True)
        
        # Step 4: Build result string
        result = ""
        for char, count in items:
            result += char * count
        
        return result
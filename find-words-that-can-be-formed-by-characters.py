class Solution:
    def countCharacters(self, words, chars):
        from collections import Counter
        
        chars_count = Counter(chars)
        total_length = 0
        
        for word in words:
            word_count = Counter(word)
            
            good = True
            for char in word_count:
                if word_count[char] > chars_count[char]:
                    good = False
                    break
            
            if good:
                total_length += len(word)
        
        return total_length

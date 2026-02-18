class Solution:
    # Function to check if two arrays are equal or not
    def checkEqual(self, a, b) -> bool:
        # If lengths are different, arrays can't be equal
        if len(a) != len(b):
            return False
        
        # Sort both arrays and compare
        a.sort()
        b.sort()
        
        return a == b

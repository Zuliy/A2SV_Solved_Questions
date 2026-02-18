class Solution:
    def isCovered(self, ranges, left, right):
        # Check each integer in the range [left, right]
        for num in range(left, right + 1):
            covered = False
            # Check if this integer is covered by any range
            for start, end in ranges:
                if start <= num <= end:
                    covered = True
                    break
            # If any number is not covered, return false
            if not covered:
                return False
        return True

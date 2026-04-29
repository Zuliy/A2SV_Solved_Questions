from bisect import bisect_right, insort

class Solution:
    def numberOfPairs(self, nums1, nums2, diff):
        arr = [a - b for a, b in zip(nums1, nums2)]

        sorted_list = []
        count = 0

        for val in arr:
         
            target = val + diff
            idx = bisect_right(sorted_list, target)
            count += idx

            insort(sorted_list, val)

        return count
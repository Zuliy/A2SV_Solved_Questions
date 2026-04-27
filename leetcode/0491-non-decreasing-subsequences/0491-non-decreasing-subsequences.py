class Solution:
    def findSubsequences(self, nums):
        result = []
        path = []

        def backtrack(start):
            if len(path) >= 2:
                result.append(path[:])  # copy current path

            used = set()  # avoid duplicates at this level

            for i in range(start, len(nums)):
                # skip duplicates in same recursion level
                if nums[i] in used:
                    continue

                # ensure non-decreasing
                if path and nums[i] < path[-1]:
                    continue

                used.add(nums[i])
                path.append(nums[i])

                backtrack(i + 1)

                path.pop()  # backtrack

        backtrack(0)
        return result
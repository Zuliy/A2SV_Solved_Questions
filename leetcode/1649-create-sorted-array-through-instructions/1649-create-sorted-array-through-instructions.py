class Solution:
    def createSortedArray(self, instructions):
        MOD = 10**9 + 7
        max_val = max(instructions)

  
        BIT = [0] * (max_val + 1)

        def update(i):
            while i <= max_val:
                BIT[i] += 1
                i += i & -i

        def query(i):
            s = 0
            while i > 0:
                s += BIT[i]
                i -= i & -i
            return s

        cost = 0

        for x in instructions:
            less = query(x - 1)
            greater = query(max_val) - query(x)

            cost += min(less, greater)
            cost %= MOD

            update(x)

        return cost
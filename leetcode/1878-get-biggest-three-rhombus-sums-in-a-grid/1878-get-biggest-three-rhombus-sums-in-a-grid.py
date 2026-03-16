class Solution:
    def getBiggestThree(self, grid):
        m, n = len(grid), len(grid[0])
        sums = set()

        def rhombus_sum(i, j, k):
            if k == 0:
                return grid[i][j]

            total = 0

            x, y = i - k, j
            for d in range(k):
                total += grid[x + d][y + d]

            x, y = i, j + k
            for d in range(k):
                total += grid[x + d][y - d]

            x, y = i + k, j
            for d in range(k):
                total += grid[x - d][y - d]

            
            x, y = i, j - k
            for d in range(k):
                total += grid[x - d][y + d]

            return total

        for i in range(m):
            for j in range(n):
                max_k = min(i, j, m - 1 - i, n - 1 - j)
                for k in range(max_k + 1):
                    sums.add(rhombus_sum(i, j, k))

        return sorted(sums, reverse=True)[:3]
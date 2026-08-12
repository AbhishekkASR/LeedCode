class Solution:
    def maxProductPath(self, grid: List[List[int]]) -> int:
        MOD = 10**9 + 7
        m, n = len(grid), len(grid[0])

        max_dp = [[0] * n for _ in range(m)]
        min_dp = [[0] * n for _ in range(m)]
        max_dp[0][0] = min_dp[0][0] = grid[0][0]

        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue

                candidates = []

                if i > 0:
                    candidates.append(max_dp[i - 1][j] * grid[i][j])
                    candidates.append(min_dp[i - 1][j] * grid[i][j])

                if j > 0:
                    candidates.append(max_dp[i][j - 1] * grid[i][j])
                    candidates.append(min_dp[i][j - 1] * grid[i][j])

                max_dp[i][j] = max(candidates)
                min_dp[i][j] = min(candidates)

        ans = max_dp[m - 1][n - 1]
        return ans % MOD if ans >= 0 else -1

class Solution:
    def constructProductMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        MOD = 12345
        m, n = len(grid), len(grid[0])

        arr = []
        for row in grid:
            arr.extend(row)

        size = len(arr)
        prefix = [1] * size
        suffix = [1] * size

        for i in range(1, size):
            prefix[i] = (prefix[i - 1] * arr[i - 1]) % MOD

        for i in range(size - 2, -1, -1):
            suffix[i] = (suffix[i + 1] * arr[i + 1]) % MOD

        res = [[0] * n for _ in range(m)]
        idx = 0
        for i in range(m):
            for j in range(n):
                res[i][j] = (prefix[idx] * suffix[idx]) % MOD
                idx += 1

        return res
class Solution:
    def minSumOfLengths(self, arr, target):
        n = len(arr)
        INF = float('inf')

        best = [INF] * n
        ans = INF
        left = 0
        curr = 0

        for right in range(n):
            curr += arr[right]

            while curr > target and left <= right:
                curr -= arr[left]
                left += 1

            if curr == target:
                length = right - left + 1

                if left > 0 and best[left - 1] != INF:
                    ans = min(ans, length + best[left - 1])

                best[right] = length

            if right > 0:
                best[right] = min(best[right], best[right - 1])

        return -1 if ans == INF else ans
class Solution:
    def maximumWeight(self, intervals):
        import bisect

        n = len(intervals)

        arr = sorted(
            (l, r, w, idx)
            for idx, (l, r, w) in enumerate(intervals)
        )

        starts = [x[0] for x in arr]

        nxt = [0] * n
        for i in range(n):
            nxt[i] = bisect.bisect_right(starts, arr[i][1])

        dp = [[(0, ()) for _ in range(5)] for _ in range(n + 1)]

        for i in range(n - 1, -1, -1):
            for k in range(1, 5):
                skip_score, skip_ids = dp[i + 1][k]

                take_score, take_ids = dp[nxt[i]][k - 1]
                take_score += arr[i][2]
                take_ids = tuple(sorted(take_ids + (arr[i][3],)))

                if take_score > skip_score:
                    dp[i][k] = (take_score, take_ids)
                elif take_score < skip_score:
                    dp[i][k] = (skip_score, skip_ids)
                else:
                    dp[i][k] = (skip_score, min(take_ids, skip_ids))

        return list(dp[0][4][1])
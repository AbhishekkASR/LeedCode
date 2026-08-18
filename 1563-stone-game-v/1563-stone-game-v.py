from functools import cache
from itertools import accumulate

class Solution:
    def stoneGameV(self, stoneValue: List[int]) -> int:
        prefix = list(accumulate(stoneValue, initial=0))

        @cache
        def dp(l, r):
            if l >= r:
                return 0

            ans = 0
            left_sum = 0
            right_sum = prefix[r + 1] - prefix[l]

            for m in range(l, r):
                left_sum += stoneValue[m]
                right_sum -= stoneValue[m]

                if left_sum < right_sum:
                    if ans >= left_sum * 2:
                        continue

                    ans = max(
                        ans,
                        left_sum + dp(l, m)
                    )

                elif left_sum > right_sum:
                    if ans >= right_sum * 2:
                        break

                    ans = max(
                        ans,
                        right_sum + dp(m + 1, r)
                    )

                else:
                    ans = max(
                        ans,
                        left_sum + dp(l, m),
                        right_sum + dp(m + 1, r)
                    )

            return ans

        return dp(0, len(stoneValue) - 1)
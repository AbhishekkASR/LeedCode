from bisect import bisect_right

class Solution:
    def countElements(self, nums, k):
        arr = sorted(nums)
        n = len(arr)
        ans = 0

        for x in nums:
            if n - bisect_right(arr, x) >= k:
                ans += 1

        return ans
class Solution:
    def resultArray(self, nums, k):
        d = [0] * k
        ans = [0] * k
        
        for a in nums:
            a %= k
            nd = [0] * k
            nd[a] += 1

            for r in range(k):
                if d[r]:
                    nd[r * a % k] += d[r]

            d = nd
            
            for r in range(k):
                ans[r] += d[r]
        return ans
        
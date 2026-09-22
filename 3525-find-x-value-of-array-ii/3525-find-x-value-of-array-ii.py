class Solution:
    def resultArray(self, nums, k, queries):
        n = len(nums)

        size = 1
        while size < n:
            size <<= 1

        prod = [1] * (2 * size)
        cnt = [[0] * k for _ in range(2 * size)]

        # Build leaves
        for i, v in enumerate(nums):
            r = v % k
            prod[size + i] = r
            cnt[size + i][r] = 1

        # Build tree
        for i in range(size - 1, 0, -1):
            left = i << 1
            right = left | 1

            lp = prod[left]
            prod[i] = (lp * prod[right]) % k

            cur = cnt[left].copy()
            for r in range(k):
                cur[(lp * r) % k] += cnt[right][r]
            cnt[i] = cur

        def merge(A, B):
            pa, ca = A
            pb, cb = B

            res = ca.copy()
            for r in range(k):
                res[(pa * r) % k] += cb[r]

            return (pa * pb) % k, res

        def query(l, r):
            left_res = (1, [0] * k)
            right_res = (1, [0] * k)

            l += size
            r += size

            while l < r:
                if l & 1:
                    left_res = merge(
                        left_res, (prod[l], cnt[l])
                    )
                    l += 1

                if r & 1:
                    r -= 1
                    right_res = merge(
                        (prod[r], cnt[r]), right_res
                    )

                l >>= 1
                r >>= 1

            return merge(left_res, right_res)[1]

        result = []

        for index, value, start, x in queries:
            # Persistent point update
            pos = size + index
            remainder = value % k

            prod[pos] = remainder
            cnt[pos] = [0] * k
            cnt[pos][remainder] = 1

            pos >>= 1
            while pos:
                left = pos << 1
                right = left | 1

                lp = prod[left]
                prod[pos] = (lp * prod[right]) % k

                cur = cnt[left].copy()
                for r in range(k):
                    cur[(lp * r) % k] += cnt[right][r]

                cnt[pos] = cur
                pos >>= 1

            # Prefix products of nums[start...n-1]
            result.append(query(start, n)[x])

        return result
class Solution:
    def smallestPalindrome(self, s, k):
        from collections import Counter
        from math import comb

        c = Counter(s)
        h = []
        m = ''

        for x in sorted(c):
            if c[x] & 1:
                m = x
            h.append(x * (c[x] // 2))

        h = ''.join(h)
        n = len(h)
        a = Counter(h)

        def ways():
            r = 1
            t = n
            for v in a.values():
                r *= comb(t, v)
                t -= v
                if r >= k:
                    return k
            return r

        if ways() < k:
            return ''

        r = []

        for i in range(n):
            for x in sorted(a):
                if not a[x]:
                    continue

                a[x] -= 1
                t = n - i - 1
                w = 1

                for v in a.values():
                    w *= comb(t, v)
                    t -= v
                    if w >= k:
                        break

                if k > w:
                    k -= w
                    a[x] += 1
                else:
                    r.append(x)
                    break

        p = ''.join(r)
        return p + m + p[::-1]
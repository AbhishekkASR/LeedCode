class Solution:
    def addBinary(self, a, b):
        i, j = len(a) - 1, len(b) - 1
        carry = 0
        res = []

        while i >= 0 or j >= 0 or carry:
            s = carry
            if i >= 0:
                s += a[i] == '1'
                i -= 1
            if j >= 0:
                s += b[j] == '1'
                j -= 1

            res.append('1' if s & 1 else '0')
            carry = s >> 1

        return ''.join(reversed(res))

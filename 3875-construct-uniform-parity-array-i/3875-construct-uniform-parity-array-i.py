class Solution:
    def uniformArray(self, nums1):
        has_even = any(x % 2 == 0 for x in nums1)
        has_odd = any(x % 2 != 0 for x in nums1)

        # All elements already have the same parity
        if not (has_even and has_odd):
            return True

        return True
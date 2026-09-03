class Solution:
    def uniformArray(self, nums1):
        has_odd = [x for x in nums1 if x % 2 == 1]
        has_even = [x for x in nums1 if x % 2 == 0]

        # Already uniform
        if not has_odd or not has_even:
            return True

        # Make all elements odd:
        # every even element needs a smaller odd element to subtract.
        smallest_odd = min(has_odd)

        return all(x > smallest_odd for x in has_even)
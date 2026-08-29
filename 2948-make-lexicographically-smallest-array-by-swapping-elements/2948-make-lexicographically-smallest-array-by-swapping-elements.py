class Solution:
    def lexicographicallySmallestArray(self, nums, limit):
        n = len(nums)

        # (value, original index)
        arr = sorted((nums[i], i) for i in range(n))

        result = [0] * n
        i = 0

        while i < n:
            j = i

            # Find a connected group of values
            while j + 1 < n and arr[j + 1][0] - arr[j][0] <= limit:
                j += 1

            # Indices belonging to this group
            indices = sorted(arr[k][1] for k in range(i, j + 1))

            # Values are already sorted
            for k in range(j - i + 1):
                result[indices[k]] = arr[i + k][0]

            i = j + 1

        return result
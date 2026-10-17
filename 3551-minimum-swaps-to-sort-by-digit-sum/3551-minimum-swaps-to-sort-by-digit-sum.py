class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        def digit_sum(n):
            total = 0
            while n:
                total += n % 10
                n //= 10
            return total

        sorted_nums = sorted(nums, key=lambda x: (digit_sum(x), x))
        pos = {num: i for i, num in enumerate(nums)}
        visited = [False] * len(nums)
        ans = 0

        for i in range(len(nums)):
            if visited[i] or pos[sorted_nums[i]] == i:
                visited[i] = True
                continue

            cycle_size = 0
            j = i

            while not visited[j]:
                visited[j] = True
                j = pos[sorted_nums[j]]
                cycle_size += 1

            ans += cycle_size - 1

        return ans
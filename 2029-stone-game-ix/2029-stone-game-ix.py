class Solution:
    def stoneGameIX(self, stones: List[int]) -> bool:
        cnt = [0, 0, 0]

        for x in stones:
            cnt[x % 3] += 1

        # If the number of 0-mod-3 stones is even,
        # Alice needs at least one 1-mod-3 and one 2-mod-3 stone.
        if cnt[0] % 2 == 0:
            return cnt[1] > 0 and cnt[2] > 0

        # If the number of 0-mod-3 stones is odd,
        # the counts of 1-mod-3 and 2-mod-3 stones
        # must differ by at least 3.
        return abs(cnt[1] - cnt[2]) > 2
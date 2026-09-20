class Solution:
    def reverseDegree(self, s: str) -> int:
        total = 0
        for i, ch in enumerate(s, 1):
            value = 26 - (ord(ch) - ord('a'))
            total += value * i

        return total


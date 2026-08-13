from typing import List

class Solution:
    def longestRepeating(self, s: str, queryCharacters: str, queryIndices: List[int]) -> List[int]:
        n = len(s)
        arr = list(s)

        size = 4 * n
        lchar = [''] * size
        rchar = [''] * size
        pref = [0] * size
        suff = [0] * size
        best = [0] * size
        length = [0] * size

        def build(node: int, l: int, r: int) -> None:
            if l == r:
                c = arr[l]
                lchar[node] = rchar[node] = c
                pref[node] = suff[node] = best[node] = 1
                length[node] = 1
                return
            mid = (l + r) // 2
            build(node * 2, l, mid)
            build(node * 2 + 1, mid + 1, r)
            pull(node)

        def pull(node: int) -> None:
            left = node * 2
            right = left + 1

            length[node] = length[left] + length[right]
            lchar[node] = lchar[left]
            rchar[node] = rchar[right]

            pref[node] = pref[left]
            if pref[left] == length[left] and rchar[left] == lchar[right]:
                pref[node] = length[left] + pref[right]

            suff[node] = suff[right]
            if suff[right] == length[right] and rchar[left] == lchar[right]:
                suff[node] = length[right] + suff[left]

            best[node] = max(best[left], best[right])
            if rchar[left] == lchar[right]:
                best[node] = max(best[node], suff[left] + pref[right])

        def update(node: int, l: int, r: int, idx: int, ch: str) -> None:
            if l == r:
                arr[idx] = ch
                lchar[node] = rchar[node] = ch
                pref[node] = suff[node] = best[node] = 1
                return
            mid = (l + r) // 2
            if idx <= mid:
                update(node * 2, l, mid, idx, ch)
            else:
                update(node * 2 + 1, mid + 1, r, idx, ch)
            pull(node)

        build(1, 0, n - 1)

        ans = []
        for ch, idx in zip(queryCharacters, queryIndices):
            update(1, 0, n - 1, idx, ch)
            ans.append(best[1])

        return ans
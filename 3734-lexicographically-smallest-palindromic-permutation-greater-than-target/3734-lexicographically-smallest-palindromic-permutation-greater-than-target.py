class Solution:
    def lexPalindromicPermutation(self, s: str, target: str) -> str:
        n = len(s)
        h = n // 2

        cnt = [0] * 26
        for ch in s:
            cnt[ord(ch) - 97] += 1

        # Check palindrome possibility
        odd = 0
        middle = ''

        for i in range(26):
            if cnt[i] % 2:
                odd += 1
                middle = chr(i + 97)

        if odd > 1:
            return ""

        # Frequency for left half
        avail = [x // 2 for x in cnt]
        left = [''] * h

        # Match target's left half
        i = 0

        while i < h:
            c = ord(target[i]) - 97

            if avail[c] == 0:
                break

            left[i] = target[i]
            avail[c] -= 1
            i += 1

        # Fill remaining positions with smallest characters
        def fill(start):
            p = start
            for c in range(26):
                while avail[c]:
                    left[p] = chr(c + 97)
                    avail[c] -= 1
                    p += 1

        def make_palindrome():
            return ''.join(left) + middle + ''.join(left[::-1])

        # Matching failed before reaching the end
        if i < h:

            t = ord(target[i]) - 97

            # Try making this position larger
            for c in range(t + 1, 26):
                if avail[c]:
                    left[i] = chr(c + 97)
                    avail[c] -= 1
                    fill(i + 1)
                    return make_palindrome()

            # Backtrack
            for pos in range(i - 1, -1, -1):

                old = ord(left[pos]) - 97
                avail[old] += 1

                t = ord(target[pos]) - 97

                for c in range(t + 1, 26):
                    if avail[c]:
                        left[pos] = chr(c + 97)
                        avail[c] -= 1
                        fill(pos + 1)
                        return make_palindrome()

            return ""

        # Left half exactly matches target's left half
        candidate = make_palindrome()

        if candidate > target:
            return candidate

        # Find next permutation of the left half
        pos = h - 2

        while pos >= 0 and left[pos] >= left[pos + 1]:
            pos -= 1

        if pos < 0:
            return ""

        j = h - 1

        while left[j] <= left[pos]:
            j -= 1

        left[pos], left[j] = left[j], left[pos]

        left[pos + 1:] = reversed(left[pos + 1:])

        candidate = make_palindrome()

        # IMPORTANT: verify it is actually greater
        if candidate > target:
            return candidate

        return ""
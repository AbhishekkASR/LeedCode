class Solution {
    public String lexGreaterPermutation(String s, String target) {
        int n = s.length();
        int[] freq = new int[26];

        for (char c : s.toCharArray()) {
            freq[c - 'a']++;
        }

        StringBuilder prefix = new StringBuilder();

        for (int i = 0; i < n; i++) {
            int t = target.charAt(i) - 'a';

            // Exact match is possible
            if (freq[t] > 0) {
                freq[t]--;
                prefix.append(target.charAt(i));
                continue;
            }

            // Exact match isn't possible.
            // Try to make this position larger.
            for (int c = t + 1; c < 26; c++) {
                if (freq[c] > 0) {
                    return buildAnswer(prefix, c, freq);
                }
            }

            // Can't make this position larger either.
            // Backtrack.
            while (prefix.length() > 0) {
                int last = prefix.length() - 1;
                int lastChar = prefix.charAt(last) - 'a';

                freq[lastChar]++;
                prefix.deleteCharAt(last);

                int targetChar = target.charAt(last) - 'a';

                for (int c = targetChar + 1; c < 26; c++) {
                    if (freq[c] > 0) {
                        return buildAnswer(prefix, c, freq);
                    }
                }
            }

            return "";
        }

        // s == target, so find the next larger permutation.
        while (prefix.length() > 0) {
            int last = prefix.length() - 1;
            int lastChar = prefix.charAt(last) - 'a';

            freq[lastChar]++;
            prefix.deleteCharAt(last);

            int targetChar = target.charAt(last) - 'a';

            for (int c = targetChar + 1; c < 26; c++) {
                if (freq[c] > 0) {
                    return buildAnswer(prefix, c, freq);
                }
            }
        }

        return "";
    }

    private String buildAnswer(StringBuilder prefix, int c, int[] freq) {
        StringBuilder ans = new StringBuilder(prefix);

        ans.append((char) ('a' + c));
        freq[c]--;

        // Put remaining characters in ascending order.
        for (int i = 0; i < 26; i++) {
            while (freq[i] > 0) {
                ans.append((char) ('a' + i));
                freq[i]--;
            }
        }

        return ans.toString();
    }
}
class Solution {
public:
    bool sumGame(string num) {
        int n = num.size();

        int diff = 0;
        int qDiff = 0;

        // First half
        for (int i = 0; i < n / 2; i++) {
            if (num[i] == '?') {
                qDiff++;
            } else {
                diff += num[i] - '0';
            }
        }

        // Second half
        for (int i = n / 2; i < n; i++) {
            if (num[i] == '?') {
                qDiff--;
            } else {
                diff -= num[i] - '0';
            }
        }

        // Odd number of '?' means Alice can always force a win.
        if (qDiff % 2 != 0)
            return true;

        // Bob can win only if the current difference can
        // exactly be compensated by the '?' characters.
        return diff != -qDiff * 9 / 2;
    }
};
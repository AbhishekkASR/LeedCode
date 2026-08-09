class Solution {
public:
    int n;
    vector<int> suffix;
    int memo[101][101];

    int solve(int i, int M) {
        if (i >= n) return 0;

        // If we can take all remaining piles
        if (i + 2 * M >= n)
            return suffix[i];

        if (memo[i][M] != -1)
            return memo[i][M];

        int ans = 0;

        for (int X = 1; X <= 2 * M; X++) {
            ans = max(ans, suffix[i] - solve(i + X, max(M, X)));
        }

        return memo[i][M] = ans;
    }

    int stoneGameII(vector<int>& piles) {
        n = piles.size();

        suffix.resize(n);
        suffix[n - 1] = piles[n - 1];
        for (int i = n - 2; i >= 0; i--) {
            suffix[i] = suffix[i + 1] + piles[i];
        }

        memset(memo, -1, sizeof(memo));

        return solve(0, 1);
    }
};
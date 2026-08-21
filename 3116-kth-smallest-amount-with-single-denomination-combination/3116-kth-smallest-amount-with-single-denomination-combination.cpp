class Solution {
public:
    using ll = long long;

    ll gcd(ll a, ll b) {
        while (b) {
            ll t = a % b;
            a = b;
            b = t;
        }
        return a;
    }

    ll lcm(ll a, ll b) {
        return a / gcd(a, b) * b;
    }

    // Count how many distinct numbers <= x
    // are divisible by at least one coin.
    ll count(ll x, vector<int>& coins) {
        int n = coins.size();
        ll ans = 0;

        for (int mask = 1; mask < (1 << n); mask++) {
            ll multiple = 1;
            int bits = 0;
            bool valid = true;

            for (int i = 0; i < n; i++) {
                if (mask & (1 << i)) {
                    bits++;

                    multiple = lcm(multiple, (ll)coins[i]);

                    if (multiple > x) {
                        valid = false;
                        break;
                    }
                }
            }

            if (!valid)
                continue;

            ll cnt = x / multiple;

            if (bits % 2 == 1)
                ans += cnt;
            else
                ans -= cnt;
        }

        return ans;
    }

    long long findKthSmallest(vector<int>& coins, int k) {
        // Remove duplicate denominations
        sort(coins.begin(), coins.end());
        coins.erase(unique(coins.begin(), coins.end()), coins.end());

        // Remove coins that are multiples of a smaller coin.
        // Example: [2, 4, 8] -> [2]
        vector<int> filtered;

        for (int i = 0; i < coins.size(); i++) {
            bool redundant = false;

            for (int j = 0; j < filtered.size(); j++) {
                if (coins[i] % filtered[j] == 0) {
                    redundant = true;
                    break;
                }
            }

            if (!redundant)
                filtered.push_back(coins[i]);
        }

        coins = filtered;

        ll low = 1;
        ll high = 1LL * (*min_element(coins.begin(), coins.end())) * k;

        while (low < high) {
            ll mid = low + (high - low) / 2;

            if (count(mid, coins) >= k) {
                high = mid;
            } else {
                low = mid + 1;
            }
        }

        return low;
    }
};
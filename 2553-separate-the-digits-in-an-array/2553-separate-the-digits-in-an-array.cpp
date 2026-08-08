class Solution {
public:
    vector<int> separateDigits(vector<int>& nums) {
        vector<int> ans;
        for (int x : nums) {
            if (x == 0) {
                ans.push_back(0);
                continue;
            }
            vector<int> digits;
            while (x > 0) {
                digits.push_back(x % 10);
                x /= 10;
            }
            reverse(digits.begin(), digits.end());
            ans.insert(ans.end(), digits.begin(), digits.end());
        }
        return ans;
    }
};
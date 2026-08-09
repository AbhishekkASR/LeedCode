class Solution {
public:
    vector<string> findRestaurant(vector<string>& list1, vector<string>& list2) {
        unordered_map<string, int> mp;

        // Store index of each restaurant in list1
        for (int i = 0; i < list1.size(); i++) {
            mp[list1[i]] = i;
        }

        vector<string> ans;
        int minSum = INT_MAX;

        // Check common restaurants in list2
        for (int j = 0; j < list2.size(); j++) {
            if (mp.count(list2[j])) {
                int sum = mp[list2[j]] + j;

                if (sum < minSum) {
                    minSum = sum;
                    ans.clear();
                    ans.push_back(list2[j]);
                } else if (sum == minSum) {
                    ans.push_back(list2[j]);
                }
            }
        }

        return ans;
    }
};
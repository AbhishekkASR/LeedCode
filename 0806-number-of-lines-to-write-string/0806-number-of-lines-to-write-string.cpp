class Solution {
public:
    vector<int> numberOfLines(vector<int>& widths, string s) {
        int lines = 1;
        int currentWidth = 0;

        for (char ch : s) {
            int w = widths[ch - 'a'];

            if (currentWidth + w <= 100) {
                currentWidth += w;
            } else {
                lines++;
                currentWidth = w;
            }
        }

        return {lines, currentWidth};
    }
};
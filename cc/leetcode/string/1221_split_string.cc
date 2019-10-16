class Solution {
public:
    int balancedStringSplit(string s) {
        int curr = 0, result = 0;
        for (char c : s) {
            if (c == 'L')
                curr++;
            else
                curr--;
            if (curr == 0)
                result++;
        }
        return result;
    }
};

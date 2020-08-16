class Solution {
public:
    bool threeConsecutiveOdds(vector<int>& arr) {
        int sum = 0;
        for (int item : arr) {
            if (item % 2 == 0)
                sum = 0;
            else {
                sum++;
                if (sum == 3)
                    return true;
            }
        }
        return false;
    }
};

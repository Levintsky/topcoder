#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        vector<int> cum = {0};
        int min_ = 0;
        int best = nums[0];
        int max_neg = INT_MIN;
        for (auto i : nums) {
        	int n = cum.size();
        	cum.push_back(cum[n-1] + i);
        	best = max(best, cum[n]-min_);
        	min_ = min(min_, cum[n]);
            if (i < 0)
                max_neg = max(i, max_neg);
        }

        if (best > 0)
        	return best;
        else
        	return max_neg;
    }
};

int main() {
	Solution a;
	vector<int> nums = {-2,1,-3,4,-1,2,1,-5,4};
    cout << a.maxSubArray(nums) << endl;

	return 0;
}
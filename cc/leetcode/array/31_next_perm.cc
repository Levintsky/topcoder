class Solution {
public:
    void nextPermutation(vector<int>& nums) {
        int n = nums.size();
        int i;
        int k;

        for (i=n-2; i>=0; i--) {
            if (nums[i] < nums[i+1])
                break;
        }
        if (i < 0) {
            std::reverse(nums.begin(), nums.end());
            return;
        }
        for (k=n-1; nums[k]<=nums[i];k--)
            ;
        cout << i << k;
        swap(nums[i], nums[k]);
        std::reverse(nums.begin()+i+1, nums.end());
    }
};

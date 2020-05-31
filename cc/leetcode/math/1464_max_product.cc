class Solution {
public:
    int maxProduct(vector<int>& nums) {
        int max_1= nums[0], max_2=nums[1];
        if (max_1 < max_2)
            swap(max_1, max_2);
        for (int i=2; i < nums.size(); ++i) {
            if (nums[i] >= max_1) {
                max_2 = max_1;
                max_1 = nums[i];
            } else if (nums[i] > max_2)
                max_2 = nums[i];
        }
        return (max_1-1) * (max_2-1);
    }
};

class NumArray {
public:
    vector<int> cum;
    NumArray(vector<int>& nums) {
        cum.push_back(0);
        for (auto item : nums)
            cum.push_back(cum.back() + item);
    }
    
    int sumRange(int i, int j) {
        return cum[j+1] - cum[i];
    }
};

/**
 * Your NumArray object will be instantiated and called as such:
 * NumArray* obj = new NumArray(nums);
 * int param_1 = obj->sumRange(i,j);
 */
class Solution {
public:
    int kConcatenationMaxSum(vector<int>& arr, int k) {
        long MOD = pow(10, 9) + 7;
        int min_ = arr[0], max_ = arr[0];
        long tmpsum = 0;
        for (int item : arr) {
            min_ = min(item, min_);
            max_ = max(item, max_);
            tmpsum += item;
        }
        // all neg
        if (max_ <= 0)
            return 0;
        // all pos
        if (min_ >= 0)
            return tmpsum * k % MOD;
        // now contains pos and neg
        if (k == 1)
            return helper_anymax(arr);
        
        vector<int> arr_inv(arr);
        reverse(arr_inv.begin(), arr_inv.end());
        cout << helper_halfmax(arr) << " " << helper_halfmax(arr_inv) << endl;
        long res = helper_halfmax(arr) + helper_halfmax(arr_inv);
        if (tmpsum > 0) {
            res += tmpsum * (k-2);
        }
        return max(res % MOD, long(helper_anymax(arr)));
    }
    
    int helper_anymax(vector<int>& arr) {
        // return maximum of any subarray
        int min_ = 0, curr = 0;
        int res = 0;
        for (int item : arr) {
            curr += item;
            min_ = min(curr, min_);
            // possible max: max(res, curr - min_, item)
            res = max(res, curr-min_);
        }
        return res;
    }
    int helper_halfmax(vector<int>& arr) {
        // return maximum of array start from the beginning
        int curr = 0, res = 0;
        for (int item : arr) {
            curr += item;
            res = max(curr, res);
        }
        return res;
    }
};

class Solution {
public:
    int maximumSum(vector<int>& arr) {
        int min_ = arr[0], max_ = arr[0];
        for (int item : arr) {
            min_ = min(min_, item);
            max_ = max(max_, item);
        }
        if (min_ >= 0) {
            int res = 0;
            for (int item : arr)
                res += item;
            return res;
        }
        if (max_ <= 0)
            return max_;
        
        // now must contain positive and negative
        int curr_ori = arr[0], curr_del = 0, result = 0;
        for (int i = 1; i < arr.size(); ++i) {
            int item = arr[i];
            int new_ori = max(curr_ori+item, item);
            int new_del = max(curr_ori, curr_del+item);
            result = max(result, max(new_ori, new_del));
            curr_ori = new_ori;
            curr_del = new_del;
        }
        return result;
    }
};

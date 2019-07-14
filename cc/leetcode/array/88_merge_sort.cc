class Solution {
public:
    void merge(vector<int>& nums1, int m, vector<int>& nums2, int n) {
        vector<int> res;
        int i = m - 1;
        int j = n - 1;
        int cnt = m + n - 1;
        while (i >= 0 || j >= 0) {
            if (j < 0 || (i >= 0 && nums1[i] >= nums2[j])) {
                nums1[cnt] = nums1[i];
                --i;
            } else {
                nums1[cnt] = nums2[j];
                --j;
            }
            cnt--;
        }
    }
};
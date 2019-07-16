class Solution {
public:
    int maxChunksToSorted(vector<int>& arr) {
        // vector<int> arr2 = arr;
        // sort(arr2.begin(), arr2.end());
        unordered_set<int> s1, s2;
        int n = arr.size();
        int res = 0;
        int i = 0, j;
        while (i < n) {
            j = i;
            while (j < n) {
                s1.insert(arr[j]);
                s2.insert(j);
                if (s1 == s2)
                    break;
                j++;
            }
            res++;
            i = j + 1;
            s1.clear();
            s2.clear();
        }
        return res;
    }
};

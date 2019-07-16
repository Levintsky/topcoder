class Solution {
public:
    void duplicateZeros(vector<int>& arr) {
        // step 1: get last non-zero
        int n = arr.size();
        int i = 0, j = 0, last_i = -1, last_j = -1;
        while (i < n && j < n) {
            if (arr[i] == 0) {
                i++;
                j += 2;
            } else {
                last_i = i;
                last_j = j;
                i++;
                j++;
            }
        }
        if (last_i == -1)
            return;
        // step 2: go backwards
        for (i = last_j+1; i < n; ++i)
            arr[i] = 0;
        for(i = last_i, j = last_j; i >= 0; ) {
            if (arr[i] != 0) {
                arr[j] = arr[i];
                j--;
                i--;
            } else {
                arr[j--] = 0;
                arr[j--] = 0;
                i--;
            }
        }
    }
};

// less error prone
class Solution {
public:
    void duplicateZeros(vector<int>& arr) {
        // step 1: get last non-zero
        int n = arr.size();
        vector<int> arr2(n, 0);
        int i = 0, j = 0;
        while (i < n && j < n) {
            if (arr[i] != 0) {
                arr2[j] = arr[i];
                j++;
            } else
                j += 2;
            
            i++;
        }
        for (int i = 0; i < n; ++i)
            arr[i] = arr2[i];
    }
};

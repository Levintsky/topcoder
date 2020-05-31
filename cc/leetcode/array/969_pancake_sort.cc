class Solution {
public:
    vector<int> pancakeSort(vector<int>& A) {
        vector<int> result;
        int n = A.size();
        for (int i = n - 1; i >= 0; i--) {
            // find max index
            int max_idx = i;
            for (int j = i - 1; j >= 0; j--) {
                if (A[j] > A[max_idx])
                    max_idx = j;
            }
            if (max_idx == i)
                continue;
            // swap: [0..j]
            reverse(A.begin(), A.begin()+max_idx+1);
            reverse(A.begin(), A.begin()+i+1);
            /*for (int k = 0; k < 4; ++k)
                cout << A[k] << " ";
            cout << endl;*/
            result.push_back(max_idx+1);
            result.push_back(i+1);
        }
        return result;
    }
};

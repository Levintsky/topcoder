class Solution {
public:
    int oddEvenJumps(vector<int>& A) {
        int n = A.size();
        vector<bool> higher(n, false), lower(n, false);
        higher[n-1] = true;
        lower[n-1] = true;
        
        map<int, int> memo;
        memo[A[n-1]] = n-1;
        
        for (int i=n-2; i >= 0; --i) {
            auto it = memo.lower_bound(A[i]);
            if (it != end(memo)) {
                higher[i] = lower[it->second];
                if (it->first == A[i])
                    ++it;
            }
            if (it != begin(memo))
                lower[i] = higher[prev(it)->second];
            memo[A[i]] = i;
        }
        
        int result = 0;
        for (bool item : higher) {
            if (item)
                result++;
        }
        return result;
    }
};

class Solution {
public:
    unordered_map<string, double> memo;
    double comb(int n, int k) {
        string s = to_string(n) + " " + to_string(k);
        // cout << s << endl;
        if (memo.find(s) != memo.end())
            return memo[s];
        if (k == 0)
            return 1;
        if (k == 1)
            return n;
        if (k == n)
            return 1;
        double result = comb(n-1, k-1) + comb(n-1, k);
        memo[s] = result;
        return result;
    }
    void dfs(vector<int>& curr,
             vector<int>& remain,
             const vector<int>& balls,
             int idx, int target, double& valid) {
        int n = balls.size();
        if (idx == n-1 ) {
            // check valid: enough balls
            if (target > balls[n-1])
                return;
            curr[n-1] = target;
            remain[n-1] = balls[n-1] - curr[n-1];
            // check valid: same color
            int c1 = 0, c2 = 0;
            for (int i = 0; i < n; ++i) {
                if (curr[i] == 0)
                    c1++;
                if (remain[i] == 0)
                    c2++;
            }
            if (c1 != c2)
                return;
            // count
            float result = 1;
            // cout << curr;

            for (int i = 0; i < n; ++i) {
                if(balls[i] < curr[i])
                    break;
                result *= comb(balls[i], curr[i]);
            }
            // cout << result << endl;
            valid += result;
        } else {
            for (int i = 0; i < min(balls[idx], target)+1; ++i) {
                curr[idx] = i;
                remain[idx] = balls[idx] - i;
                dfs(curr, remain, balls, idx+1, target-i, valid);
            }
        }
        
    }
    
    double getProbability(vector<int>& balls) {
        int total = 0, half;
        
        for (int item : balls)
            total += item;
        half = total / 2;
        long long comb_all = comb(total, half);
        cout << comb_all;
        
        int n = balls.size();
        vector<int> curr(n);
        vector<int> remain(n);
        double valid = 0.;
        
        dfs(curr, remain, balls, 0, half, valid);
        double result = valid / comb_all;
        return result;
    }
};

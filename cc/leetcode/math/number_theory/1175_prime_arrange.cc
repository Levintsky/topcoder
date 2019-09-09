class Solution {
public:
    int numPrimeArrangements(int n) {
        if (n <= 1)
            return 1;
        // count prime
        int n_prime = 0, n_non = 0;
        vector<bool> arr(n+1, true); // prime or not
        arr[0] = arr[1] = false;
        long MOD = pow(10, 9) + 7;
        
        for (int i = 2; i <= n/2; ++i) {
            for (int j = 2; i * j <= n; ++j) 
                arr[i*j] = false;
        }
        for (int i = 1; i < n+1; ++i) {
            if (arr[i])
                n_prime++;
            else
                n_non++;
        }
        long result = (factor(n_prime) * factor(n_non)) % MOD;
        return result;
    }
    
    long factor(int i) {
        long MOD = pow(10, 9) + 7;
        long res = 1;
        while (i > 1) {
            res = (res * i) % MOD;
            i--;
        }
        return res;
    }
};

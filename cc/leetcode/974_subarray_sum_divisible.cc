class Solution(object):
    def subarraysDivByK(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        memo = {0: [-1]}
        tmp = 0
        res = 0
        for i, item in enumerate(A):
            tmp = (tmp + item) % K
            if tmp in memo:
                res += len(memo[tmp])
            if tmp not in memo:
                memo[tmp] = []
            memo[tmp].append(i)
        return res

    // better solution
    int subarraysDivByK(vector<int>& A, int K) {
        int n = A.size();
        if(n == 0){
            return 0;
        }
        vector<int> buckets(K, 0);
        buckets[0] = 1;
        int sum = 0;
        for(int i = 0; i < n; ++i){
            sum += A[i];
            int mod;
            if(sum >= 0){
                mod = sum % K;
            }
            else{
                mod = K - ((-sum) % K);
                if(mod == K){
                    mod = 0;
                }
            }
            ++buckets[mod];
        }
        
        int ans = 0;
        for(int i = 0; i < K; ++i){
            ans += buckets[i] * (buckets[i] - 1) / 2;
        }
        return ans;
    }

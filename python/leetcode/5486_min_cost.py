import bisect

class Solution(object):
    def minCost(self, n, cuts):
        """
        :type n: int
        :type cuts: List[int]
        :rtype: int
        """
        cuts.sort()
        self.memo = {}
        # return self.helper(0, n, cuts)
        res = self.dp(0, n, cuts)
        return res

    def gen_key(self, left, right, cuts):
        key = [left, right] + cuts
        key = tuple([item-left for item in key])
        return key


    def dp(self, left, right, cuts):
        if len(cuts) == 0:
            return 0
        if len(cuts) == 1:
            return right - left
        # generate key
        key = self.gen_key(left, right, cuts)
        if key in self.memo:
            return self.memo[key]

        # bound = self.helper(left, right, cuts)
        n = len(cuts)
        best_res = (right - left) * n
        for i in range(n):
            res = right - left
            mid = cuts[i]
            res += self.dp(left, mid, cuts[:i])
            res += self.dp(mid, right, cuts[i+1:])
            best_res = min(res, best_res)
        self.memo[key] = best_res
        return self.memo[key]
    
    def helper(self, left, right, cuts):
        if len(cuts) == 0:
            return 0
        if len(cuts) == 1:
            return right - left
        
        mid = (left + right) // 2
        ind = bisect.bisect_left(cuts, mid)
        
        def get_score(left, right, v):
            return max(v-left, right-v)
            
        ind1 = min(ind, len(cuts)-1)
        ind2 = max(0, ind-1)
        score1 = get_score(left, right, cuts[ind1])
        score2 = get_score(left, right, cuts[ind2])
        if score1 <= score2:
            # perform at cuts[ind]
            ind = ind1
        else:
            ind = ind2
        
        res = right - left
        mid = cuts[ind]
        res += self.helper(left, mid, cuts[:ind])
        res += self.helper(mid, right, cuts[ind+1:])
        return res


if __name__ == "__main__":
    a = Solution()
    print(a.minCost(7, [1,3,4,5]))
    print(a.minCost(9, [5,6,1,4,2]))
    print(a.minCost(10, [7,8,9,2,1]))

    print(a.minCost(30, [18,15,13,7,5,26,25,29]))
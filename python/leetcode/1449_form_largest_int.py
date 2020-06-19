class Solution(object):
    def largestNumber(self, cost, target):
        """
        :type cost: List[int]
        :type target: int
        :rtype: str
        """
        min_cost = min(cost)
        while min_cost > 1:
            res = [item % min_cost for item in cost]
            if max(res) == 0:
                break
            else:
                min_cost -= 1
        
        if target % min_cost > 0:
            return "0"
        
        # cost_backup = [item for item in cost]
        cost_memo = {}
        for i, c in enumerate(cost):
            cost_memo[c] = i+1

        cost = list(set(cost))
        cost.sort()
        memo = [0] * len(cost)
        self.best = [0] * len(cost)
        self.flag = False
        self.result = "0"
        
        cost_key = list(cost_memo.keys())
        cost_key.sort()
        cost_val = [cost_memo[k] for k in cost_key]

        def generate_result(tmpmemo):
            result = []
            for i in range(len(tmpmemo)):
                result += [cost_val[i]] * tmpmemo[i]
            result.sort(reverse=True)
            result = [str(c) for c in result]
            return "".join(result)

        def backtrack(idx, t):
            # work on the idx-th
            # print('work on idx: ', idx)
            
            # edge case 0:
            if t == 0:
                self.flag = True
                if sum(memo) > sum(self.best):
                    self.best = [item for item in memo]
                    self.result = generate_result(memo)
                elif sum(memo) == sum(self.best):
                    result = generate_result(memo)
                    self.result = max(result, self.result)
                return
            # edge case 1:
            if cost[idx] > t: # not doable
                return
            # edge case 2:
            if idx == len(cost) - 1:
                if t % cost[idx] == 0:
                    self.flag = True
                    memo[idx] = t // cost[idx]
                    if sum(memo) > sum(self.best):
                        self.best = [item for item in memo]
                        self.result = generate_result(memo)
                    elif sum(memo) == sum(self.best):
                        result = generate_result(memo)
                        self.result = max(result, self.result)
                    memo[idx] = 0
                return
            # case 3:
            max_ = t // cost[idx]
            for item in range(max_, -1, -1):
                memo[idx] = item
                t_res = t - cost[idx] * item
                # potential
                potential = sum(memo) + t_res // cost[idx+1]
                if potential < sum(self.best):
                    break
                else:
                    backtrack(idx+1, t_res)
            memo[idx] = 0
            return
        
        backtrack(0, target)
        # print(self.best)
        # print(cost_memo)
        if not self.flag:
            return "0"

        
        # print(cost_val)

        
        return self.result


if __name__ == "__main__":
    a = Solution()
    """
    print(a.largestNumber([4,3,2,5,6,7,2,5,5], 9))
    print(a.largestNumber([7,6,5,5,5,6,8,7,8], 12))
    print(a.largestNumber([2,4,6,2,4,6,4,4,4], 5))
    print(a.largestNumber([6,10,15,40,40,40,40,40,40], 47))
    print(a.largestNumber([1,1,1,1,1,1,1,3,2], 10))
    print(a.largestNumber([5,6,7,3,4,6,7,4,8], 29))
    """
    print(a.largestNumber([15,11,12,14,10,6,15,6,15], 49))

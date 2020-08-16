"""
1553. Minimum Number of Days to Eat N Oranges (Hard)

There are n oranges in the kitchen and you decided to eat some of these oranges every day as follows:

Eat one orange.
If the number of remaining oranges (n) is divisible by 2 then you can eat  n/2 oranges.
If the number of remaining oranges (n) is divisible by 3 then you can eat  2*(n/3) oranges.
You can only choose one of the actions per day.

Return the minimum number of days to eat n oranges.

 

Example 1:

Input: n = 10
Output: 4
Explanation: You have 10 oranges.
Day 1: Eat 1 orange,  10 - 1 = 9.  
Day 2: Eat 6 oranges, 9 - 2*(9/3) = 9 - 6 = 3. (Since 9 is divisible by 3)
Day 3: Eat 2 oranges, 3 - 2*(3/3) = 3 - 2 = 1. 
Day 4: Eat the last orange  1 - 1  = 0.
You need at least 4 days to eat the 10 oranges.
Example 2:

Input: n = 6
Output: 3
Explanation: You have 6 oranges.
Day 1: Eat 3 oranges, 6 - 6/2 = 6 - 3 = 3. (Since 6 is divisible by 2).
Day 2: Eat 2 oranges, 3 - 2*(3/3) = 3 - 2 = 1. (Since 3 is divisible by 3)
Day 3: Eat the last orange  1 - 1  = 0.
You need at least 3 days to eat the 6 oranges.
Example 3:

Input: n = 1
Output: 1
Example 4:

Input: n = 56
Output: 6
 

Constraints:

1 <= n <= 2*10^9
"""


import collections

import pdb

class Solution(object):
    def minDays(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        # get memo
        memo = {n: 0}
        q = collections.deque([n])

        cum = [0] * min(n, 2001) # 1000 - min(3000, n)

        # 1000 - 3000 section
        while sum(cum) == len(cum):
            # pdb.set_trace()
            q2 = set()
            while len(q) > 0:
                item = q.popleft()
                if item >= 1000 and item <= min(3000, n): # all covered
                    cum[item-1000] = 1
                    continue
                # /2
                if item % 2 == 0:
                    # tmp, res = item // 2, item % 2
                    tmp = item // 2
                    if tmp in memo and memo[tmp] <= memo[item] - 1:
                        pass
                    else:
                        memo[tmp] = memo[item]+1
                        q2.add(tmp)
                
                # /3
                if item % 3 == 0:
                    # tmp, res = item // 2, item % 2
                    tmp = item // 3
                    if tmp in memo and memo[tmp] <= memo[item] - 1:
                        pass
                    else:
                        memo[tmp] = memo[item]+1
                        q2.add(tmp)

                tmp = item - 1
                """
                if tmp not in memo:
                    q2.add(tmp)
                memo[tmp] = min(memo.get(tmp, tmp), memo[item]+1)
                """
                if tmp in memo and memo[tmp] <= memo[item] - 1:
                    pass
                else:
                    memo[tmp] = memo[item]+1
                    q2.add(tmp)
                # print(memo)
            # q = collections.deque(q2)
            # print(memo)

        q = collections.deque([1])
        visited = set([1])
        
        step = 1
        while n not in visited:
            q2 = set()
            while len(q) > 0:
                item = q.popleft()
                if item in memo:
                    return step + memo[item]
                visited.add(item)
                
                if item * 2 <= n and item * 2 not in visited:
                    q2.add(item * 2)
                if  item * 3 <= n and item* 3 not in visited:
                    q2.add(item * 3)
                if item + 1 not in visited:
                    q2.add(item + 1)
            q = collections.deque(q2)
            step += 1
            # print(step, q)
        return step


    def solve2(self, n):
        self.memo = {}
       
        def dp(m):
            if m <= 1:
                return m
            if m not in self.memo:
                res = 1 + min(m % 2 + dp(m//2), m % 3 + dp(m//3))
                self.memo[m] = res
            return self.memo[m]

        res = dp(n)
        return res


if __name__ == "__main__":
    a = Solution()
    # print(a.minDays(10))
    print(a.solve2(10))
    print(a.solve2(2 * (10 ** 9)))
    print(a.solve2(1421))
    print(a.solve2(69652))

    """
    print(a.minDays(2 * (10 ** 9)))
    print(a.minDays(1421))
    print(a.minDays(69652))
    """
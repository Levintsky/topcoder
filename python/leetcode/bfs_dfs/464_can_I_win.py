"""
464. Can I Win (Medium)

In the "100 game," two players take turns adding, to a running total, any integer from 1..10. The player who first causes the running total to reach or exceed 100 wins.

What if we change the game so that players cannot re-use integers?

For example, two players might take turns drawing from a common pool of numbers of 1..15 without replacement until they reach a total >= 100.

Given an integer maxChoosableInteger and another integer desiredTotal, determine if the first player to move can force a win, assuming both players play optimally.

You can always assume that maxChoosableInteger will not be larger than 20 and desiredTotal will not be larger than 300.

Example

Input:
maxChoosableInteger = 10
desiredTotal = 11

Output:
false

Explanation:
No matter which integer the first player choose, the first player will lose.
The first player can choose an integer from 1 up to 10.
If the first player choose 1, the second player can only choose integers from 2 up to 10.
The second player will win by choosing 10 and get a total = 11, which is >= desiredTotal.
Same with other integers chosen by the first player, the second player will always win.
"""

"""
Memoization: 
time complexity: O(2^n)
no state kept: O(n!)
Solution 2: faster with bit operation

After solving several "Game Playing" questions in leetcode, I find them to be pretty similar. Most of them can be solved using the top-down DP approach, which "brute-forcely" simulates every possible state of the game.

The key part for the top-down dp strategy is that we need to avoid repeatedly solving sub-problems. Instead, we should use some strategy to "remember" the outcome of sub-problems. Then when we see them again, we instantly know their result. By doing this, we can always reduce time complexity from exponential to polynomial.
(EDIT: Thanks for @billbirdh for pointing out the mistake here. For this problem, by applying the memo, we at most compute for every subproblem once, and there are O(2^n) subproblems, so the complexity is O(2^n) after memorization. (Without memo, time complexity should be like O(n!))

For this question, the key part is: what is the state of the game? Intuitively, to uniquely determine the result of any state, we need to know:

The unchosen numbers
The remaining desiredTotal to reach
A second thought reveals that 1) and 2) are actually related because we can always get the 2) by deducting the sum of chosen numbers from original desiredTotal.

Then the problem becomes how to describe the state using 1).

In my solution, I use a boolean array to denote which numbers have been chosen, and then a question comes to mind, if we want to use a Hashmap to remember the outcome of sub-problems, can we just use Map<boolean[], Boolean> ? Obviously we cannot, because the if we use boolean[] as a key, the reference to boolean[] won't reveal the actual content in boolean[].

Since in the problem statement, it says maxChoosableInteger will not be larger than 20, which means the length of our boolean[] array will be less than 20. Then we can use an Integer to represent this boolean[] array. How?

Say the boolean[] is {false, false, true, true, false}, then we can transfer it to an Integer with binary representation as 00110. Since Integer is a perfect choice to be the key of HashMap, then we now can "memorize" the sub-problems using Map<Integer, Boolean>.

The rest part of the solution is just simulating the game process using the top-down dp.
"""

import timeit

class Solution(object):
  def solution2(self, maxChoosableInteger, desiredTotal):
        """
        :type maxChoosableInteger: int
        :type desiredTotal: int
        :rtype: bool
        """
        if (1+maxChoosableInteger)*maxChoosableInteger/2 < desiredTotal:
            return False
        if desiredTotal <= 0:
            return True
        d = collections.defaultdict(bool)
        
        def helper(k, M, desiredTotal):
            if k in d:
                return d[k]
            if desiredTotal <= 0:
                return False
            for i in xrange(M, 0, -1):
                if k&(1<<i) == 0:  
                    if not helper(k+(1<<i), M, desiredTotal - i):
                        d[k] = True
                        return True
            d[k] = False
            return False
        return helper(0, maxChoosableInteger, desiredTotal)
 
  def canIWin(self, maxChoosableInteger, desiredTotal):
    """
    :type maxChoosableInteger: int
    :type desiredTotal: int
    :rtype: bool
    """
    n = maxChoosableInteger
    if n*(n+1) < desiredTotal: return False
    curr = [True] * n
    # key = self.bool_to_int(curr)
    table = {}
    result = self.helper(table, curr, desiredTotal, n)
    print table
    return result

  def helper(self, table, curr, total, n):
    # case 1: already checked
    key = tuple(curr)
    if tuple(curr) in table:
      return table[tuple(curr)]
    # base case 2: achievable by select the largest number
    # curr = self.int_to_bool(key, n)
    # print 'current', curr

    # memoized dp
    for i in range(n-1,-1,-1):
      if curr[i] == True:
        # print 'total', total, 'i+1', i+1, curr
        curr[i] = False
        if total-i-1>0:
          result = self.helper(table, curr, total-i-1, n)
          # print table
        else:
          result = False
        curr[i] = True
        if not result:
          table[key] = True
          return True
    table[key] = False
    # print table
    return False


if __name__ == '__main__':
  start = timeit.timeit()
  a = Solution()
  print a.canIWin(5,6) 
  end = timeit.timeit()
  print end-start

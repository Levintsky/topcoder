"""
440. K-th Smallest in Lexicographical Order (Hard)

Given integers n and k, find the lexicographically k-th smallest integer in the range from 1 to n.

Note: 1 <= k <= n <= 10**9.

Example:

Input:
n: 13   k: 2

Output:
10

Explanation:
The lexicographical order is [1, 10, 11, 12, 13, 2, 3, 4, 5, 6, 7, 8, 9], so the second smallest number is 10.
"""

"""
Original idea comes from
http://bookshadow.com/weblog/2016/10/24/leetcode-k-th-smallest-in-lexicographical-order/

Actually this is a denary tree (each node has 10 children). Find the kth element is to do a k steps preorder traverse of the tree.
Initially, image you are at node 1 (variable: curr),
the goal is move (k - 1) steps to the target node x. (substract steps from k after moving)
when k is down to 0, curr will be finally at node x, there you get the result.

we don't really need to do a exact k steps preorder traverse of the denary tree, the idea is to calculate the steps between curr and curr + 1 (neighbor nodes in same level), in order to skip some unnecessary moves.

Main function
Firstly, calculate how many steps curr need to move to curr + 1.

if the steps <= k, we know we can move to curr + 1, and narrow down k to k - steps.

else if the steps > k, that means the curr + 1 is actually behind the target node x in the preorder path, we can't jump to curr + 1. What we have to do is to move forward only 1 step (curr * 10 is always next preorder node) and repeat the iteration.

calSteps function

how to calculate the steps between curr and curr + 1?
Here we come up a idea to calculate by level.
Let n1 = curr, n2 = curr + 1.
n2 is always the next right node beside n1's right most node (who shares the same ancestor "curr")
(refer to the pic, 2 is right next to 1, 20 is right next to 19, 200 is right next to 199).

so, if n2 <= n, what means n1's right most node exists, we can simply add the number of nodes from n1 to n2 to steps.

else if n2 > n, what means n (the biggest node) is on the path between n1 to n2, add (n + 1 - n1) to steps.

organize this flow to "steps += Math.min(n + 1, n2) - n1; n1 *= 10; n2 *= 10;"

Here is the code snippet:

public int findKthNumber(int n, int k) {
    int curr = 1;
    k = k - 1;
    while (k > 0) {
        int steps = calSteps(n, curr, curr + 1);
        if (steps <= k) {
            curr += 1;
            k -= steps;
        } else {
            curr *= 10;
            k -= 1;
        }
    }
    return curr;
}
//use long in case of overflow
public int calSteps(int n, long n1, long n2) {
    int steps = 0;
    while (n1 <= n) {
        steps += Math.min(n + 1, n2) - n1;
        n1 *= 10;
        n2 *= 10;
    }
    return steps;
}
"""

class Solution(object):
  def findKthNumber(self, n, k):
    """
    :type n: int
    :type k: int
    :rtype: int
    """
    prefix = 0
    cnt = 0
    while True:
      if prefix == 0: start = 1
      else: start = 0
      for i in range(start, 10):
        tmp = self.cnt_start(n, prefix*10+i)
        if k > tmp: k -= tmp
        else: break
      prefix = prefix * 10 + i
      if k == 1: return prefix
      k -= 1 # if not prefix itself
      # print 'start with', i
      print 'prefix', prefix, 'k', k
      cnt += 1
      if cnt == 10: break

  # def helper(self, n, i, k):

  def cnt_start(self, n, prefix):
    # how many numbers <=n and starts with prefix
    if n < prefix: return 0
    tmp = n
    while tmp/10 >= prefix: tmp /= 10
    print tmp, prefix
    if tmp != prefix: # not starting with prefix
      # count
      base = 1
      cnt = 0
      while prefix*base < n:
        cnt += base
        base *= 10
      return cnt
    else: # starting with prefix
      base = 1
      cnt = 0
      while n/base != prefix:
        cnt += base
        base *= 10
      print cnt
      return cnt+ n%base+1


if __name__ == '__main__':
  a = Solution()
  print a.findKthNumber(1000,300)
  # print a.cnt_start(22,2)

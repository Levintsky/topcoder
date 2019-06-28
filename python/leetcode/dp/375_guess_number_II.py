'''
375. Guess Number Higher or Lower II (Medium)

We are playing the Guess Game. The game is as follows:

I pick a number from 1 to n. You have to guess which number I picked.

Every time you guess wrong, I'll tell you whether the number I picked is higher or lower.

However, when you guess a particular number x, and you guess wrong, you pay $x. You win the game when you guess the number I picked.

Example:

n = 10, I pick 8.

First round:  You guess 5, I tell you that it's higher. You pay $5.
Second round: You guess 7, I tell you that it's higher. You pay $7.
Third round:  You guess 9, I tell you that it's lower. You pay $9.

Game over. 8 is the number I picked.

You end up paying $5 + $7 + $9 = $21.
Given a particular n >= 1, find out how much money you need to have to guarantee a win.
'''

"""
Solution 1:
For each number x in range[i~j]
we do: result_when_pick_x = x + max{DP([i~x-1]), DP([x+1, j])}
--> // the max means whenever you choose a number, the feedback is always bad and therefore leads you to a worse branch.
then we get DP([i~j]) = min{xi, ... ,xj}
--> // this min makes sure that you are minimizing your cost.

public class Solution {
    public int getMoneyAmount(int n) {
        int[][] table = new int[n+1][n+1];
        return DP(table, 1, n);
    }
    
    int DP(int[][] t, int s, int e){
        if(s >= e) return 0;
        if(t[s][e] != 0) return t[s][e];
        int res = Integer.MAX_VALUE;
        for(int x=s; x<=e; x++){
            int tmp = x + Math.max(DP(t, s, x-1), DP(t, x+1, e));
            res = Math.min(res, tmp);
        }
        t[s][e] = res;
        return res;
    }
}
Here is a bottom up solution.

public class Solution {
    public int getMoneyAmount(int n) {
        int[][] table = new int[n+1][n+1];
        for(int j=2; j<=n; j++){
            for(int i=j-1; i>0; i--){
                int globalMin = Integer.MAX_VALUE;
                for(int k=i+1; k<j; k++){
                    int localMax = k + Math.max(table[i][k-1], table[k+1][j]);
                    globalMin = Math.min(globalMin, localMax);
                }
                table[i][j] = i+1==j?i:globalMin;
            }
        }
        return table[1][n];
    }
}
"""

# memoized DP

class Solution(object):
  def getMoneyAmount(self, n):
    '''
    input: int
    output: int
    '''
    # create a [n+1] by [n+1] table
    table = []
    for i in range(n+1):
      subtable = [-1] * (n+1)
      table.append(subtable)
    result = self.helper(1, n, table)
    return result

  def helper(self, min_, max_, table):
    if max_ <= min_:
      table[min_][max_] = 0
    elif min_ == max_-1:
      table[min_][max_] = min_
    elif min_ == max_-2:
      table[min_][max_] = min_+1
    else:
      res = None
      for k in range(min_+1, max_):
        # result = min{ max(dp(min_,k-1), dp(k+1,max_) + k }
        if table[min_][k-1] != -1:
          k1 = table[min_][k-1]
        else:
          k1 = self.helper(min_, k-1, table)
        print 'k1: ', min_, k-1, k1
        if table[k+1][max_] != -1:
          k2 = table[k+1][max_]
        else:
          k2 = self.helper(k+1, max_, table)
        print 'k2: ', k+1, max_, k2
        tmp_res = max(k1, k2) + k
        print 'k=', k, 'result=', tmp_res
        if res is None:
          res = tmp_res
        else: res = min(res, tmp_res)
      table[min_][max_] = res
    print table[1][2]
    return table[min_][max_]
    

if __name__ == '__main__':
  a = Solution()
  print a.getMoneyAmount(5)

'''
486. Predict the Winner (Medium)

Given an array of scores that are non-negative integers. Player 1 picks one of the numbers from either end of the array followed by the player 2 and then player 1 and so on. Each time a player picks a number, that number will not be available for the next player. This continues until all the scores have been chosen. The player with the maximum score wins.

Given an array of scores, predict whether player 1 is the winner. You can assume each player plays to maximize his score.

Example 1:
Input: [1, 5, 2]
Output: False
Explanation: Initially, player 1 can choose between 1 and 2. 
If he chooses 2 (or 1), then player 2 can choose from 1 (or 2) and 5. If player 2 chooses 5, then player 1 will be left with 1 (or 2). 
So, final score of player 1 is 1 + 2 = 3, and player 2 is 5. 
Hence, player 1 will never be the winner and you need to return False.
Example 2:
Input: [1, 5, 233, 7]
Output: True
Explanation: Player 1 first chooses 1. Then player 2 have to choose between 5 and 7. No matter which number player 2 choose, player 1 can choose 233.
Finally, player 1 has more score (234) than player 2 (12), so you need to return True representing player1 can win.
Note:
1 <= length of the array <= 20.
Any scores in the given array are non-negative integers and will not exceed 10,000,000.
If the scores of both players are equal, then player 1 is still the winner.
'''

"""
what's the best score? (>=0, player 1 win)
a vector of len(n)
each item records the best score one can achieve of len(k)
iterate k = 1..n times starting from the corner case
"""


class Solution(object):
  def PredictTheWinner(self, nums):
    n = len(nums)
    if n<=2:
      return True
    # construct from 2
    tmp_result = []
    current_result = []
    # init
    for i in range(n-1):
      tmp_result.append(max(nums[i],nums[i+1]))
    curr_len = 2
    while(len(tmp_result)>1):
      # compute current_result from tmp_result
      for i in range(n-curr_len):
        # select nums[i+curr_len], 
        opt1 = sum(nums[i:i+curr_len]) - tmp_result[i] + nums[i+curr_len]
        # select nums[i]
        opt2 = sum(nums[i+1:i+curr_len+1]) - tmp_result[i+1] + nums[i]
        current_result.append(max(opt1, opt2))
      # swap
      tmp_result, current_result = current_result, []
      curr_len += 1
    tmp_result = tmp_result[0]
    print tmp_result
    if sum(nums) > 2*tmp_result:
      return False
    else:
      return True


if __name__ == '__main__':
  a = Solution()
  print a.PredictTheWinner([1,5,2])
  print a.PredictTheWinner([1,5,233,7])

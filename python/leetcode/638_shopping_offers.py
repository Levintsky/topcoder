'''
638. Shopping Offers (Medium)

In LeetCode Store, there are some kinds of items to sell. Each item 
has a price.

However, there are some special offers, and a special offer consists of 
one or more different kinds of items with a sale price.

You are given the each item's price, a set of special offers, and the 
number we need to buy for each item. The job is to output the lowest 
price you have to pay for exactly certain items as given, where you 
could make optimal use of the special offers.

Each special offer is represented in the form of an array, the last 
number represents the price you need to pay for this special offer, 
other numbers represents how many specific items you could get if you 
buy this offer.

You could use any of special offers as many times as you want.

Example 1:
Input: [2,5], [[3,0,5],[1,2,10]], [3,2]
Output: 14
Explanation: 
There are two kinds of items, A and B. Their prices are $2 and $5 
respectively. 
In special offer 1, you can pay $5 for 3A and 0B
In special offer 2, you can pay $10 for 1A and 2B. 
You need to buy 3A and 2B, so you may pay $10 for 1A and 2B 
(special offer #2), and $4 for 2A.

Example 2:
Input: [2,3,4], [[1,1,0,4],[2,2,1,9]], [1,2,1]
Output: 11
Explanation: 
The price of A is $2, and $3 for B, $4 for C. 
You may pay $4 for 1A and 1B, and $9 for 2A ,2B and 1C. 
You need to buy 1A ,2B and 1C, so you may pay $4 for 1A and 1B 
(special offer #1), and $3 for 1B, $4 for 1C. 
You cannot add more items, though only $9 for 2A ,2B and 1C.

Note:
There are at most 6 kinds of items, 100 special offers.
For each item, you need to buy at most 6 of them.
You are not allowed to buy more items than you want, even if that would lower the overall price.
'''

class Solution(object):
  def shopping(self, price, special, needs):
    n = len(price)
    table = {}
    table[tuple([0]*n)] = 0
    for i in range(n):
      tmp = [0]*i + [1] + [0]*(n-i-1)
      table[tuple(tmp)] = price[i]
      tmp.append(price[i])
      special.append(tmp)
    for item in special:
      if sum(item[:-1]) == 1:
        table[tuple(item[:-1])] = min(table[tuple(item[:-1])], item[-1])
    # prune special
    special2 = []
    for item in special:
      flag = True
      for j in range(len(item)-1):
        if item[j] > needs[j]:
          flag = False
          break
      if flag:
        special2.append(item)
    # print special
    # print table
    return self.dp(needs, price, special2, table)

  def dp(self, needs, price, special, table):
    # print 'working on needs', needs
    needs = tuple(needs)
    n = len(price)
    if needs in table:
      return table[needs]
    min_ = max(price) * sum(needs)
    for item in special:
      # print 'item', item
      tmp_tuple = tuple(item[:-1])
      # print 'tuple', tmp_tuple
      new_needs = [it for it in needs]
      for i in range(n):
        new_needs[i] -= tmp_tuple[i]
      # print 'new needs', new_needs
      if min(new_needs) >= 0:
        # print 'item before', item
        res = self.dp(new_needs, price, special, table)
        # print 'result', res, 'item after', item
        min_ = min(min_, res + item[-1])
    table[needs] = min_
    return min_

if __name__ == '__main__':
  a = Solution()
  # print a.shopping([2,5], [[3,0,5],[1,2,10]], [3,2])
  # print a.shopping([2,3,4], [[1,1,0,4],[2,2,1,9]], [1,2,1])
  # print a.shopping([2,3],[[1,0,1],[0,1,2]],[1,1])
  print a.shopping([1,2,3,1,9,9],
[[6,3,5,6,1,0,17],[6,6,6,5,2,2,2],[5,2,2,1,4,1,1],[6,4,4,4,0,4,19],[4,6,0,1,0,4,3],[1,2,0,5,0,4,13],[2,5,1,0,0,3,8],[4,3,1,3,5,3,11],[6,1,0,1,5,6,23],[5,3,1,0,3,6,7],[3,4,0,6,2,1,6],[0,3,6,3,4,0,2],[2,2,3,6,3,2,1],[6,1,1,4,2,0,2],[5,6,6,2,1,4,20],[1,4,5,2,5,4,9],[2,3,2,2,5,4,4],[6,6,0,3,0,6,23],[0,6,1,5,6,5,2],[0,0,6,0,4,5,17],[0,0,5,2,3,5,7],[6,0,5,3,6,3,2],[4,3,5,4,0,6,15],[6,2,1,5,2,1,15]]
,[5,6,5,5,6,1])
  # print a.shopping([2,5], [], [0,2])

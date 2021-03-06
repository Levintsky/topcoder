'''
365 Water and Jug Problem (Medium)

You are given two jugs with capacities x and y litres. There is an infinite amount of water supply available. You need to determine whether it is possible to measure exactly z litres using these two jugs.

If z liters of water is measurable, you must have z liters of water contained within one or both buckets by the end.

Operations allowed:

Fill any of the jugs completely with water.
Empty any of the jugs.
Pour water from one jug into another till the other jug is completely full or the first jug itself is empty.
Example 1: (From the famous "Die Hard" example)

Input: x = 3, y = 5, z = 4
Output: True
Example 2:

Input: x = 2, y = 6, z = 5
Output: False
'''

class Solution(object):
  def canMeasure(self, x, y, z):
    tmp_gcd = self.gcd(x,y)
    if z%tmp_gcd == 0: return True
    else: return False

  def gcd(self,x,y):
    x, y = min(x,y), max(x,y)
    while(y%x!=0):
      x, y = y%x, x
    return x


if __name__ == '__main__':
  a = Solution()
  print a.gcd(6,8)

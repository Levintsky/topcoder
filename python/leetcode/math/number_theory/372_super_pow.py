'''
372. Super Pow (Medium)

Your task is to calculate ab mod 1337 where a is a positive integer and b is an extremely large positive integer given in the form of an array.

Example1:

a = 2
b = [3]

Result: 8
Example2:

a = 2
b = [1,0]

Result: 1024
'''

class Solution(object):
  def superPow(self, a, b):
    rem = 1
    for item in b:
      # rem^10 * a^item
      result = 1
      for j in range(10):
        result = (result * rem) % 1337
      for j in range(item):
        result = (result * a) % 1337
      rem = result
    return rem


if __name__ == '__main__':
  a = Solution()
  print a.superPow(2, [3])
  print a.superPow(2, [1, 0])

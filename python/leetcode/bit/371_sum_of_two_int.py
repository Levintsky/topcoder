"""
371. Sum of Two Integers (Easy)

Calculate the sum of two integers a and b, but you are not allowed to use the operator + and -.

Example:
Given a = 1 and b = 2, return 3.
"""

"""
# take-away:
# 1. a & b carry
# 2. a ^ b add without carry

naive:
while b != 0:
  a, b = a^b, (a&b)<<1

case 1: pos, pos
case 2: neg, neg
case 3: pos, neg (sum neg)
case 4(tricky): pos, neg (sum pos)
  1s will move all the way to the most significant
  finally, neg will be 100000001x1x0
           pos will be 1000000000000
  and for carry will disappear after mask
  the 1x1x0 will be the positive part
"""


class Solution(object):
    def Helper(self, a, b):
        """
    :type a: int
    :type b: int
    :rtype: int
    """
        MAX = 0x7FFFFFFF
        MIN = 0x80000000
        Mask = 0xFFFFFFFF
        cnt = 0
        while b != 0:
            a, b = (a ^ b) & Mask, ((a & b) << 1) & Mask
            print(bin(a), bin(b))
            cnt += 1

        if a < MAX:
            return a
        else:
            return ~(a ^ Mask)

    def getSum(self, a, b):
        return self.Helper(a, b)


if __name__ == "__main__":
    a = Solution()
    print("result: ", a.getSum(-14, 16))

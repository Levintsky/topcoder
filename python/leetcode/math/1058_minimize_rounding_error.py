"""
1058. Minimize Rounding Error to Meet Target (Medium)

Given an array of prices [p1,p2...,pn] and a target, round each price pi to Roundi(pi) so that the rounded array [Round1(p1),Round2(p2)...,Roundn(pn)] sums to the given target. Each operation Roundi(pi) could be either Floor(pi) or Ceil(pi).

Return the string "-1" if the rounded array is impossible to sum to target. Otherwise, return the smallest rounding error, which is defined as Σ |Roundi(pi) - (pi)| for i from 1 to n, as a string with three places after the decimal.

Example 1:

Input: prices = ["0.700","2.800","4.900"], target = 8
Output: "1.000"
Explanation: 
Use Floor, Ceil and Ceil operations to get (0.7 - 0) + (3 - 2.8) + (5 - 4.9) = 0.7 + 0.2 + 0.1 = 1.0 .
Example 2:

Input: prices = ["1.500","2.500","3.500"], target = 10
Output: "-1"
Explanation: 
It is impossible to meet the target.

Note:

1 <= prices.length <= 500.
Each string of prices prices[i] represents a real number which is between 0 and 1000 and has exactly 3 decimal places.
target is between 0 and 1000000.
"""


class Solution(object):
    def minimizeError(self, prices, target):
        """
        :type prices: List[str]
        :type target: int
        :rtype: str
        """
        prices = [float(item) for item in prices]
        t_round = sum([round(item) for item in prices])
        res = sum([abs(round(item) - item) for item in prices])
        if t_round == target:
            # just round
            return str("%.3f" % res)
        elif t_round < target:
            # should round up
            tmp = [item - round(item) for item in prices if round(item) < item]
            diff = target - t_round
            if diff > len(tmp):
                return "-1"
            tmp.sort(reverse=True)
            tmp = tmp[:diff]
            res2 = sum([1.0 - 2 * item for item in tmp])
            return str("%.3f" % (res + res2))
        else:  # t_round > target
            # should round down
            tmp = [round(item) - item for item in prices if round(item) > item]
            diff = t_round - target
            if diff > len(tmp):
                return "-1"
            tmp.sort(reverse=True)
            tmp = tmp[:diff]
            res2 = sum([1.0 - 2 * item for item in tmp])
            return str("%.3f" % (res + res2))


if __name__ == "__main__":
    a = Solution()
    print(a.minimizeError(["0.700", "2.800", "4.900"], 8))

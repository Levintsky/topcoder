"""
754. Reach a Number (Easy)

You are standing at position 0 on an infinite number line. There is a goal at position target.

On each move, you can either go left or right. During the n-th move (starting from 1), you take n steps.

Return the minimum number of steps required to reach the destination.

Example 1:
Input: target = 3
Output: 2
Explanation:
On the first move we step from 0 to 1.
On the second step we step from 1 to 3.
Example 2:
Input: target = 2
Output: 3
Explanation:
On the first move we step from 0 to 1.
On the second move we step  from 1 to -1.
On the third move we step from -1 to 2.
Note:
target will be a non-zero integer in the range [-10^9, 10^9].
"""


class Solution(object):
    def reachNumber(self, target):
        """
        :type target: int
        :rtype: int
        """
        target = abs(target)
        i = 1
        curr = 0
        while curr < target:
            curr += i
            i += 1
        i -= 1
        # print(i)
        # case 1:
        if curr == target:
            return i
        # case 2: an even number away
        elif (curr - target) % 2 == 0:
            return i
        # case 3: an odd number away
        elif (curr + i + 1 - target) % 2 == 0:
            return i + 1
        else:
            return i + 2


if __name__ == "__main__":
    a = Solution()
    # print(a.reachNumber(3))
    print(a.reachNumber(2))

"""
1073. Adding Two Negabinary Numbers (Medium)

Given two numbers arr1 and arr2 in base -2, return the result of adding them together.

Each number is given in array format:  as an array of 0s and 1s, from most significant bit to least significant bit.  For example, arr = [1,1,0,1] represents the number (-2)^3 + (-2)^2 + (-2)^0 = -3.  A number arr in array format is also guaranteed to have no leading zeros: either arr == [0] or arr[0] == 1.

Return the result of adding arr1 and arr2 in the same format: as an array of 0s and 1s with no leading zeros.

Example 1:

Input: arr1 = [1,1,1,1,1], arr2 = [1,0,1]
Output: [1,0,0,0,0]
Explanation: arr1 represents 11, arr2 represents 5, the output represents 16.

Note:

1 <= arr1.length <= 1000
1 <= arr2.length <= 1000
arr1 and arr2 have no leading zeros
arr1[i] is 0 or 1
arr2[i] is 0 or 1
"""

"""
Really similar to 1017.
"""

class Solution(object):
    def addNegabinary(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: List[int]
        """
        arr1 = arr1[::-1]
        arr2 = arr2[::-1]
        n = max(len(arr1), len(arr2))
        res = [0] * n
        for i in range(n):
            if len(arr1) > i:
                res[i] += arr1[i]
            if len(arr2) > i:
                res[i] += arr2[i]
        while res.count(2) > 0 or res.count(-1) > 0:
            # step 1: remove 2
            n = len(res)
            for i in range(n):
                if res[i] == 2:
                    res[i] = 0
                    if i+1 != n:
                        res[i+1] -= 1
                    else:
                        res.append(-1)
            # remove -1
            n = len(res)
            for i in range(n):
                if res[i] == -1:
                    res[i] = 1
                    if i+1 != n:
                        res[i+1] += 1
                    else:
                        res.append(1)
        while len(res) > 1 and res[-1] == 0:
            _ = res.pop()
        res = res[::-1]
        return res

    def solve2(self, A, B):
        res = []
        carry = 0
        while A or B or carry:
            carry += (A or [0]).pop() + (B or [0]).pop()
            res.append(carry & 1)
            carry = -(carry >> 1)
        while len(res) > 1 and res[-1] == 0:
            res.pop()
        return res[::-1]

if __name__ == "__main__":
    a = Solution()
    # print(a.addNegabinary([1,1,0,1], [1,1,0,1,1]))
    print(a.solve2([1,1,0,1], [1,1,0,1,1]))
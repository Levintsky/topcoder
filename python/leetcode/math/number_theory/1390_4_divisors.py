"""
1390. Four Divisors (Medium)

Given an integer array nums, return the sum of divisors of the integers in that array that have exactly four divisors.

If there is no such integer in the array, return 0.

Example 1:

Input: nums = [21,4,7]
Output: 32
Explanation:
21 has 4 divisors: 1, 3, 7, 21
4 has 3 divisors: 1, 2, 4
7 has 2 divisors: 1, 7
The answer is the sum of divisors of 21 only.
 

Constraints:

1 <= nums.length <= 10^4
1 <= nums[i] <= 10^5
"""

import math

class Solution(object):
    def sumFourDivisors(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_ = max(nums)
        max_sqrt = int(math.sqrt(max_)) + 1
        memo = [True] * (max_+1)

        i = 2
        while i * i <= max_:
            if memo[i] == False:
                i += 1
                continue
            for j in range(2*i, len(memo), i):
                # print(j)
                memo[j] = False
            i += 1
        memo2 = set()
        for i in range(len(memo)):
            if i >= 2 and memo[i]:
                memo2.add(i)
        # print('done')
        # print(memo2)

        cnt = 0
        for item in nums:
            j = 2
            while j * j <= item:
                if j not in memo2 or item % j !=0:
                    j += 1
                if item % j == 0:
                    if item // j in memo2 and j * j !=item:
                        cnt += 1 + item + j + item // j
                        print(1, item, j, item//j)
                    elif j ** 3 == item:
                        cnt += 1 + j + j ** 2 + item
                        print(1, j, j*2, item)
                    break
        return cnt
    
    # def solve2(self, nums: List[int]) -> int:
    def solve2(self, nums):
        ans = 0
        for num in nums:
            ans += self.fourDivisors(num)
        return ans
    
    def fourDivisors(self, num):
        memo = set()
        for i in range(1, num + 1):
            if i * i > num:
                break
            if num % i == 0:
                memo.add(i)
                memo.add(num // i)
                if len(memo) > 4:
                    return 0
        if len(memo) == 4:
            return sum(memo)
        return 0

if __name__ == "__main__":
    a = Solution()
    # arr = [42592, 228, 37816, 83030, 4913, 59938, 96804, 89189, 81684, 65966]
    arr = [4913]
    for item in arr:
        print(a.sumFourDivisors([item]))
        print(a.solve2([item]))
    # print(a.sumFourDivisors([21,4,7, 91]))
    # print(a.sumFourDivisors([1,2,3,4,5,6,7,8,9,10]))
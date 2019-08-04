"""
825. Friends Of Appropriate Ages (Medium)

Some people will make friend requests. The list of their ages is given and ages[i] is the age of the ith person. 

Person A will NOT friend request person B (B != A) if any of the following conditions are true:

age[B] <= 0.5 * age[A] + 7
age[B] > age[A]
age[B] > 100 && age[A] < 100
Otherwise, A will friend request B.

Note that if A requests B, B does not necessarily request A.  Also, people will not friend request themselves.

How many total friend requests are made?

Example 1:

Input: [16,16]
Output: 2
Explanation: 2 people friend request each other.
Example 2:

Input: [16,17,18]
Output: 2
Explanation: Friend requests are made 17 -> 16, 18 -> 17.
Example 3:

Input: [20,30,100,110,120]
Output: 
Explanation: Friend requests are made 110 -> 100, 120 -> 110, 120 -> 100.

Notes:

1 <= ages.length <= 20000.
1 <= ages[i] <= 120.
"""

import collections

class Solution(object):
    def numFriendRequests(self, ages):
        """
        :type ages: List[int]
        :rtype: int
        """
        arr = collections.Counter(ages)

        ages.sort()
        n = len(ages)
        iA, iB = 1, 0

        res = 0
        # unequal
        while iA < n:
        	# get iB1
        	if ages[iA] <= 14:
        		iA += 1
        		continue
        	while iB < iA and 2 * ages[iB] - 14 <= ages[iA]:
        		iB += 1
        	res += iA - iB
        	iA += 1

        # equal
        # print('mid', res)
        for k, v in arr.items():
        	if v > 1:
        		if k > 14:
        			res += v * (v-1) // 2
        return res


if __name__ == "__main__":
	a = Solution()
	print(a.numFriendRequests([16, 16]))
	print(a.numFriendRequests([16, 17, 18]))
	print(a.numFriendRequests([20, 30, 100, 110, 120]))
	print(a.numFriendRequests([8, 85, 24, 85, 69]))

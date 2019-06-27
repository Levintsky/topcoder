"""
1090. Largest Values From Labels (Medium)

We have a set of items: the i-th item has value values[i] and label labels[i].

Then, we choose a subset S of these items, such that:

|S| <= num_wanted
For every label L, the number of items in S with label L is <= use_limit.
Return the largest possible sum of the subset S.

Example 1:

Input: values = [5,4,3,2,1], labels = [1,1,2,2,3], num_wanted = 3, use_limit = 1
Output: 9
Explanation: The subset chosen is the first, third, and fifth item.
Example 2:

Input: values = [5,4,3,2,1], labels = [1,3,3,3,2], num_wanted = 3, use_limit = 2
Output: 12
Explanation: The subset chosen is the first, second, and third item.
Example 3:

Input: values = [9,8,8,7,6], labels = [0,0,0,1,1], num_wanted = 3, use_limit = 1
Output: 16
Explanation: The subset chosen is the first and fourth item.
Example 4:

Input: values = [9,8,8,7,6], labels = [0,0,0,1,1], num_wanted = 3, use_limit = 2
Output: 24
Explanation: The subset chosen is the first, second, and fourth item.

Note:

1 <= values.length == labels.length <= 20000
0 <= values[i], labels[i] <= 20000
1 <= num_wanted, use_limit <= values.length
"""

import heapq


class Solution(object):
    def largestValsFromLabels(self, values, labels, num_wanted, use_limit):
        """
        :type values: List[int]
        :type labels: List[int]
        :type num_wanted: int
        :type use_limit: int
        :rtype: int
        """
        q = []
        for v, l in zip(values, labels):
            heapq.heappush(q, (-v, l))
        memo = {}
        result = []
        while not num_wanted == 0 and len(q) > 0:
            v, l = heapq.heappop(q)
            v = -v
            if l in memo and memo[l] == use_limit:
                continue
            result.append(v)
            memo[l] = memo.get(l, 0) + 1
            num_wanted -= 1
        return sum(result)


if __name__ == "__main__":
    a = Solution()
    print(a.largestValsFromLabels([5, 4, 3, 2, 1], [1, 1, 2, 2, 3], 3, 1))
    print(a.largestValsFromLabels([5, 4, 3, 2, 1], [1, 3, 3, 3, 2], 3, 2))
    print(a.largestValsFromLabels([9, 8, 8, 7, 6], [0, 0, 0, 1, 1], 3, 1))
    print(a.largestValsFromLabels([9, 8, 8, 7, 6], [0, 0, 0, 1, 1], 3, 2))

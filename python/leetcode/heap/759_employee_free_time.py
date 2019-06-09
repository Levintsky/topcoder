"""
759. Employee Free Time (Hard)

We are given a list schedule of employees, which represents the working time for each employee.

Each employee has a list of non-overlapping Intervals, and these intervals are in sorted order.

Return the list of finite intervals representing common, positive-length free time for all employees, also in sorted order.

Example 1:

Input: schedule = [[[1,2],[5,6]],[[1,3]],[[4,10]]]
Output: [[3,4]]
Explanation:
There are a total of three employees, and all common
free time intervals would be [-inf, 1], [3, 4], [10, inf].
We discard any intervals that contain inf as they aren't finite.
 

Example 2:

Input: schedule = [[[1,3],[6,7]],[[2,4]],[[2,5],[9,12]]]
Output: [[5,6],[7,9]]
 

(Even though we are representing Intervals in the form [x, y], the objects inside are Intervals, not lists or arrays. For example, schedule[0][0].start = 1, schedule[0][0].end = 2, and schedule[0][0][0] is not defined.)

Also, we wouldn't include intervals like [5, 5] in our answer, as they have zero length.

Note:

schedule and schedule[i] are lists with lengths in range [1, 50].
0 <= schedule[i].start < schedule[i].end <= 10^8.
NOTE: input types have been changed on April 15, 2019. Please reset to default code definition to get new method signature.
"""

import heapq


class Solution(object):
    def employeeFreeTime(self, schedule):
        """
        :type schedule: List[List[List[int]]]
        :rtype: List[List[int]]
        """
        # preprocessing: get min_, max_
        min_, max_ = float("inf"), -float("inf")
        for emp in schedule:
            min_ = min(min_, emp[0][0])
            max_ = max(max_, emp[-1][1])
        result = [[min_, float("inf")]]
        m = len(schedule)
        q = []
        for i in range(m):
            st, end = schedule[i][0]
            heapq.heappush(q, (st, -end, i, 0))
        while len(q) > 0:
            # pop and add new
            st, end, i, j = heapq.heappop(q)
            if len(schedule[i]) > j+1:
                st2, end2 = schedule[i][j+1]
                heapq.heappush(q, (st2, -end2, i, j+1))
            
            end = -end
            # case 1: end last, start new
            if st > result[-1][0]:
                result[-1] = [result[-1][0], st]
                result.append([end, float("inf")])
            result[-1][0] = max(result[-1][0], end)
        return result[:-1]

    def solve2(self, schedule):
        ints = sorted([i for s in schedule for i in s], key=lambda x: x[0])
        res, pre = [], ints[0]
        for i in ints[1:]:
            if i[0] <= pre[-1] and i[-1] > pre[-1]:
                pre[-1] = i[-1]
            elif i[0] > pre[-1]:
                res.append([pre[-1], i[0]])
                pre = i
        return res


if __name__ == "__main__":
    a = Solution()
    print(a.employeeFreeTime([[[1,2],[5,6]],[[1,3]],[[4,10]]]))
    print(a.solve2([[[1,2],[5,6]],[[1,3]],[[4,10]]]))
    # print(a.employeeFreeTime([[[1,3],[6,7]],[[2,4]],[[2,5],[9,12]]]))

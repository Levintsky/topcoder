"""
1013. Pairs of Songs With Total Durations Divisible by 60 (Easy)

In a list of songs, the i-th song has a duration of time[i] seconds. 

Return the number of pairs of songs for which their total duration in 
seconds is divisible by 60.  Formally, we want the number of indices 
i < j with (time[i] + time[j]) % 60 == 0.

Example 1:

Input: [30,20,150,100,40]
Output: 3
Explanation: Three pairs have a total duration divisible by 60:
(time[0] = 30, time[2] = 150): total duration 180
(time[1] = 20, time[3] = 100): total duration 120
(time[1] = 20, time[4] = 40): total duration 60
Example 2:

Input: [60,60,60]
Output: 3
Explanation: All three pairs have a total duration of 120, which is 
divisible by 60.

Note:

1 <= time.length <= 60000
1 <= time[i] <= 500
"""


class Solution(object):
    def numPairsDivisibleBy60(self, time):
        """
        :type time: List[int]
        :rtype: int
        """
        stat = {}
        for item in time:
            item_ = item % 60
            stat[item_] = stat.get(item_, 0) + 1

        result = 0
        # case 1: 29
        for i in range(1, 30):
            result += stat.get(i, 0) * stat.get(60 - i, 0)

        # case 2: 30
        result += stat.get(30, 0) * (stat.get(30, 0) - 1) // 2

        # case 3: 60
        result += stat.get(0, 0) * (stat.get(0, 0) - 1) // 2
        return result


if __name__ == "__main__":
    a = Solution()
    # print(a.numPairsDivisibleBy60([30, 20, 150, 100, 40, 60]))
    print(a.numPairsDivisibleBy60([60, 60, 60]))

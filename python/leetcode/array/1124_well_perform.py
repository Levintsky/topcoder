"""
1124. Longest Well-Performing Interval (Medium)

We are given hours, a list of the number of hours worked per day for a given employee.

A day is considered to be a tiring day if and only if the number of hours worked is (strictly) greater than 8.

A well-performing interval is an interval of days for which the number of tiring days is strictly larger than the number of non-tiring days.

Return the length of the longest well-performing interval.

 

Example 1:

Input: hours = [9,9,6,0,6,6,9]
Output: 3
Explanation: The longest well-performing interval is [9,9,6].
 

Constraints:

1 <= hours.length <= 10000
0 <= hours[i] <= 16
"""

"""
Intuition
If working hour > 8 hours, yes it's tiring day.
But I doubt if 996 is a well-performing interval.
Life needs not only 996 but also 669.


Explanation
We starts with a score = 0,
If the working hour > 8, we plus 1 point.
Otherwise we minus 1 point.
We want find the maximum interval that have strict positive score.

After one day of work, if we find the total score > 0,
the whole interval has positive score,
so we set res = i + 1.

If the score is a new lowest score, we record the day by seen[cur] = i.
And the maximum interval is i - seen[score - 1]


Complexity
Time O(N^2)
Space O(N)


Java:

    public int longestWPI(int[] hours) {
        int res = 0, score = 0, n = hours.length;
        Map<Integer, Integer> seen = new HashMap<>();
        seen.put(0, -1);
        for (int i = 0; i < n; ++i) {
            score += hours[i] > 8 ? 1 : -1;
            if (score > 0) {
                res = i + 1;
            } else {
                seen.putIfAbsent(score, i);
                if (seen.containsKey(score - 1))
                    res = Math.max(res, i - seen.get(score - 1));
            }
        }
        return res;
    }
C++:

    int longestWPI(vector<int>& hours) {
        int res = 0, score = 0, n = hours.size();
        unordered_map<int, int> seen = {{0, -1}};
        for (int i = 0; i < n; ++i) {
            score += hours[i] > 8 ? 1 : -1;
            if (score > 0) {
                res = i + 1;
            } else {
                if (seen.find(score) == seen.end())
                    seen[score] = i;
                if (seen.find(score - 1) != seen.end())
                    res = max(res, i - seen[score - 1]);
            }
        }
        return res;
    }
Python:

    def longestWPI(self, hours):
        res = score = 0
        seen = {}
        for i, h in enumerate(hours):
            score = score + 1 if h > 8 else score - 1
            if score > 0:
                res = i + 1
            seen.setdefault(score, i)
            if score - 1 in seen:
                res = max(res, i - seen[score - 1])
        return res
"""

class Solution(object):
    def longestWPI(self, hours):
        """
        :type hours: List[int]
        :rtype: int
        """
        n = len(hours)
        if n == 0:
            return 0
        l, r = 0, n
        array = []
        for item in hours:
            if item > 8:
                array.append(1)
            else:
                array.append(0)

        def check(mid):
            cnt = sum(array[:mid])
            if cnt * 2 > mid:
                return True
            for i in range(mid, len(array)):
                cnt += array[i]
                cnt -= array[i-mid]
                if cnt * 2 > mid:
                    # print(array[i-mid+1:i+1])
                    return True
            return False

        for i in range(20, 50):
            print(i, check(i))

        if not check(1):
        	return 0

        while l < r:
            mid = (l + r) // 2
            # print(mid)
            if mid % 2 == 0 and mid < n:
                mid += 1
            print(mid)
            if check(mid):
                if not check(mid + 2):
                    break
                l = min(mid + 2, n)
            else:
                r = mid - 2

        # mid = (l + r) // 2
        if l == r:
            mid = l
        tmp = min(2 * mid - 1, n)
        if check(tmp):
            return tmp
        else:
            return mid

    def solve(self, hours):
        array = [0]
        memo = {0: -1}
        best = 0
        for i, item in enumerate(hours):
            if item > 8:
                tmp = array[-1] + 1
            else:
                tmp = array[-1] - 1
            for k in memo:
                if k < tmp:
                    best = max(best, i - memo[k])
            if tmp <= 0 and tmp not in memo:
                memo[tmp] = i
            array.append(tmp)
        return best

    def solve2(self, hours):
        res = score = 0
        seen = {}
        for i, h in enumerate(hours):
            score = score + 1 if h > 8 else score - 1
            if score > 0:
                res = i + 1
            seen.setdefault(score, i)
            if score - 1 in seen:
                res = max(res, i - seen[score - 1])
        return res


if __name__ == "__main__":
    a = Solution()
    print(a.solve([9,9,6,0,6,6,9]))
    print(a.solve([6,9,9]))
    print(a.solve([9,6,9,6,9,6,5,4]))
    print(a.solve([6,6,6]))
    print(a.solve([9,9,9]))

"""
1088. Confusing Number II (Hard)

We can rotate digits by 180 degrees to form new digits. When 0, 
1, 6, 8, 9 are rotated 180 degrees, they become 0, 1, 9, 8, 6 
respectively. When 2, 3, 4, 5 and 7 are rotated 180 degrees, they become invalid.

A confusing number is a number that when rotated 180 degrees 
becomes a different number with each digit valid.(Note that the 
rotated number can be greater than the original number.)

Given a positive integer N, return the number of confusing 
numbers between 1 and N inclusive.

Example 1:

Input: 20
Output: 6
Explanation: 
The confusing numbers are [6,9,10,16,18,19].
6 converts to 9.
9 converts to 6.
10 converts to 01 which is just 1.
16 converts to 91.
18 converts to 81.
19 converts to 61.
Example 2:

Input: 100
Output: 19
Explanation: 
The confusing numbers are [6,9,10,16,18,19,60,61,66,68,80,81,86,89,90,91,98,99,100].

Note:

1 <= N <= 10^9
"""

"""
Solution 2: DFS
check all numbers until too large
will TLE in python
Time complexity: O(m)
"""


class Solution(object):
    def confusingNumberII(self, N):
        """
        :type N: int
        :rtype: int
        """
        # edge case:
        if N < 6:
            return 0
        if N in [6, 7, 8]:
            return 1
        if N == 9:
            return 2
        small_set = set([6, 9])
        large_set = set([0, 1, 6, 8, 9])
        # count how many digit in N
        n_digit = 1
        N2 = N
        N_break = []
        while N2 > 0:
            N_break.append(N2 % 10)
            N2 //= 10
            n_digit += 1
        N_break = N_break[::-1]

        # for n digit, calculate how many valid
        n = 1
        memo = []
        while n < n_digit - 1:
            if n == 0:
                memo.append(2)
            else:
                all_ = 4 * (5 ** (n - 1))
                invalid_ = 2 * (3 ** (n - 1) // 2)
                memo.append(all_ - invalid_)
            n += 1
        result = sum(memo)
        print(memo)
        # calculate result with n_digit
        for i, item in enumerate(N_break):
            # ith-digit, from 1..item-1
            # n_digit-i remaining
            if i != 0:
                start = 0
            else:
                start = 1
            for tmp in range(start, item):
                if tmp in [0, 1, 8]:
                    result += sum(memo[: n_digit - i])
                elif tmp == 6 or tmp == 9:
                    result += 5 ** (n_digit - i)
            if item not in large_set:
                break
        return result

    def solve2(self, N):
        nums = [0, 1, 6, 8, 9]
        mMap = {0: 0, 1: 1, 6: 9, 8: 8, 9: 6}
        self.res = 0

        def check(n):
            flip = 0

            n2 = n
            while n2 > 0:
                tmp = n2 % 10
                if tmp not in mMap:
                    return False
                else:
                    flip = flip * 10 + mMap[tmp]
                n2 //= 10
            return n == flip

        def dfs(curNum):
            print(curNum)
            if curNum > N:
                return
            if curNum <= N and not check(curNum):
                self.res += 1
            if curNum == 0:
                start = 1
            else:
                start = 0
            for i in range(start, 5):
                dfs(curNum * 10 + nums[i])

        dfs(0)
        return self.res

    def getDigitCount(self, digit):
        for d in range(len(self.digit_count), digit + 1):
            self.digit_count.append(
                4 * (5 ** (d - 1)) - 4 * len(self.digit_conf_dict[d - 2])
            )
            max_digit = 10 ** (d - 1)
            self.digit_conf_dict[d] = [
                val * max_digit + middle * 10 + val
                for val in self.valid_digits
                for middle in self.digit_conf_dict[d - 2]
            ]
        return self.digit_count[digit]

    def solve3(self, N: int) -> int:
        self.digit_conf_dict = {1: [0, 1, 8], 2: [0, 11, 69, 88, 96]}
        self.digit_count = [0, 2, 16]
        self.valid_digits = [0, 1, 6, 8, 9]
        self.include = {0: 1, 1: 2, 2: 2, 3: 2, 4: 2, 5: 2, 6: 3, 7: 3, 8: 4, 9: 5}

        total_count = 0
        upperlimit, digit = 9, 1
        while upperlimit <= N:
            total_count += self.getDigitCount(digit)
            upperlimit = upperlimit * 10 + 9
            digit += 1
        upperlimit = (upperlimit - 9) // 10
        if N == upperlimit:
            return total_count
        # accounts for ALL the valid-rotate numbers from upperlimit to N inclusively
        s = str(N)
        for i, c in enumerate(s):
            val = int(c)
            if val not in self.valid_digits:
                total_count += (
                    (self.include[val] * (5 ** (digit - 1 - i)))
                    if i > 0
                    else ((self.include[val] - 1) * (5 ** (digit - 1 - i)))
                )
                break
            else:
                total_count += (
                    ((self.include[val] - 1) * (5 ** (digit - 1 - i)))
                    if i > 0
                    else ((self.include[val] - 2) * (5 ** (digit - 1 - i)))
                )
                if i == len(s) - 1:
                    total_count += 1

        # remove invalid numbers out from the count for the incomplete part of digits
        get = self.getDigitCount(digit)
        for remove in self.digit_conf_dict[digit]:
            if remove > N:
                break
            if remove <= upperlimit:
                continue
            total_count -= 1
        return int(total_count)

    def solve4(self, N):
        l = [0, 1, 6, 8, 9]

        s = str(N)
        n = len(s)

        if len(set(s) - set([str(x) for x in l])) == 0:
            res = 1
        else:
            res = 0
        for i in range(1, n):
            if i == 1:
                res -= 3
            else:
                if i % 2 == 0:
                    res -= 4 * pow(5, i // 2 - 1)
                else:
                    res -= 4 * 3 * pow(5, i // 2 - 1)

        if n % 2 == 0:
            x = s[: (n - 1) // 2 + 1]
        else:
            x = s[: (n - 1) // 2]

        if len(set(x) - set([str(x) for x in l])) == 0:
            x = list(x)
            for i in range(len(x)):
                if x[i] == "6":
                    x[i] = "9"
                elif x[i] == "9":
                    x[i] = "6"
            x.reverse()
            left = "".join(x)
            right = s[(n - 1) // 2 + 1 :]
            if right >= left:
                if n % 2 == 0:
                    res -= 1
                else:
                    y = int(s[(n - 1) // 2])
                    if y >= 8:
                        res -= 3
                    elif 1 <= y < 8:
                        res -= 2
                    else:
                        res -= 1
            else:
                if n % 2 != 0:
                    y = int(s[(n - 1) // 2])
                    if y > 8:
                        res -= 3
                    elif 1 < y <= 8:
                        res -= 2
                    elif 0 < y <= 1:
                        res -= 1

        d = {0: 1, 1: 3}
        for i in range(2, n - 1):
            if i % 2 == 0:
                v = pow(5, i // 2)
            else:
                v = 3 * pow(5, i // 2)
            d[i] = v

        for i in range(n):
            j = self.bs(l, int(s[i]))
            res += j * pow(5, n - i - 1)
            if n >= (i + 1) * 2:
                if i == 0:
                    j -= 1
                res -= j * d[n - (i + 1) * 2]
            if int(s[i]) not in l:
                break
        return res

    def bs(self, l, v):
        low = 0
        high = len(l) - 1
        while low <= high:
            mid = (low + high) // 2
            if l[mid] < v:
                low = mid + 1
            else:
                high = mid - 1
        return low


if __name__ == "__main__":
    a = Solution()
    # print(a.confusingNumberII(20))
    # print(a.solve3(20))
    print(a.solve4(100))

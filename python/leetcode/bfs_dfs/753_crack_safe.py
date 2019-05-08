"""
753. Cracking the Safe (Hard)

There is a box protected by a password. The password is n digits, where each letter can be one of the first k digits 0, 1, ..., k-1.

You can keep inputting the password, the password will automatically be matched against the last n digits entered.

For example, assuming the password is "345", I can open it when I type "012345", but I enter a total of 6 digits.

Please return any string of minimum length that is guaranteed to open the box after the entire string is inputted.

Example 1:
Input: n = 1, k = 2
Output: "01"
Note: "10" will be accepted too.
Example 2:
Input: n = 2, k = 2
Output: "00110"
Note: "01100", "10011", "11001" will be accepted too.
Note:
n will be in the range [1, 4].
k will be in the range [1, 10].
k^n will be at most 4096.
"""

"""
Solution 1:
Hamilton graph:
node (1111) and (1112) can be concatenated together,
we draw an arrow;

Solution 2:
all n-divisors:
4: 1, 2, 4
1
11
1111
1112
1113
...
12
1211
1212
1213
...
2
21
2111

cross circular, like 11, 1111, 1212,
cross rotating repetition like 1211, since we have 1112
"""

class Solution(object):
    def crackSafe(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        result = []
        def sub_gen(n_, k):
            if n_ == 1:
                result = [str(i) for i in range(k)]
                return result
            else:
                result = sub_gen(n_-1, k)
                new_result = []
                for i in range(k):
                    tmp_result = [str(i)+item for item in result]
                    new_result += tmp_result
                return new_result

        def generate(n, k):
            # n-digit, k-choice
            if n == 1: len_ = [1]
            elif n == 2: len_ = [1, 2]
            elif n == 3: len_ = [1, 3]
            else: len_ = [1, 2, 4]
        
            for i in range(k):
                # 1st digit
                s = str(i)
                result.append(s)
                if n == 1: continue
                for j in range(k):
                    s = str(i)+str(j)
                    result.append(s)
                    if n != 4: continue
                    for ii in range(k):
                        for jj in range(k):
                            result.append(s+str(ii)+str(jj))
        generate(n, k)
        print(result)

    def solve2(self, n, k):
        # Hamilton graph
        curr = "0" * n
        self.memo = set()
        self.memo.add(curr)
        self.result = ""

        def dfs(curr):
            # corner case: all successful
            if len(curr) == k ** n + n - 1:
                self.result = curr
                return True
            tmp = curr[-(n-1):]
            for i in range(k):
                full = tmp + str(i)
                if full not in self.memo:
                    self.memo.add(full)
                    curr += str(i)
                    if dfs(curr):
                        return True
                    curr = curr[:-1]
                    self.memo.remove(full)
            return False
        dfs(curr)
        return self.result


if __name__ == "__main__":
    a = Solution()
    # print(a.crackSafe(2, 2))
    print(a.solve2(1, 2))

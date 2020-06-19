"""
1062. Longest Repeating Substring (Medium)

Given a string S, find out the length of the longest repeating substring(s). Return 0 if no repeating substring exists.

 

Example 1:

Input: "abcd"
Output: 0
Explanation: There is no repeating substring.
Example 2:

Input: "abbaba"
Output: 2
Explanation: The longest repeating substrings are "ab" and "ba", each of which occurs twice.
Example 3:

Input: "aabcaabdaab"
Output: 3
Explanation: The longest repeating substring is "aab", which occurs 3 times.
Example 4:

Input: "aaaaa"
Output: 4
Explanation: The longest repeating substring is "aaaa", which occurs twice.
 

Note:

The string S consists of only lowercase English letters from 'a' - 'z'.
1 <= S.length <= 1500
"""

class Solution(object):
    def longestRepeatingSubstring(self, S):
        """
        :type S: str
        :rtype: int
        """
        nums = [ord(c)-ord('a') for c in S]
        MOD = 2 ** 64
        
        def valid(l):
            key = 0
            memo = set()
            for item in nums[:l]:
                key = key * 26 + item
            key = key % MOD
            memo.add(key)
            aL = 26 ** (l-1)
            for i in range(l, len(nums)):
                key = key - nums[i-l] * aL
                key = (key * 26 + nums[i]) % MOD
                if key in memo:
                    return True
                memo.add(key)
            return False
        
        l, r = 0, len(nums)-1
        best = 0
        print(valid(20))
        exit()
        while l <= r:
            mid = (l+r)//2
            print(mid)
            if valid(mid):
                best = max(best, mid)
                l = mid + 1
            else:
                r = mid - 1
        return best

    def solve2(self, s):
        memo = set()
        for i in range(len(s)-20):
            ss = s[i:i+20]
            if ss not in memo:
                memo.add(ss)
            else:
                print(ss)

    def solve3(self, s):
        n = len(s)
        memo = []
        for i in range(n+1):
            memo.append([0] * (n+1))

        best = 0
        for i in range(n):
            for j in range(i+1, n):
                if s[i-1] == s[j-1]:
                    memo[i][j] = memo[i-1][j-1] + 1
                    if memo[i][j] == 20:
                        print(s[i-20:i], s[j-20:j])
                        print(i, j)
                    best = max(best, memo[i][j])
        return best

    def solve4(self, S):
        nums = [ord(c)-ord('a') for c in S]
        MOD = 10 ** 9 + 7
        
        def valid(l):
            key = 0
            memo = {}
            for item in nums[:l]:
                key = key * 26 + item
            key = key % MOD
            memo[key] = [0]
            aL = 26 ** (l-1)
            for i in range(l, len(nums)):
                key = key - nums[i-l] * aL
                key = (key * 26 + nums[i]) % MOD
                if key in memo.keys():
                    subset = [tuple(nums[j:j+l]) for j in memo[key]]
                    if tuple(nums[i-l+1:i+1]) in subset:
                        return True
                else:
                    memo[key] = []
                memo[key].append(i-l+1)
            return False
        
        l, r = 0, len(nums)-1
        best = 0
        while l <= r:
            mid = (l+r)//2
            # print(mid)
            if valid(mid):
                best = max(best, mid)
                l = mid + 1
            else:
                r = mid - 1
        return best
                

if __name__ == "__main__":
    a = Solution()
    print(a.solve4("banana"))
    arr = "aaabaabaaaababaaaaaaaabaabaaabbbaaaabbbabbbaaaababbbababbbabaaabbaabaaabbaabbaaaabbbaaaabababbbbbaabbbabbaaabababbbbbbaabaaaabbbaaaaaabbbababbaabbbbaabaaabbababbbbabbbabbaabaaaaaabbabaabbbbbabaabababaabbabaaaabbbabbbbbabbaaaaabaababbbbabbaaaaaababbbbaabbbaabaaabaabbbbabbabaabaaaabaaabaaaaaabbbbabbbabbabaaabbbaaaaababaabaabbbbbababaaabbaaaabbbabababaabaabbababbbaaaaabbbabaabbbbbaaabbbaaaaaaabbbbbbbbabbaabbbabaaaabbbbabababababbabbbbbababaaaaababaabbabbbbaababaabbbbbabbbabbaaabbababaabbabbbbaaabaabbaaabbbababaabaaaaaabababaaababaaabaabaabaababaabbaaaaaabababbbabbaababbbababbabababbbabbababbbabbaaaabbbaaabbaababababaaaabbababbbbaaababababbabababbaaaaaabababbbabbabbbaabaaaaabbbbaabaababbbbbbbbbbbbaaaaaaababbbbbaaabaaaaaabaababaababaabaaabbbbaabbbaabbaaaaabaaabaaaababbaabaaaababbbaabbbabaabbaabbbbbabaaaaabaabbabaabbaaaabbababaaabaabbabbbaaaaaaababbbabaaaaaabbbaaabbbabaaabbaaaabbbaabaabbaaaaaaaaabababaaabbaabaaaaaaabbbbabbabbbbbbabbbbbbbaabbbaaaabbabbbbbaabaabbbbbbaabbabbabbaababbbaababbbaab"
    print(len(arr))
    # print(arr[548:568])
    # print(a.longestRepeatingSubstring(arr[548:]))
    print(a.solve4(arr))
    # print(a.solve2(arr))
    # print(a.solve3(arr))
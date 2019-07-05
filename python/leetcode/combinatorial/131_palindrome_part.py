'''
131. Palindrome Partitioning (Medium)

Given a string s, partition s such that every substring of the partition is a palindrome.

Return all possible palindrome partitioning of s.

For example, given s = "aab",
Return

[
  ["aa","b"],
  ["a","a","b"]
]
'''

class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        result = []
        n = len(s)
        
        def isPalin(s, i, j):
            while i < j:
                if s[i] == s[j]:
                    i += 1
                    j -= 1
                else:
                    return False
            return True

        def backtrack(tmpList, start):
            if start == n:
                result.append([item for item in tmpList])
            else:
                for i in range(start, n):
                    if isPalin(s, start, i):
                        tmpList.append(s[start:i+1])
                        backtrack(tmpList, i+1)
                        _ = tmpList.pop()

        backtrack([], 0)
        return result


if __name__ == "__main__":
    a = Solution()
    print(a.partition("aab"))
"""
1023. Binary String With Substrings Representing 1 To N (Mediums)

Given a binary string S (a string consisting only of '0' and '1's) and a positive integer N, return true if and only if for every integer X from 1 to N, the binary representation of X is a substring of S.

Example 1:

Input: S = "0110", N = 3
Output: true
Example 2:

Input: S = "0110", N = 4
Output: false
 

Note:

1 <= S.length <= 1000
1 <= N <= 10^9
"""

"""
Intuition
We can process the entire string and track all numbers [1..N] that we can build.

OR

We can generate binary string representation for [1..N], and search for it in the string.

Solution 1
For each non-zero position i in S, gradually build num while num <= N.
Track each num in seen, increment X for new num.
Return true if we built all numbers from 1 to N (X == N).
bool queryString(string S, int N, int X = 0) {
  vector<bool> seen(N);
  for (auto i = 0; i < S.size() && X < N; ++i) {
    if (S[i] == '0') continue;
    for (auto j = i, num = 0; num <= N && j < S.size(); ++j) {
      num = (num << 1) + S[j] - '0';
      if (num > 0 && num <= N && !seen[num - 1]) {
        ++X;
        seen[num - 1] = true;
      }
    }
  }
  return X == N;
}
Complexity Analysis
Runtime: O(S log N), where S is the string size. For every position, we analyze log N digits.
Memory: O(N) as we need to track all numbers from 1 to N.

Solution 2
Iterate from N to 1. Build binary string and search.

bool queryString(string S, int N) {
  while (N > 0) {
    auto s = bitset<32>(N--).to_string();
    if (S.find(s.substr(s.find("1"))) == string::npos) return false;
  }
  return true;
}
Complexity Analysis
Runtime: O(N * (S + log N)), where S is the string size. We search N times, and every search is O(S + log N).
Memory: O(1).
"""


class Solution(object):
    def queryString(self, S, N):
        """
        :type S: str
        :type N: int
        :rtype: bool
        """

        def helper(k):
            # binarize
            result = []
            while k != 0:
                result.append(k % 2)
                k = k // 2
            result = result[::-1]
            result = [str(item) for item in result]
            result = "".join(result)
            return result

        for i in range(1, N + 1):
            if i % 2 == 1:
                str_ = helper(i)
                curr = i
                while curr <= N:
                    if S.find(str_) < 0:
                        return False
                    str_ += "0"
                    curr *= 2
        return True


if __name__ == "__main__":
    a = Solution()
    print(a.queryString("0110", 4))

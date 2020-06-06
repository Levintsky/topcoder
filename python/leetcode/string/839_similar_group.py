"""
839. Similar String Groups (Hard)

Two strings X and Y are similar if we can swap two letters (in different positions) of X, so that it equals Y. Also two strings X and Y are similar if they are equal.

For example, "tars" and "rats" are similar (swapping at positions 0 and 2), and "rats" and "arts" are similar, but "star" is not similar to "tars", "rats", or "arts".

Together, these form two connected groups by similarity: {"tars", "rats", "arts"} and {"star"}.  Notice that "tars" and "arts" are in the same group even though they are not similar.  Formally, each group is such that a word is in the group if and only if it is similar to at least one other word in the group.

We are given a list A of strings.  Every string in A is an anagram of every other string in A.  How many groups are there?


Example 1:

Input: A = ["tars","rats","arts","star"]
Output: 2
 

Constraints:

1 <= A.length <= 2000
1 <= A[i].length <= 1000
A.length * A[i].length <= 20000
All words in A consist of lowercase letters only.
All words in A have the same length and are anagrams of each other.
The judging time limit has been increased for this question.
"""

class Solution(object):
    def numSimilarGroups(self, A):
        """
        :type A: List[str]
        :rtype: int
        """
        def valid(s1, s2):
            # print(s1, s2)
            diff = 0
            cnt = 0
            for c1, c2 in zip(s1, s2):
                if c1 != c2:
                    cnt += 1
                if cnt > 2:
                    return False
            return cnt == 2
            
        def dfs(s):
            newlist = []
            for i, item in enumerate(A):
                if A[i] == s:
                    A[i] = None
                elif A[i] is None:
                    continue
                elif valid(s, A[i]):
                    newlist.append(A[i])
                    A[i] = None
            if len(newlist) == 0:
                return
            else:
                for item in newlist:
                    dfs(item)
        
        result = 0
        while len(A) > 0:
            result += 1
            dfs(A[0])
            A = [item for item in A if item is not None]
            print(A)
        return result

    def solve2(self, A):
        def valid(s1, s2):
            # print(s1, s2)
            diff = 0
            cnt = 0
            for c1, c2 in zip(s1, s2):
                if c1 != c2:
                    cnt += 1
                if cnt > 2:
                    return False
            return cnt == 2

        n = len(A)
        memo = [-1] * n

        def find_par(idx):
            while memo[idx] != -1:
                idx = memo[idx]
            return idx

        for i in range(n):
            s1 = A[i]
            for j in range(i+1, n):
                if valid(A[i], A[j]):
                    par_i = find_par(i)
                    par_j = find_par(j)
                    if par_i != par_j:
                        min_par, max_par = min(par_i, par_j), max(par_i, par_j)
                        memo[max_par] = min_par
        print(memo)
        return memo.count(-1)


if __name__ == "__main__":
    a = Solution()
    # print(a.numSimilarGroups(["tars","rats","arts","star"]))
    print(a.solve2(["tars","rats","arts","star"]))
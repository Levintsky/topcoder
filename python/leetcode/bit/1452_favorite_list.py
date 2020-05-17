"""
1452. People Whose List of Favorite Companies Is Not a Subset of Another List (Medium)

Given the array favoriteCompanies where favoriteCompanies[i] is the list of favorites companies for the ith person (indexed from 0).

Return the indices of people whose list of favorite companies is not a subset of any other list of favorites companies. You must return the indices in increasing order.

Example 1:

Input: favoriteCompanies = [["leetcode","google","facebook"],["google","microsoft"],["google","facebook"],["google"],["amazon"]]
Output: [0,1,4] 
Explanation: 
Person with index=2 has favoriteCompanies[2]=["google","facebook"] which is a subset of favoriteCompanies[0]=["leetcode","google","facebook"] corresponding to the person with index 0. 
Person with index=3 has favoriteCompanies[3]=["google"] which is a subset of favoriteCompanies[0]=["leetcode","google","facebook"] and favoriteCompanies[1]=["google","microsoft"]. 
Other lists of favorite companies are not a subset of another list, therefore, the answer is [0,1,4].
Example 2:

Input: favoriteCompanies = [["leetcode","google","facebook"],["leetcode","amazon"],["facebook","google"]]
Output: [0,1] 
Explanation: In this case favoriteCompanies[2]=["facebook","google"] is a subset of favoriteCompanies[0]=["leetcode","google","facebook"], therefore, the answer is [0,1].
Example 3:

Input: favoriteCompanies = [["leetcode"],["google"],["facebook"],["amazon"]]
Output: [0,1,2,3]
 

Constraints:

1 <= favoriteCompanies.length <= 100
1 <= favoriteCompanies[i].length <= 500
1 <= favoriteCompanies[i][j].length <= 20
All strings in favoriteCompanies[i] are distinct.
All lists of favorite companies are distinct, that is, If we sort alphabetically each list then favoriteCompanies[i] != favoriteCompanies[j].
All strings consist of lowercase English letters only.
"""

class Solution(object):
    def peopleIndexes(self, favoriteCompanies):
        """
        :type favoriteCompanies: List[List[str]]
        :rtype: List[int]
        """
        memo = {}
        for tmp in favoriteCompanies:
            for item in tmp:
                if item not in memo:
                    memo[item] = len(memo)
        print(memo)
        # encode
        fav = []
        for i, item in enumerate(favoriteCompanies):
            fav.append((i, item))
        fav.sort(key=lambda item:len(item[1]), reverse=True)
        print(fav)
        binset = set()
        result = []
        for idx, tmp in fav:
            bin_ = 0
            for k in tmp:
                id_ = memo[k]
                bin_ |= 1 << id_
            print(idx, tmp, bin_)
            flag = True
            for item in binset:
                print(item, (bin_ ^ item) & bin_)
                if (bin_ ^ item) & bin_ == 0:
                    flag = False
                    break
            if flag:
                result.append(idx)
            binset.add(bin_)
            print(result)
            print("")
        return result

a = Solution()
print(a.peopleIndexes([["leetcode","google","facebook"],["google","microsoft"],["google","facebook"],["google"],["amazon"]])) 
print(a.peopleIndexes([["leetcode","google","facebook"],["leetcode","amazon"],["facebook","google"]]))
print(a.peopleIndexes([["leetcode"],["google"],["facebook"],["amazon"]]))

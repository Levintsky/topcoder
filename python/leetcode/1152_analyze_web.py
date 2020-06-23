"""
1152. Analyze User Website Visit Pattern (Medium)

We are given some website visits: the user with name username[i] visited the website website[i] at time timestamp[i].

A 3-sequence is a list of websites of length 3 sorted in ascending order by the time of their visits.  (The websites in a 3-sequence are not necessarily distinct.)

Find the 3-sequence visited by the largest number of users. If there is more than one solution, return the lexicographically smallest such 3-sequence.

 

Example 1:

Input: username = ["joe","joe","joe","james","james","james","james","mary","mary","mary"], timestamp = [1,2,3,4,5,6,7,8,9,10], website = ["home","about","career","home","cart","maps","home","home","about","career"]
Output: ["home","about","career"]
Explanation: 
The tuples in this example are:
["joe", 1, "home"]
["joe", 2, "about"]
["joe", 3, "career"]
["james", 4, "home"]
["james", 5, "cart"]
["james", 6, "maps"]
["james", 7, "home"]
["mary", 8, "home"]
["mary", 9, "about"]
["mary", 10, "career"]
The 3-sequence ("home", "about", "career") was visited at least once by 2 users.
The 3-sequence ("home", "cart", "maps") was visited at least once by 1 user.
The 3-sequence ("home", "cart", "home") was visited at least once by 1 user.
The 3-sequence ("home", "maps", "home") was visited at least once by 1 user.
The 3-sequence ("cart", "maps", "home") was visited at least once by 1 user.
 

Note:

3 <= N = username.length = timestamp.length = website.length <= 50
1 <= username[i].length <= 10
0 <= timestamp[i] <= 10^9
1 <= website[i].length <= 10
Both username[i] and website[i] contain only lowercase characters.
It is guaranteed that there is at least one user who visited at least 3 websites.
No user visits two websites at the same time.
"""

from collections import defaultdict
from itertools import combinations


class Solution(object):
    def mostVisitedPattern(self, username, timestamp, website):
        """
        :type username: List[str]
        :type timestamp: List[int]
        :type website: List[str]
        :rtype: List[str]
        """
        packed_tuple = zip(timestamp, username, website)
        sorted_packed_tuple = sorted(packed_tuple)
        
        mapping = defaultdict(list)
        for t, u, w in sorted_packed_tuple:
            mapping[u].append(w)
        
        counter_dict = defaultdict(int)         # use a dict for counting
        for website_list in mapping.values():
            combs = set(combinations(website_list, 3))    # size of combination is set to 3 
            for comb in combs:
                counter_dict[comb] += 1
        
        sorted_counter_dict = sorted(counter_dict, key=lambda x: (-counter_dict[x], x)) # sort descending by value, then lexicographically
        return sorted_counter_dict[0]


if __name__ == "__main__":
    a = Solution()
    username = ["joe","joe","joe","james","james","james","james","mary","mary","mary"]
    timestamp = [1,2,3,4,5,6,7,8,9,10]
    website = ["home","about","career","home","cart","maps","home","home","about","career"]
    print(a.mostVisitedPattern(username, timestamp, website))
    
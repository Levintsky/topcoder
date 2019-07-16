"""
1125. Smallest Sufficient Team (Hard)

In a project, you have a list of required skills req_skills, and a 
list of people.  The i-th person people[i] contains a list of skills 
that person has.

Consider a sufficient team: a set of people such that for every required 
skill in req_skills, there is at least one person in the team who has 
that skill.  We can represent these teams by the index of each person: 
for example, team = [0, 1, 3] represents the people with skills 
people[0], people[1], and people[3].

Return any sufficient team of the smallest possible size, represented 
by the index of each person.

You may return the answer in any order.  It is guaranteed an answer exists.

Example 1:

Input: req_skills = ["java","nodejs","reactjs"], people = [["java"],["nodejs"],["nodejs","reactjs"]]
Output: [0,2]
Example 2:

Input: req_skills = ["algorithms","math","java","reactjs","csharp","aws"], people = [["algorithms","math","java"],["algorithms","math","reactjs"],["java","csharp","aws"],["reactjs","csharp"],["csharp","math"],["aws","java"]]
Output: [1,2]
 

Constraints:

1 <= req_skills.length <= 16
1 <= people.length <= 60
1 <= people[i].length, req_skills[i].length, people[i][j].length <= 16
Elements of req_skills and people[i] are (respectively) distinct.
req_skills[i][j], people[i][j][k] are lowercase English letters.
It is guaranteed a sufficient team exists.
"""

class Solution(object):
    def smallestSufficientTeam(self, req_skills, people):
        """
        :type req_skills: List[str]
        :type people: List[List[str]]
        :rtype: List[int]
        """
        memo = {}
        for item in req_skills:
            memo[item] = len(memo)
        p_bit = []
        for plist in people:
            tmp = 0
            for item in plist:
                k = memo[item]
                tmp += 1 << k
            p_bit.append(tmp)
        # print(p_bit)
        target = 2 ** len(memo) - 1
        self.best = [1] * len(people)
        p_res = [0] * len(people)

        def dfs(p_num, ind, curr):
            if curr == target:
                if sum(p_res) < sum(self.best):
                    self.best = [item for item in p_res]
                return
            if ind == len(people):
                return
            # dfs
            # with ind
            new_curr = curr | p_bit[ind]
            p_res[ind] = 1
            dfs(p_num+1, ind+1, new_curr)
            p_res[ind] = 0
            dfs(p_num, ind+1, curr)

        dfs(0, 0, 0)
        res = []
        for i, item in enumerate(self.best):
            if item == 1:
                res.append(i)
        return res

    def solve2(self, req_skills, people):
        n, m = len(req_skills), len(people)
        key = {v: i for i, v in enumerate(req_skills)}
        dp = {0: []}
        for i, p in enumerate(people):
            his_skill = 0
            for skill in p:
                if skill in key:
                    his_skill |= 1 << key[skill]
            res_list = list(dp.items())
            for skill_set, need in res_list:
                with_him = skill_set | his_skill
                if with_him == skill_set: continue
                if with_him not in dp or len(dp[with_him]) > len(need) + 1:
                    dp[with_him] = need + [i]
        return dp[(1 << n) - 1]


if __name__ == "__main__":
    a = Solution()
    print(a.smallestSufficientTeam(["java","nodejs","reactjs"], [["java"],["nodejs"],["nodejs","reactjs"]]))
    req_skills = ["algorithms","math","java","reactjs","csharp","aws"]
    people = [["algorithms","math","java"],["algorithms","math","reactjs"],["java","csharp","aws"],["reactjs","csharp"],["csharp","math"],["aws","java"]]
    print(a.smallestSufficientTeam(req_skills, people))
    req_skills = ["hdbxcuzyzhliwv","uvwlzkmzgis","sdi","bztg","ylopoifzkacuwp","dzsgleocfpl"]
    people = [["hdbxcuzyzhliwv","dzsgleocfpl"],["hdbxcuzyzhliwv","sdi","ylopoifzkacuwp","dzsgleocfpl"],["bztg","ylopoifzkacuwp"],["bztg","dzsgleocfpl"],["hdbxcuzyzhliwv","bztg"],["dzsgleocfpl"],["uvwlzkmzgis"],["dzsgleocfpl"],["hdbxcuzyzhliwv"],[],["dzsgleocfpl"],["hdbxcuzyzhliwv"],[],["hdbxcuzyzhliwv","ylopoifzkacuwp"],["sdi"],["bztg","dzsgleocfpl"],["hdbxcuzyzhliwv","uvwlzkmzgis","sdi","bztg","ylopoifzkacuwp"],["hdbxcuzyzhliwv","sdi"],["hdbxcuzyzhliwv","ylopoifzkacuwp"],["sdi","bztg","ylopoifzkacuwp","dzsgleocfpl"],["dzsgleocfpl"],["sdi","ylopoifzkacuwp"],["hdbxcuzyzhliwv","uvwlzkmzgis","sdi"],[],[],["ylopoifzkacuwp"],[],["sdi","bztg"],["bztg","dzsgleocfpl"],["sdi","bztg"]]
    print(a.solve2(req_skills, people))

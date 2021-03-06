/*
There are potentially a lot of overlapping sub problems, but meanwhile we don't exactly know what those sub problems are. DP with memoization works pretty well in such cases. The workflow is like backtracking, but with memoization. Here I simply use a sorted string of target as the key for the unordered_map DP. A sorted target results in a unique sub problem for possibly different strings.

dp[s] is the minimum stickers required for string s (-1 if impossible). Note s is sorted.
clearly, dp[""] = 0, and the problem asks for dp[target].
The DP formula is:

dp[s] = min(1+dp[reduced_s]) for all stickers, 
here reduced_s is a new string after certain sticker applied
Optimization: If the target can be spelled out by a group of stickers, at least one of them has to contain character target[0]. So I explicitly require next sticker containing target[0], which significantly reduced the search space.

BTW, I am not good at Java. Looking forward to your revision!
*/

// C++

class Solution {
public:
    int minStickers(vector<string>& stickers, string target) {
        int m = stickers.size();
        vector<vector<int>> mp(m, vector<int>(26, 0));
        unordered_map<string, int> dp;
        // count characters a-z for each sticker 
        for (int i = 0; i < m; i++) 
            for (char c:stickers[i]) mp[i][c-'a']++;
        dp[""] = 0;
        return helper(dp, mp, target);
    }
private:
    int helper(unordered_map<string, int>& dp, vector<vector<int>>& mp, string target) {
        if (dp.count(target)) return dp[target];
        int ans = INT_MAX, n = mp.size();
        vector<int> tar(26, 0);
        for (char c:target) tar[c-'a']++;
        // try every sticker
        for (int i = 0; i < n; i++) {
            // optimization
            if (mp[i][target[0]-'a'] == 0) continue; 
            string s;
            // apply a sticker on every character a-z
            for (int j = 0; j < 26; j++) 
                if (tar[j]-mp[i][j] > 0) s += string(tar[j]-mp[i][j], 'a'+j);
            int tmp = helper(dp, mp, s);
            if (tmp!= -1) ans = min(ans, 1+tmp);
        }
        dp[target] = ans == INT_MAX? -1:ans;
        return dp[target];
    }
};

// Java

class Solution {
    public int minStickers(String[] stickers, String target) {
        int m = stickers.length;
        int[][] mp = new int[m][26];
        Map<String, Integer> dp = new HashMap<>();
        for (int i = 0; i < m; i++) 
            for (char c:stickers[i].toCharArray()) mp[i][c-'a']++;
        dp.put("", 0);
        return helper(dp, mp, target);
    }
    private int helper(Map<String, Integer> dp, int[][] mp, String target) {
        if (dp.containsKey(target)) return dp.get(target);
        int ans = Integer.MAX_VALUE, n = mp.length;
        int[] tar = new int[26];
        for (char c:target.toCharArray()) tar[c-'a']++;
        // try every sticker
        for (int i = 0; i < n; i++) {
            // optimization
            if (mp[i][target.charAt(0)-'a'] == 0) continue;
            StringBuilder sb = new StringBuilder();
            // apply a sticker on every character a-z
            for (int j = 0; j < 26; j++) {
                if (tar[j] > 0 ) 
                    for (int k = 0; k < Math.max(0, tar[j]-mp[i][j]); k++)
                        sb.append((char)('a'+j));
            }
            String s = sb.toString();
            int tmp = helper(dp, mp, s);
            if (tmp != -1) ans = Math.min(ans, 1+tmp);
        }
        dp.put(target, ans == Integer.MAX_VALUE? -1:ans);
        return dp.get(target);
    }
}

// Python

class Solution(object):
    def minStickers(self, stickers, target):
        m = len(stickers)
        mp = [[0]*26 for y in range(m)] 
        for i in range(m):
            for c in stickers[i]:
                mp[i][ord(c)-ord('a')] += 1    
        dp = {}
        dp[""] = 0
        
        def helper(dp, mp, target):
            if target in dp:
                return dp[target]
            n = len(mp)
            tar = [0]*26
            for c in target:
                tar[ord(c)-ord('a')] += 1   
            ans = sys.maxint
            for i in xrange(n):
                if mp[i][ord(target[0])-ord('a')] == 0:
                    continue
                s = ''
                for j in range(26):
                    if tar[j] > mp[i][j]:
                        s += chr(ord('a')+j)*(tar[j] - mp[i][j]) 
                tmp = helper(dp, mp, s)
                if (tmp != -1): 
                    ans = min(ans, 1+tmp)    
            dp[target] = -1 if ans == sys.maxint else ans
            return dp[target]
                
        return helper(dp, mp, target)

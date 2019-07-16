class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        array<int, 256> memo;
        fill(memo.begin(), memo.end(), 0);
        int i = 0, j = 0;
        int res = 0;
        while (j < s.size()) {
            // move j
            while (j < s.size()) {
                memo[s[j]]++;
                if (memo[s[j]] == 2)
                    break;
                j++;
            }
            res = max(res, j-i);
            // move i
            if (j == s.size())
                break;
            while (memo[s[j]] == 2) {
                memo[s[i]]--;
                i++;
            }
            j++;
        }
        return res;
    }

    // better, faster, directly jump to the repitition
    int lengthOfLongestSubstring(string s) {
        if(s.empty())
            return 0;
        int n=s.size();
        int max=1,curr=1,prev;
        int visited[256];
        for(int i=0;i<256;i++)
        {
            visited[i]=-1;
        }
        visited[s[0]]=0;
        for(int i=1;i<n;i++)
        {
            prev=visited[s[i]];
            if((prev==-1)||(i-curr>prev))
                curr++;
            else
            {
                if(curr>max)
                    max=curr;
                curr=i-prev;
            }
            visited[s[i]]=i;
        }
        if(curr>max)
            max=curr;
        return max;
    }
};

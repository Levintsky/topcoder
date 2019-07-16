class Solution {
public:
    int compress(vector<char>& chars) {
        int n = chars.size();
        if (n == 0)
            return 0;
        int i = 0, j;
        vector<int> cnt;
        vector<char> cs;
        while (i < n) {
            j = i + 1;
            while (j < n && chars[j] == chars[i])
                j++;
            cs.push_back(chars[i]);
            cnt.push_back(j-i);
            i = j;
        }
        int index = 0;
        for (int i = 0; i < cs.size(); ++i) {
             chars[index] = cs[i];
            index++;
            if (cnt[i] > 1) {
                string tmp = to_string(cnt[i]);
                for (int j = 0; j < tmp.size(); j++)
                    chars[index++] = tmp[j];
            }
        }
        chars.resize(index);
        return index;
    }
};

// better solution
class Solution {
public:
    int compress(vector<char>& chars) {
        int i=0,j=1;
        int n=chars.size(),cnt=1;
        for(j=1,cnt=1;j<=n;j++,cnt++)
        {
            if(j==chars.size() || chars[j]!=chars[j-1] )
            {  chars[i++]=chars[j-1];
            if(cnt>=2)
                for(char c : to_string(cnt))
                    chars[i++]=c;
                cnt=0;
            }
            
        }
        return i;
        
        
    }
};

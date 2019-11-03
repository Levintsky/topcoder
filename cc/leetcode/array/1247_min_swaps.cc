class Solution {
public:
    int minimumSwap(string s1, string s2) {
        int len = s1.size();
        int s1x = 0, s1y = 0;
        for (int i = 0; i < s1.size(); ++i) {
            if (s1[i] != s2[i]) {
                if (s1[i] == 'x')
                    s1x++;
                else
                    s1y++;
            }
        }
        if ((s1x + s1y) % 2 == 1)
            return -1;
        int result = s1x / 2 + s1y / 2;
        if (s1x % 2 == 1)
            result += 2;
        return result;
    }
};

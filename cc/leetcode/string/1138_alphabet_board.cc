class Solution {
public:
    
    string alphabetBoardPath(string target) {
        if (target == "")
            return "";
        string res;
        int n = target.size();
        target = 'a' + target;
        for (int i = 0; i < n; ++i) {
            char c1 = target[i], c2 = target[i+1];
            auto pos1 = charPos(c1);
            auto pos2 = charPos(c2);
            if (c1 == 'z') {
                res += gen(pos1.first, pos2.first, 'U', 'D');
                res += gen(pos1.second, pos2.second, 'L', 'R');
            } else {
                res += gen(pos1.second, pos2.second, 'L', 'R');
                res += gen(pos1.first, pos2.first, 'U', 'D');
            }
            res += '!';
        }
        return res;
    }
    
    pair<int, int> charPos(char c) {
        int tmp = c - 'a';
        return make_pair(tmp / 5, tmp % 5);
    }
    
    string gen(int n1, int n2, char c1, char c2) {
        string res;
        if (n1 > n2) {
            for (int i = 0; i < n1-n2; ++i)
                res += c1;
        } else {
            for (int i = 0; i < n2-n1; ++i)
                res += c2;
        }
        return res;
    }
};

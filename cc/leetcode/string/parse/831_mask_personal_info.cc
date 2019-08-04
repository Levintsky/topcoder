class Solution {
public:
    string maskPII(string S) {
        bool email = false;
        int i = 0;
        for (char c : S) {
            if (c == '@') {
                email = true;
                break;
            }
        }
        string res;
        if (email) {
            res += S[0];
            for (i = 1; i < S.size(); ++i) {
                if (S[i] == '@') {
                    res += "*****";
                    res += S[i-1];
                    res += S[i];
                    break;
                }
            }
            // S[i+1..]
            res += S.substr(i+1, S.size()-i-1);
            transform(res.begin(), res.end(), res.begin(), ::tolower);
        } else {
            for (char c : S) {
                if (c >= '0' && c <= '9')
                    res += c;
            }
            if (res.size() == 10) {
                res = "***-***-" + res.substr(6, 4);
            } else {
                int aux = res.size() - 10;
                string tmp = "+";
                for (i = 0; i < aux; ++i)
                    tmp += '*';
                tmp += "-***-***-" + res.substr(res.size()-4, 4);
                res = tmp;
            }
        }
        return res;
    }
};

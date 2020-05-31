class Solution {
public:
    string toGoatLatin(string S) {
        stringstream is(S);
        string s;
        string result;
        unordered_set<char> vowel{'a','e','i','o','u','A','E','I','O','U'};
        int cnt = 1;
            
        while (is >> s) {
            
            if (vowel.find(s[0]) == vowel.end()) {
                int n = s.size();
                s = s.substr(1, n-1) + s[0];
            }
            s += "ma";
            s += string(cnt, 'a');
            result += s;
            result += ' ';
            cnt++;
        }
        result = result.substr(0, result.size()-1);
        return result;
    }
};

class Solution {
public:
    string reverseParentheses(string s) {
        // edge case: no '(' or ')' in s
        if (s.find('(') == std::string::npos)
            return s;
        
        // parse string
        vector<string> stack;
        int cnt = 0;
        string curr = "";
        for (char c : s) {
            if (c == '(')
                cnt++;
            else if (c == ')')
                cnt--;
            curr += c;
            if (cnt == 0) {
                stack.push_back(curr);
                curr = "";
            }   
        }
        // edge case: "(xxxx)"
        if (stack.size() == 1) {
            string sub = s.substr(1, s.size()-2);
            string res = reverseParentheses(sub);
            reverse(res.begin(), res.end());
            return res;
        } else {
            string res;
            for (string s : stack) {
                res += reverseParentheses(s);
            }
            return res;
        }
    }
};

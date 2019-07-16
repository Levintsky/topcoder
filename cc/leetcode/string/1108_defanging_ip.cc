class Solution {
public:
    string defangIPaddr(string address) {
        string res = "";
        for (auto c : address) {
            if (c != '.')
                res += c;
            else
                res += "[.]";
        }
        return res;
    }
};

class Solution {
public:
    string addStrings(string num1, string num2) {
        string res;
        reverse(num1.begin(), num1.end());
        reverse(num2.begin(), num2.end());
        
        int i = 0, carry = 0;
        while (i < num1.size() || i < num2.size()) {
            int tmp = 0;
            if (i < num1.size())
                tmp += num1[i] - '0';
            if (i < num2.size())
                tmp += num2[i] - '0';
            if (carry > 0)
                tmp += carry;
            if (tmp < 10) {
                res += '0' + tmp;
                carry = 0;
            } else {
                tmp -= 10;
                res += '0' + tmp;
                carry = 1;
            }
            i++;
        }
        if (carry > 0)
            res += '1';
        reverse(res.begin(), res.end());
        return res;
    }
};

class Solution {
public:
    vector<int> plusOne(vector<int>& digits) {
        reverse(digits.begin(), digits.end());
        int carry = 0;
        for (int i = 0; i < digits.size(); i++) {
        	if (i == 0 || carry == 1)
        		digits[i]++;
        	if (digits[i] == 10) {
        		carry = 1;
                digits[i] = 0;
            } else {
                carry = 0;
        		break;
            }
        }
        if (carry > 0)
        	digits.push_back(1);
        reverse(digits.begin(), digits.end());
        return digits;
    }
};
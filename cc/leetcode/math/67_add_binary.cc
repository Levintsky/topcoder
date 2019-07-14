#include <iostream>

using namespace std;

class Solution {
public:
    string addBinary(string a, string b) {
    	reverse(a.begin(), a.end());
        reverse(b.begin(), b.end());
        string res;
        int carry = 0;
        for (int i = 0; i < max(a.size(), b.size()); ++i) {
        	int item = 0;
        	if (i < a.size() and a[i] == '1')
        		item++;
        	if (i < b.size() and b[i] == '1')
        		item++;
        	item += carry;
        	if (item > 1) {
        		carry = 1;
        		item -= 2;
        	} else
        		carry = 0;
        	res += to_string(item);
        }
        if (carry == 1)
        	res += '1';
        reverse(res.begin(), res.end());
        return res;
    }
};

int main() {
	Solution a;
	cout << a.addBinary("11", "1") << endl;
	cout << a.addBinary("1010", "1011") << endl;

    return 0;
}
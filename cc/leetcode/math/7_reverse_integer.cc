#include <iostream>
#include <math.h>

using namespace std;

class Solution {
public:
    int reverse(int x) {
    	bool flag = true;
        long x2 = x;
    	if (x2 < 0) {
    		flag = false;
    		x2 = -x2;
    	}
    	long res = 0;
    	while (x2 > 0) {
    		res = res * 10 + x2 % 10;
    		x2 = x2 / 10;
    		if (res > pow(2, 31) - 1)
    			return 0;
    		if (res < -pow(2, 31))
    			return 0;
    	}
    	if (flag)
    		return res;
    	else
    		return -res;
    }
};

int main() {
	Solution a;
	cout << a.reverse(123) << endl;
	cout << a.reverse(-123) << endl;
	int x = pow(2, 31) - 1;
	cout << a.reverse(x) << endl;
	x = -pow(2, 31);
	cout << a.reverse(x) << endl;

	return 0;
}
#include <iostream>

using namespace std;

class Solution {
public:
    int mySqrt(int x) {
        if (x < 2)
            return x;
        int l = 1, r = x;
        while (true) {
            int mid = (l + r) / 2;
            if (mid * mid > x)
                r = mid - 1;
            else {
            	if ((mid + 1) * (mid + 1) > x)
            		return mid;
            	l = mid + 1;
            	// last = l;
            }
        }
    }
};

int main() {
	Solution a;

    for (int i = 0; i < 10; ++i)
  		cout << i << " " << a.mySqrt(i) << endl;
}
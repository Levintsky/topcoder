#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    int sumOfDigits(vector<int>& A) {
    	int min_ = A[0];
    	for (auto item : A)
    		min_ = min(min_, item);
    	// get sum of digits
    	int res = 0;
    	while (min_ > 0) {
    		res += min_ % 10;
    		min_ /= 10;
    	}
    	if (res % 2 == 0)
    		return 1;
    	else
    		return 0;
    }
};

int main() {
	Solution a;
	// vector<int> A = {34,23,1,24,75,33,54,8};
	vector<int> A = {99,77,33,66,55};
	cout << a.sumOfDigits(A) << endl;
	return 0;
}
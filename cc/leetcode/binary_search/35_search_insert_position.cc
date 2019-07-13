#include <algorithm> 
#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    int searchInsert(vector<int>& nums, int target) {
        int l = 0, r = nums.size();
        while (l < r) {
        	int mid = (l+r)/2;
        	if (nums[mid] == target)
        		return mid;
        	else if (nums[mid] > target)
        		r = mid;
        	else
        		l = mid+1;
        }
        return l;
    }
};

int main() {
	Solution a;
	vector<int> v = {1,3,5,6};
	std::vector<int> test = {0,1,2,3,4,5,6,7};
	for (auto i : test)
		cout << i << " " << a.searchInsert(v, i) << endl;

	return 0;
}
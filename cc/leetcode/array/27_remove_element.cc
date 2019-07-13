#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
    	int n = nums.size();
    	int i = 0, j = 0;
    	for (int j = 0; j < n; ++j) {
    		if (nums[j] != val) {
    			nums[i] = nums[j];
    			i++;
    		}
    	}
        return i;
    }
};

void print_arr(vector<int>& arr) {
	for (int i = 0; i < arr.size(); ++i)
		cout << arr[i] << " ";
	cout << endl;
}

int main() {
	Solution a;
	vector<int> nums = {3,2,2,3};
	cout << a.removeElement(nums, 3) << endl;
	print_arr(nums);
	return 0;
}
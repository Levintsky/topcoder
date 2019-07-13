#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        int n = nums.size();
        if (n == 0)
        	return 0;
        int i = 0, j = 0;
        while (j < n) {
        	while (j < n and nums[j] == nums[i])
        		j++;
        	i++;
        	if (j == n)
        		break;
        	nums[i] = nums[j];
        }
        return i;
    }

    int solve2(vector<int>& nums) {
        if(nums.size()==0) return 0;
        int i=0;
        for(int j=1; j<nums.size(); j++){
            if(nums[i]!=nums[j]){
                nums[++i] = nums[j];
            }
        }
        return i+1;
    }
};

void print_arr(vector<int>& arr) {
	for (int i = 0; i < arr.size(); ++i)
		cout << arr[i] << " ";
	cout << endl;
}

int main() {
	Solution a;
	vector<int> arr = {1, 1, 2};
	cout << a.removeDuplicates(arr) << endl;
	print_arr(arr);
	vector<int> arr2 = {0,0,1,1,1,2,2,3,3,4};
	cout << a.removeDuplicates(arr2) << endl;
	print_arr(arr2);
}
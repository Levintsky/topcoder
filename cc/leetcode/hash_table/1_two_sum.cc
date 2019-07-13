#include <vector>
#include <iostream>
#include <unordered_map>

using namespace std;

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        vector<int> result;
        
        unordered_map<int, int> record;
        for (int i = 0; i < nums.size(); ++i) {
            int item = nums[i];
            if (record.find(target-item) != record.end() ) {
                result.push_back(record[target-item]);
                result.push_back(i);
                break;
            } else {
                record[item] = i;
            }
        }
        return result;
    }
};

int main() {
    Solution a;
    const int arr[] = {2, 7, 11, 15};
    vector<int> input(arr, arr+4);

    vector<int> result = a.twoSum(input, 9);

    for (int i = 0; i < result.size(); ++i)
        cout << result[i] << endl;
    return 0;
}

#include <iostream>
#include <string>
#include <vector>

using namespace std;

class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        int n = strs.size();
        if (n == 0)
			return string("");
		else if (n == 1)
			return strs[0];
		size_t max_length = strs[0].length();
		for (int i = 1; i < strs.size(); ++i)
			max_length = min(max_length, strs[i].length());

		string result;
		for (int i = 0; i < max_length; ++i) {
			char c = strs[0][i];
			for (int j = 0; j < strs.size(); ++j) {
				if (strs[j][i] != c)
					return result;
			}
			result += c;
		}
		return result;
    }
};

int main() {
	vector<string> strs = {"abc", "add"};
	Solution a;
	cout << a.longestCommonPrefix(strs) << endl;
	return 0;
}

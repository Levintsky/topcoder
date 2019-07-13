#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    int lengthOfLastWord(string s) {
    	if (s == "")
            return 0;
        vector<string> arr;
    	int i = 0;
    	while (i < s.size()) {
    		if (s[i] == ' ') {
    			++i;
    			continue;
    		}
    		int j = i + 1;
    		while (j < s.size() and s[j] != ' ')
    			j++;
    		arr.push_back(s.substr(i, j-i));
    		i = j + 1;
    	}
        if (arr.size() > 0)
        	return arr[arr.size()-1].size();
        else
            return 0;
    }
};

int main() {
	Solution a;
	cout << a.lengthOfLastWord("Hello World") << endl;
	cout << a.lengthOfLastWord("helloo") << endl;

	return 0;
}
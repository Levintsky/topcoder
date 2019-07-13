#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    string countAndSay(int n) {
        vector<int> a1 = {1};
        vector<int> a2;
        
        while (n > 1) {
        	int i = 0;
	        while ( i < a1.size()) {
	        	int j = i+1;
	        	while (j < a1.size() && a1[j] == a1[j-1])
	        		++j;
	        	a2.push_back(j-i);
	        	a2.push_back(a1[i]);
	        	i = j;
	        }
	        a1 = a2;
	        a2.clear();
	        n--;
	    }
	    string res;
	    for (auto i : a1) {
	    	res += to_string(i);
	    }
	    return res;
    }
};

int main() {
	Solution a;
	cout << a.countAndSay(2) << endl;
	cout << a.countAndSay(4) << endl;
	cout << a.countAndSay(4) << endl;
	return 0;
}
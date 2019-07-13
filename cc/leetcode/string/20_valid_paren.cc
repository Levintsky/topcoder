#include <iostream>
#include <stack>
#include <unordered_map>

using namespace std;

class Solution {
public:
    bool isValid(string s) {
        stack<char> st;

		unordered_map<char, char> map({
									{')', '('}, 
									{']', '['}, 
									{'}', '{'}
									});
		int n = s.length();

		for (int i = 0; i < n; ++i) {
			char c = s[i];
			if (s[i] == '(' or s[i] == '[' or s[i] == '{')
				st.push(s[i]);
			else {
				if (st.size() > 0 and st.top() == map[c])
					st.pop();
				else
					return false;
			}
		}
		return st.size() == 0;
    }
};

int main() {
	Solution a;
	cout << a.isValid("()[]{}");
}

/*
To solve this problem, we must keep in heart the following points:

We know the cut point must come from the one string, assumed it is called c-string.
Then except the c-string, all the other string must become its lexicographically biggest status, assumed it is called b-status. Since only in this situation, we could get the lexicographically biggest string after cutting.
To reach the point 2, we need to first let all the string reach its b-status for the convenience of traversing all the strings afterward.
Then, for each string's traversal procedure, we need to decide whether it should be reversed or not since we don't know which might generate the final answer, and then we enumerated all the characters in this string.
*/

class Solution {
public:
    int n;
    string ans = "";
    // solve function: flag - whether we need to reverse the string; i - the ith string in the strs
    void solve(vector<string>& strs, int i, bool flag) {
        string temp = strs[i]; // intermediate string for not disturbing the original structure of 'strs'
        if (flag) reverse(temp.begin(), temp.end());
        int size = (int)temp.size();
        string str1 = "", str2 = "";
        for (int j=i+1; j<n; ++j) str1 += strs[j]; // Concatenate all the string behind the strs[i]
        for (int j=0; j<i; ++j) str2 += strs[j]; // Concatenate all the string before the strs[i]
        // traverse all the string character
        for (int k=0; k<size; ++k) {
            string newOne = temp.substr(k) + str1 + str2 + temp.substr(0, k); // cut and find the regular string
            ans = ans == "" ? newOne : max(ans, newOne); // update the ans
        }
    }
    // Reach the b-status for all the strings.
    void findMaxStrings(vector<string>& strs) {
        for (int i=0; i<n; ++i) {
            string temp = strs[i];
            reverse(temp.begin(), temp.end());
            strs[i] = strs[i] > temp ? strs[i] : temp;
        }
    }
    // Main function
    string splitLoopedString(vector<string>& strs) {
        n = (int)strs.size();
        if (n == 0) return "";
        findMaxStrings(strs);
        for (int i=0; i<n; ++i) {
            // we dont's know which will generate the final answer, so we traverse both situations.
            solve(strs, i, true); // reverse the string situation
            solve(strs, i, false); // not reverse the string situation
        }
        return ans;
    }
};

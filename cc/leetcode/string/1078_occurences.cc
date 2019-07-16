class Solution {
public:
    vector<string> findOcurrences(string text, string first, string second) {
        vector<string> ans;
        string t = first + " " + second+" ";
        int n = t.length();
        int i = 0,j=0;
        while(i<text.size()){
            i = text.find(t, i);
            if(i==string::npos){
                break;
            }
            j = text.find(" ", i+n);
            ans.push_back(text.substr(i+n, j-i-n));
            i += n;
        }
        return ans;
    }
};

// smarter
class Solution {
public:
    vector<string> findOcurrences(string text, string first, string second) {
        vector<string> ans;
        string t = first + " " + second+" ";
        int n = t.length();
        int i = 0,j=0;
        while(i<text.size()){
            i = text.find(t, i);
            if(i==string::npos){
                break;
            }
            j = text.find(" ", i+n);
            ans.push_back(text.substr(i+n, j-i-n));
            i += n;
        }
        return ans;
    }
};

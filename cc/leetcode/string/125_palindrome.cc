class Solution {
public:
    bool isPalindrome(string s) {
        int i = 0, j = s.size() - 1;
        while (i < j) {
            while (!is_char(s[i]) && !is_num(s[i]) && i < j)
                ++i;
            while (!is_char(s[j]) && !is_num(s[j]) && i < j)
                --j;
            if (i >= j)
                break;
            // cout << i << " " << j << endl;
            if (is_num(s[i]) && is_num(s[j])) {
                if (s[i] != s[j])
                    return false;
            } else if (is_char(s[i]) && is_char(s[j])) {                
                if (ind(s[i]) != ind(s[j]))
                    return false;
            } else
                return false;
            ++i;
            --j;
        }
        return true;
    }
    
    bool is_char(char c) {
        if (c >= 'A' && c <= 'Z')
            return true;
        if (c >= 'a' && c <= 'z')
            return true;
        return false;
    }
    bool is_num(char c) {
        return c >= '0' && c <= '9';
    }
    int ind(char c) {
        if (c >= 'A' && c <= 'Z')
            return c - 'A';
        if (c >= 'a' && c <= 'z')
            return c - 'a'; 
        return -1;
    }
};
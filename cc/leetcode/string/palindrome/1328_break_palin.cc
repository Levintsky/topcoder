class Solution {
public:
    string breakPalindrome(string palindrome) {
        int n = palindrome.size();
        // case 1: len 1
        if (n == 1)
            return "";
        // case 2: all 'a'' case 3: aaaxaaa
        int i = 0;
        while (i < n && palindrome[i] == 'a')
            i++;

        if ((i == n) || (n % 2 == 1 && i == (n-1)/2)) {
            palindrome[n-1] = 'b';
            return palindrome;
        }

        // case 4: abcba
        palindrome[i] = 'a';
        return palindrome;
    }
};

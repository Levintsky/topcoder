class Solution {
public:
    bool validateStackSequences(vector<int>& pushed, vector<int>& popped) {
        stack<int> s;
        int iPush = 0, iPop = 0;
        while (iPop < popped.size() && iPush < pushed.size()) {
            if (s.size() > 0 && s.top() == popped[iPop]) {
                iPop++;
                s.pop();
            } else if (pushed[iPush] == popped[iPop]) {
                iPop++;
                iPush++;
            } else {
                s.push(pushed[iPush]);
                iPush++;
            }
        }
        while (s.size() > 0) {
            if (s.top() != popped[iPop])
                return false;
            s.pop();
            iPop++;
        }
        return true;
    }
};

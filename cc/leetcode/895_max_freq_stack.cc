class FreqStack {
    unordered_map<int, int> freq;
    unordered_map<int, stack<int>> memo;
    int max_f;
public:
    FreqStack() {
        max_f = 0;
    }
    
    void push(int x) {
        freq[x]++;
        int tmp_freq = freq[x];
        memo[tmp_freq].push(x);
        max_f = max(max_f, tmp_freq);
    }
    
    int pop() {
        int item = memo[max_f].top();
        freq[item]--;
        memo[max_f].pop();
        if (memo[max_f].size() == 0)
            max_f--;
        return item;
    }
};

/**
 * Your FreqStack object will be instantiated and called as such:
 * FreqStack* obj = new FreqStack();
 * obj->push(x);
 * int param_2 = obj->pop();
 */

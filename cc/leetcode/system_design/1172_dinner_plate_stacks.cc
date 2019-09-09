class DinnerPlates {
public:
    
    DinnerPlates(int capacity) {
        stacks.push_back({});
        active_list.insert(0);
        cap = capacity;
    }
    
    void push(int val) {
        int index = *active_list.begin();
        stacks[index].push(val);
        // if (pop_list.find(index) == pop_list.end())
        pop_list.insert(index);
        if (stacks[index].size() == cap) {
            active_list.erase(index);
            if (active_list.size() == 0) {
                stacks.push_back({});
                active_list.insert(stacks.size()-1);
            }
        }
    }
    
    int pop() {
        if (pop_list.size() == 0)
            return -1;
        int index = *pop_list.rbegin();
        int res = stacks[index].top();
        stacks[index].pop();
        active_list.insert(index);
        if (stacks[index].size() == 0)
            pop_list.erase(index);
        return res;
    }
    
    int popAtStack(int index) {
        if (index >= stacks.size() || stacks[index].size() == 0)
            return -1;
        int res = stacks[index].top();
        stacks[index].pop();
        if (stacks[index].size() == cap - 1)
            active_list.insert(index);
        if (stacks[index].size() == 0)
            pop_list.erase(index);
        return res;
    }
private:
    vector<stack<int>> stacks;
    set<int> active_list;
    set<int> pop_list;
    int cap;
};

/**
 * Your DinnerPlates object will be instantiated and called as such:
 * DinnerPlates* obj = new DinnerPlates(capacity);
 * obj->push(val);
 * int param_2 = obj->pop();
 * int param_3 = obj->popAtStack(index);
 */

/*
Solution 2
Use a map m to keep the mapping between index and stack
Use a set available to keep indices of all no full stacks.

C++:

    int c;
    map<int, vector<int>> m;
    set<int> available;

    DinnerPlates(int capacity) {
        c = capacity;
    }

    void push(int val) {
        if (!available.size())
            available.insert(m.size());
        m[*available.begin()].push_back(val);
        if (m[*available.begin()].size() == c)
            available.erase(available.begin());
    }

    int pop() {
        if (m.size() == 0)
            return -1;
        return popAtStack(m.rbegin()->first);
    }

    int popAtStack(int index) {
        if (m[index].size() == 0)
            return -1;
        int val = m[index].back();
        m[index].pop_back();
        available.insert(index);
        if (m[index].size() == 0)
            m.erase(index);
        return val;
    }
*/
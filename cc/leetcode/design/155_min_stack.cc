class MinStack {
public:
    /** initialize your data structure here. */
    vector<int> arr;
    int min_rec = INT_MAX;
    MinStack() {
        
    }
    
    void push(int x) {
        arr.push_back(x);
        min_rec = min(min_rec, x);
    }
    
    void pop() {
        if (arr.back() < min_rec)
            arr.pop_back();
        else {
            arr.pop_back();
            min_rec = INT_MAX;
            for (auto i : arr)
                min_rec = min(i, min_rec);
        }
    }
    
    int top() {
        return arr.back();
    }
    
    int getMin() {
        return min_rec;
    }
};

class MinStack {
 public:
  MinStack() {
    // do intialization if necessary
  }

  /*
   * @param number: An integer
   * @return: nothing
   */
  void push(int number) {
    int min = number;
    if (!_data_stack.empty()) {
      if (_min_stack.top() < number) {
        min = _min_stack.top();
      }
    }

    _data_stack.push(number);
    _min_stack.push(min);
  }

  /*
   * @return: An integer
   */
  int pop() {
    int top = _data_stack.top();
    _data_stack.pop();
    _min_stack.pop();
    return top;
  }

  int top() { return _data_stack.top(); }

  /*
   * @return: An integer
   */
  int getMin() { return _min_stack.top(); }

 private:
  stack<int> _data_stack;
  stack<int> _min_stack;
};
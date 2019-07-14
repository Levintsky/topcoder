// my solution
class MyStack {
public:
    /** Initialize your data structure here. */
    queue<int> q1;
    queue<int> q2;
    MyStack() {
        
    }
    
    /** Push element x onto stack. */
    void push(int x) {
        q1.push(x);
    }
    
    /** Removes the element on top of the stack and returns that element. */
    int pop() {
        while (q1.size() > 1) {
            q2.push(q1.front());
            q1.pop();
        }
        int item = q1.front();
        q1.pop();
        swap(q1, q2);
        return item;
    }
    
    /** Get the top element. */
    int top() {
        return q1.back();
    }
    
    /** Returns whether the stack is empty. */
    bool empty() {
        return q1.size() == 0;
    }
};

// better solution:
class Stack {
public:
	queue<int> que;
	// Push element x onto stack.
	void push(int x) {
		que.push(x);
		for(int i=0;i<que.size()-1;++i){
			que.push(que.front());
			que.pop();
		}
	}

	// Removes the element on top of the stack.
	void pop() {
		que.pop();
	}

	// Get the top element.
	int top() {
		return que.front();
	}

	// Return whether the stack is empty.
	bool empty() {
		return que.empty();
	}
};
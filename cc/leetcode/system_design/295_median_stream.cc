class MedianFinder {
    priority_queue<long> small, large;
public:

    void addNum(int num) {
        small.push(num);
        large.push(-small.top());
        small.pop();
        if (small.size() < large.size()) {
            small.push(-large.top());
            large.pop();
        }
    }

    double findMedian() {
        return small.size() > large.size()
               ? small.top()
               : (small.top() - large.top()) / 2.0;
    }
};

// Faster solution
class MedianFinder {
public:
    /** initialize your data structure here. */
    MedianFinder() {
    }
    
    //Always let minHeap.size() <= maxHeap.size()
    void addNum(int num) {
        if(maxHeap.empty()){
            maxHeap.push(num);
        }
        else if(maxHeap.size() == minHeap.size()){
            if(num >= minHeap.top()){
                maxHeap.push(minHeap.top());
                minHeap.pop();
                minHeap.push(num);
            }
            else{
                maxHeap.push(num);
            }
        }
        else{
            if(num >= maxHeap.top()){
                minHeap.push(num);
            }
            else{
                minHeap.push(maxHeap.top());
                maxHeap.pop();
                maxHeap.push(num);
            }
        }
    }
    
    double findMedian() {
        if(maxHeap.size() != minHeap.size()){
            return maxHeap.top();
        }
        else{
            return (minHeap.top() + maxHeap.top()) / 2.0;
        }
    }
    
private:
    priority_queue<int, vector<int>> maxHeap;
    priority_queue<int, vector<int>, greater<int>> minHeap;
};

// Another good solution with multiset
class MedianFinder {
public:
    /** initialize your data structure here. */
    MedianFinder() {
        _mid = _data.begin();
    }
    
    void addNum(int num) {
        _data.insert(num);
        if (_data.size() == 1) {
            _mid = _data.begin();
        } else if (num < *_mid) {
            _mid = _data.size() & 1 ? prev(_mid) : _mid; 
        } else {
            _mid = _data.size() & 1 ? _mid : next(_mid);
        }
    }
    
    double findMedian() {
        //auto mid = next(_data.begin(), _data.size() / 2);
        return (*_mid + *prev(_mid, 1 - (_data.size() & 1))) / 2;
    }
private:
    multiset<double> _data;
    multiset<double>::iterator _mid;
};

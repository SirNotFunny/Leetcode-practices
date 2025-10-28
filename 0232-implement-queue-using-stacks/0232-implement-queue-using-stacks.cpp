class MyQueue {
public:
    MyQueue() {
        //empty
    }
    
    void push(int x) {
        q.push(x);
        for(int i = 0; i<q.size(); i++){
            q.push(q.front());
            q.pop();
        }
    }
    
    int pop() {
        int val = q.front();
        q.pop();
        return val;
    }
    
    int peek() {
        return q.front();
    }
    
    bool empty() {
        return q.empty();
    }
    private:
        queue<int> q; //bien thanh vien
};

/**
 * Your MyQueue object will be instantiated and called as such:
 * MyQueue* obj = new MyQueue();
 * obj->push(x);
 * int param_2 = obj->pop();
 * int param_3 = obj->peek();
 * bool param_4 = obj->empty();
 */
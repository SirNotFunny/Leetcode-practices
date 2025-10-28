class MinStack {
public:
    MinStack() {
        minS.push(INT_MAX);
    }
    
    void push(int val) {
        mainS.push(val);
        minS.push(min(val, minS.top()));
    }
    
    void pop() {
        mainS.pop();
        minS.pop();
    }
    
    int top() {
        return mainS.top();
    }
    
    int getMin() {
        return minS.top();
    }
    private:
    stack<int> mainS;
    stack<int> minS; 
};

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack* obj = new MinStack();
 * obj->push(val);
 * obj->pop();
 * int param_3 = obj->top();
 * int param_4 = obj->getMin();
 */
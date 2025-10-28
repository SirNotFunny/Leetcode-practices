class MyStack {
public:
    MyStack() { //this is using q to simulate stack
        //empty
    }
    
    void push(int x) {
        q.push(x); //cho x vao cuoi phan tu
        for(int i=0; i<q.size()-1; i++){
            q.push(q.front()); //cho phan tu x vua cho vao day stack
            q.pop(); //pop gia tri dau cu vi da copy no o cuoi  
        }
    }
    
    int pop() { //xoa di phan tu va tra ve gia tri da bi xoa
        int val = q.front();
        q.pop();
        return val;
    }
    
    int top() {
        return q.front();
    }
    
    bool empty() {
        return q.empty();
    }
    private:
        queue<int> q; // biến thành viên
};

/**
 * Your MyStack object will be instantiated and called as such:
 * MyStack* obj = new MyStack();
 * obj->push(x);
 * int param_2 = obj->pop();
 * int param_3 = obj->top();
 * bool param_4 = obj->empty();
 */
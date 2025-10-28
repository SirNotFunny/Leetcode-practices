class Solution {
public:
    int evalRPN(vector<string>& tokens) {
        stack<int> s;
        for(const string& token : tokens){
            if(token.size() > 1 || isdigit(token[0])){
                s.push(stoi(token));
            }
            else{
                int secondTop = s.top();
                s.pop();
                int firstTop = s.top();
                s.pop();
                if(token[0] == '+'){
                    s.push(firstTop + secondTop);
                }
                else if (token[0] == '-'){
                    s.push(firstTop - secondTop);
                }
                else if(token[0] == '*'){
                    s.push(firstTop * secondTop);
                }
                else if(token[0] == '/'){
                    s.push(firstTop / secondTop);
                }
            }
        }
        return s.top();
    }
};
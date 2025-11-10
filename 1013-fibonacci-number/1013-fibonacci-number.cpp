class Solution {
public:
    int fib(int n) {
        long long memo[100];
        for(int i=0; i<100; i++){
            memo[i]=-1;
        }
        if(n<=1){
            return n;
        }
        if(memo[n]!=-1){
            return memo[n];
        }
        memo[n] = fib(n-1) + fib(n-2);
        return memo[n];
    }
};
int Solution::pow(int x, int n, int d) {
    // Do not write main() function.
    // Do not read input, instead use the arguments to the function.
    // Do not print the output, instead return values as specified
    // Still have a doubt. Checkout www.interviewbit.com/pages/sample_codes/ for more details
    
    if (n==0) return 1 % d;
    if (d==1) return 0;
    
    long long int ans = 1;
    long long int base = x;
    
    while (n>0){
        if (n & 1){
            ans = (ans * base) % d;
            n -= 1;
        }
        base = (base * base) % d;
        n >>= 1;
    }
    if (ans < 0) ans = (ans + d) % d;
    return ans;
}


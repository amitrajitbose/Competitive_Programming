# Kth Character In Double Decrypted String
#
#
string Solution::solve(string A, int B)
{
    stack<pair<string,long long int>>st;
    long long int len = 0,n=A.size(),freq;
    string temp;
    for(int i=0;i<n;i++){
        if(isalpha(A[i])){
            len++;
            temp = A[i];
            st.push({temp,len});
        }
        else{
            freq=0;
            while(i<n and isdigit(A[i])){
                freq = freq*10 +(A[i]-'0');
                i++;
            }
            if(freq*len>=B)
                break;
            len = len*freq;
            i--;
        }
    }
    while(!st.empty()){
        pair<string,long long int> p = st.top();
        st.pop();
        B = B%p.second;
        if(B==0)
            return p.first;
    }
}

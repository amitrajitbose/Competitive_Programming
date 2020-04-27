// LC 62
long long int comb(int m,int n)
{
     long long int res = 1, i;
     int a=(m>n)? m: n;
     for (i=m+n-2;i>=a; i--) 
         res *= i; 
    return res; 
}

long long int fact(int n)
{
    long long int res=1,i;
    for(i=2;i<=n;i++)
        res*=i;
    return res;
}

int Solution::uniquePaths(int m, int n) {
    long long int a,k=comb(m,n);
    if(m<n)
        a=fact(m-1); // since m is smaller
    else
        a=fact(n-1); // else as n is smaller
    return k/a;
}


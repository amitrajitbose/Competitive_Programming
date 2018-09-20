
/*
 * Author: Amitrajit Bose
 * Problem Link: https://www.codechef.com/problems/EQUALIZE
 * Approach: Binary
 */

#include<bits/stdc++.h>
#include <iostream>
#include<ctype.h>
#include<climits>
using namespace std;
typedef long long ll;
#define rep(m,n) for(i=m; i<(n); i++)
#define test ll t; cin>>t; while(t--)

int h[1001][1001];
int t[1001][1001];
int main()
{
    int n,m,query;
    cin >> n >> m >> query;

    for(int i=1;i<=n;i++)
    {
        for(int j=1;j<=m;j++)
        {
            cin >> h[i][j];
        }
    }

    // processing queries
    int k,l;
    for(int i=0; i<query;i++)
    {
        cin >> k >> l;
        int low=0;
        int high=10000000;
        int cnt = (k*l)/2 +1;
        k--;
        l--;

        while(low<high)
        {
            int mid = (low+high+1)/2;
            for(int p=1;p<=n;p++)
            {
                for(int q=1;q<=m;q++)
                {
                    t[p][q] = t[p-1][q]+t[p][q-1]-t[p-1][q-1]+(h[p][q]>=mid?1:0);
                }
            }
            int flag=1;
            for(int p=1;(p+k)<=n;p++)
            {
                for(int q=1;(q+l)<=m;q++)
                {
                    if((t[p+k][q+l] - t[p-1][q+l] - t[p+k][q-1] + t[p-1][q-1]) >= cnt)
                    {
                        low=mid;
                        flag=0;
                        break;
                    }
                }
                if(!flag)
                    break;
            }
            if(flag)
                high=mid-1;
        } 
        cout << low << endl;
    }
    return 0;
}
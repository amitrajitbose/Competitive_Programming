#include<bits/stdc++.h>
using namespace std;

int maxDepth(string S) 
{ 

    int current_max = 0; // current count 

    int max = 0;    // overall maximum count 

    int n = S.length(); 

    // Traverse the input string 

    for (int i = 0; i< n; i++) 

    { 

        if (S[i] == '(') 

        { 

            current_max++; 

            // update max if required 

            if (current_max> max) 

                max = current_max; 

        } 

        else if (S[i] == ')') 

        { 

            if (current_max>0) 

                current_max--; 

            else

                return -1; 

        } 

    } 

    if (current_max != 0) 

        return -1; 

    return max; 
}

int main()
{
    int t;
    cin >> t;
    while(t--)
    {
        string s;
        cin>>s;
        cout<<maxDepth(s)<<endl;
    }
    return 0;
}
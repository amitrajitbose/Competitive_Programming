#include<bits/stdc++.h>
#include<fstream>
//#define s(x) scanf("%d",&(x))
#define print(x) printf("%d ",x)
#define printnl(x) printf("%d\n",x);
#define fi(i,a,b) for(int i=(a);i<(b);i++)
#define fd(i,a,b) for(int i=(a);i>(b);--i)
#define MOD 1000000009
#define infy 1e18
#define llu  long long unsigned
#define ll long long
#define tr(container, it) for(typeof(container.begin()) it = container.begin(); it != container.end(); it++)
/*By using these macros we can traverse every kind of container, not only vector. This will produce const_iterator for const object and normal iterator for non-const object, and you will never get an error here.
 void f(const vector<int>& v) {
      int r = 0;
      tr(v, it) {
           r += (*it)*(*it);
      }
      return r;
 }*/
#define sz(a) int((a).size())
#define all(c) c.begin(), c.end() 	// sort(X.rbegin(), X.rend()); // Sort array in descending order using with reverse iterators
#define pb push_back		//Push_back adds an element to the end of vector, increasing its size by one
#define isEmpty(v) = v.empty();	//using v.size() takes O(n)
using namespace::std;
 
typedef vector <int> vi;	//The following operations are defined for iterators: get value of an iterator, int x = *it; , increment and decrement iterators it1++, it2--; , compare iterators by '!=' and by '<' , add an immediate to iterator it += 20; <=> shift 20 elements forward , get the distance between iterators, int n = it2-it1; ,  Not only can they operate on any container, they may also perform, for example, range checking and profiling of container usage.
				//The type of iterator can be constructed by a type of container by appending “::iterator”, “::const_iterator”, “::reverse_iterator” or “::const_reverse_iterator” to it. use '!=' instead of '<', and 'empty()' instead of 'size() != 0' -- for some container types, it’s just very inefficient to determine which of the iterators precedes another.
typedef vector<vi> vvi;		//vector< vector<int> > Matrix(N, vector<int>(M, -1));
typedef pair < int, int > ii;	//Pairs are compared first-to-second element. If the first elements are not equal, the result will be based on the comparison of the first elements only; the second elements will be compared only if the first ones are equal. The array (or vector) of pairs can easily be sorted by STL internal functions.(convex hull - For example, if you want to sort the array of integer points so that they form a polygon, it’s a good idea to put them to the vector< pair<double, pair<int,int> >, where each element of vector is { polar angle, { x, y } }. One call to the STL sorting function will give you the desired order of points. )
typedef vector < ii > vii;
typedef vector <vii> vvii;
 
/** sets and maps **/
// set and map have the member functions find() and count(), which works in O(log N), while std::find() and std::count() take O(N).
#include <cstdio>
int cnt = 0;
vector<llu> s(1000010, 0), e(s), b(s);
int bs(int x, int n)
{
    cnt = 0;
    int l = 0, h = n-1, m;
    while(h - l >= 2)
    {
        m = (l+h)>>1;
        if(b[m] >= x)
            l = m;
        else
            h = m-1;
            /** MAKE THE PROGRAM OUTPUT WRONG RESULT IF BS() ENTERS INFINITE LOOP**/
            if(cnt++ > 1000)
                return -1;
    }
    m = (l + h)>>1;
    if(b[h] >= x)
        return h+1;
    if(b[l] >= x)
        return l+1;
    return 0;
}
int main()
{
//   freopen("in.txt", "r", stdin);
ios_base::sync_with_stdio(0);
cin.tie(0);
ll n, m, q, l, r, x;
cin>>n>>m;
fi(i, 0, m)
{
    cin>>l>>r;
    s[l-1]++;
    e[r-1]++;
}
 
ll run_sum = 0;
fi(i, 0, n)
{
    b[i] = s[i] + run_sum;
    run_sum += (s[i] - e[i]);
}
//fi(i, 0, n)
//cout<<b[i]<<' ';
//vector<llu> ausi(b.begin(), b.begin() + n);
//sort(ausi.rbegin(), ausi.rend());
//fi(i, 0, n)
//b[i] = ausi[i];
 
sort(b.rbegin() + 1000010 - n, b.rend());
//fi(i, 0, n)
//cout<<b[i]<<' ';
cin>>q;
fi(i, 0, q)
{
    cin>>x;
    cout<<bs(x, n)<<endl;
}
return 0;
}
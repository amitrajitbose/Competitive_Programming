#include <bits/stdc++.h>
using namespace std;

#define rep(i, a, b) for(int i = a; i < (b); ++i)
#define trav(a, x) for(auto& a : x)
#define all(x) x.begin(), x.end()
#define sz(x) (int)(x).size()
typedef long long ll;
typedef long double ld;
typedef pair<int, int> pii;
typedef vector<int> vi;

const ll big = 1000000007;

const int inf = 1e9;
struct Node {
    Node *L = 0, *R = 0;
    int lo, hi, mset = inf, madd = 0, val = -inf;
    Node(int lo,int hi):lo(lo),hi(hi){} // Large interval of -inf
    Node(vi& v, int lo, int hi) : lo(lo), hi(hi) {
        if (lo + 1 < hi) {
            int mid = lo + (hi - lo)/2;
            L = new Node(v, lo, mid); R = new Node(v, mid, hi);
            val = max(L->val, R->val);
        }
        else val = v[lo];
    }
    int query(int from, int to) {
        if (to <= lo || hi <= from) return -inf;
        if (from <= lo && hi <= to) return val;
        push();
        return max(L->query(from, to), R->query(from, to));
    }
    void set(int from, int to, int x) {
        if (to <= lo || hi <= from) return;
        if (from <= lo && hi <= to) mset = val = x, madd = 0;
        else {
            push(), L->set(from, to, x), R->set(from, to, x);
            val = max(L->val, R->val);
        }
    }
    void add(int from, int to, int x) {
        if (to <= lo || hi <= from) return;
        if (from <= lo && hi <= to) {
            if (mset != inf) mset += x;
            else madd += x;
            val += x;
        }
        else {
            push(), L->add(from, to, x), R->add(from, to, x);
            val = max(L->val, R->val);
        }
    }
    void push() {
        if (!L) {
            int mid = lo + (hi - lo)/2;
            L = new Node(lo, mid); R = new Node(mid, hi);
        }
        if (mset != inf)
            L->set(lo,hi,mset), R->set(lo,hi,mset), mset = inf;
        else if (madd)
            L->add(lo,hi,madd), R->add(lo,hi,madd), madd = 0;
    }
};

struct Tree {
    typedef int T;
    const T LOW = -1234567890;
    T f(T a, T b) { return max(a, b); }

    int n;
    vi s;
    Tree() {}
    Tree(int m, T def=0) { init(m, def); }
    void init(int m, T def) {
        n = 1; while (n < m) n *= 2;
        s.assign(n + m, def);
        s.resize(2 * n, LOW);
        for (int i = n; i --> 1; )
            s[i] = f(s[i * 2], s[i*2 + 1]);
    }
    void update(int pos, T val) {
        pos += n;
        s[pos] = val;
        for (pos /= 2; pos >= 1; pos /= 2)
            s[pos] = f(s[pos * 2], s[pos * 2 + 1]);
    }
    T query(int a, int b) { return que(1, a, b, 0, n); }
    T que(int pos, int a, int b, int x, int y) {
        if (a >= b) return LOW;
        if (a == x && b == y) return s[pos];
        int m = (x + y) / 2;
        return f(que(2 * pos, a, min(b, m), x, m),
                que(2 * pos + 1, max(a, m), b, m, y));
    }
};

ll n,m,k,T;

ll F[40] = {0};

vector<ll> L;
vector<ll> R;
vector<ll> ind;
vector<ll> kind;
vector<vector<ll> > C(100001, vector<ll>());

ll MA[100001] = {0};

ll ANS[100001] = {0};

int main() {

  //  freopen("input.txt","r",stdin);
    //freopen("autput.txt","w",stdout);

    ll a,b,c,d;

    cin >> T;
    for(ll c4 = 0; c4 < T; c4++){
        cin >> m >> n;
        L.clear();
        R.clear();
        kind.clear();
        ind.clear();
        for(ll c1 = 0; c1 < m; c1++){
            C[c1].clear();
            MA[c1]= 0;
        }
        for(ll c1 = 0; c1 < n; c1++){
            ANS[c1+1] = 13333337;
            char ch;
            cin >> ch;
            a = 1;
            if(ch == 'E' || ch == 'C')a = 0;
            kind.push_back(a);
        }
        for(ll c1 = 0; c1 < n; c1++){
            cin >> a;
            a--;
            L.push_back(a);
        }
        for(ll c1 = 0; c1 < n; c1++){
            cin >> b;
            b--;
            R.push_back(b);
            if(b > L[c1]){
                C[b].push_back(c1);
            }
            ind.push_back(c1);
        }

        vi v1;
        vi v2;
        for(int c1 = 0; c1 < m; c1++){
            v1.push_back(0);
            v2.push_back(0);
        }

        Node* st1 = new Node(v1,0,m);
        Node* st2 = new Node(v2,0,m);

       // Tree st1(m);
       // Tree st2(m);

        for(ll c1 = 0; c1 < m; c1++){
            for(ll c2 = 0; c2 < sz(C[c1]); c2++){
                a = C[c1][c2];
                if(kind[a] == 0){
                    st1->add(0,L[a]+1,1);
                }
                else{
                    st2->add(0,L[a]+1,1);
                }
                MA[c1] = max(st1->query(0,c1+1) , st2->query(0,c1+1));
                st1->set(c1,c1+1,MA[c1]);
                st2->set(c1,c1+1,MA[c1]);
                //MA[c1][kind[a]] = max(MA[c1][kind[a]] , temp);
                //st1.update(c1,MA[c1][0]);
                //st2.update(c1,MA[c1][1]);
            }
          //  cout << MA[c1][0] << " " << MA[c1][1] << "  k\n";

            ANS[MA[c1]] = min(c1, ANS[MA[c1]] );
            //ANS[MA[c1][1]] = min(c1, ANS[MA[c1][1]] );
        }


        ll mi = 13333337;

        for(ll c1 = n; c1 > 0; c1--){
            ANS[c1] = min(mi,ANS[c1]);
            mi = min(mi, ANS[c1]);
        }

        for(ll c1 = 0; c1 < n; c1++){

            if(ANS[c1+1] == 13333337){
                cout << "-1 ";
            }
            else{
                cout << ANS[c1+1]+1 << " ";
            }
        }cout << "\n";


    }


    return 0;
}
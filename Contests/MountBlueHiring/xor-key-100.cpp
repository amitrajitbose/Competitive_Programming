#include <cstdio>
#include <vector>
#include <algorithm>
using namespace std;

#define MAXPOW 15

int nCases;
int N, Q, curval;

int main() {
    for (scanf("%d",&nCases); nCases; nCases--) {
        scanf("%d%d",&N,&Q);
        vector<vector<int> > present =
            vector<vector<int> >((1<<(MAXPOW+1))-1);
        for (int i = 0; i < N; i++) {
            scanf("%d",&curval);
            for (int j = MAXPOW, k = 0; j >= 0; j--) {
                if (j != MAXPOW) {
                    k = 2*k+1;
                    if (curval & (1<<j)) k++;
                }
                present[k].push_back(i+1);
            }
        }
        for (int i = 0; i < Q; i++) {
            int p, q;
            scanf("%d%d%d",&curval,&p,&q);
            int k = 0, val = 0;
            for (int j = MAXPOW-1; j >= 0; j--) {
                int newk = 2*k + 1;
                int newval = 2*val;
                if (!(curval & (1<<j))) {
                    newk++;
                    newval++;
                }
                vector<int>::iterator itr =
                    lower_bound(present[newk].begin(),
                            present[newk].end(),
                            p);
                if (itr == present[newk].end() || *itr > q) {
                    newk = 2*(2*k+1)+1-newk;
                    newval = 2*(2*val)+1-newval;
                }


                k = newk;
                val = newval;
            }
            printf("%d",val^curval);
            if (nCases > 1 || i != Q-1) {
                printf("\n");
            }
        }
    }
}
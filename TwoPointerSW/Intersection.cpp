vector<int> Solution::intersect(const vector<int> &A, const vector<int> &B) {
    int p1=0,p2=0;
    vector<int> ans;
    while (p1<A.size() and p2<B.size()){
        if (A[p1] == B[p2])
            {ans.push_back(A[p1]); p1++; p2++;}
        else if(A[p1]<B[p2])
            p1++;
        else
            p2++;
    }
    return ans;
}


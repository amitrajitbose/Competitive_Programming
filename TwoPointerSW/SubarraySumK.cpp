// array has to be sorted to apply this method
vector<int> Solution::solve(vector<int> &A, int B) {
    int l=0, r=0, sum=A[0];
    while (l<A.size() and r<A.size() and l<=r){
        if (sum == B){
            return {A.begin() + l, A.end() - (A.size()-r-1)};
        }
        else if(sum < B){
            r++;
            sum += A[r];
        }
        else if(sum > B){
            sum -= A[l];
            l++;
        }
    }
    return {-1};
}


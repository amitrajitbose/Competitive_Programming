vector<int> Solution::searchRange(const vector<int> &A, int B) {
    vector<int> sol(2); // stores the solution
    sol[0] = -1;
    sol[1] = -1;
    // look for lower bound
    int low = 0, high = A.size()-1, mid;
    while (low <= high)
    {
        mid = low + (high - low)/2;
        if (A[mid] == B){
            sol[0] = mid;
            high = mid - 1;
        }
        else if(A[mid] > B){
            high = mid - 1;
        }
        else{
            low = mid + 1;
        }
    }
    if (sol[0] == -1)
        return sol; // element not present
    
    // look for upper bound
    low = 0, high = A.size()-1;
    while (low <= high)
    {
        mid = low + (high - low)/2;
        if (A[mid] == B){
            sol[1] = mid;
            low = mid + 1;
        }
        else if(A[mid] > B){
            high = mid - 1;
        }
        else{
            low = mid + 1;
        }
    }
    return sol;
}


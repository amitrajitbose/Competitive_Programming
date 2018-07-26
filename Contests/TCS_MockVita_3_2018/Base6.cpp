//MockVita Problem - Base 6

#include <bits/stdc++.h>
using namespace std;
int _mergeSort(int arr[], int temp[], int left, int right);
int merge(int arr[], int temp[], int left, int mid, int right);

/* This function sorts the input array and returns the
number of inversions in the array */
int mergeSort(int arr[], int array_size)
{
    int *temp = (int *)malloc(sizeof(int)*array_size);
    return _mergeSort(arr, temp, 0, array_size - 1);
}

/* An auxiliary recursive function that sorts the input array and
returns the number of inversions in the array. */
int _mergeSort(int arr[], int temp[], int left, int right)
{
int mid, inv_count = 0;
if (right > left)
{
    /* Divide the array into two parts and call _mergeSortAndCountInv()
    for each of the parts */
    mid = (right + left)/2;

    /* Inversion count will be sum of inversions in left-part, right-part
    and number of inversions in merging */
    inv_count = _mergeSort(arr, temp, left, mid);
    inv_count += _mergeSort(arr, temp, mid+1, right);

    /*Merge the two parts*/
    inv_count += merge(arr, temp, left, mid+1, right);
}
return inv_count;
}

/* This funt merges two sorted arrays and returns inversion count in
the arrays.*/
int merge(int arr[], int temp[], int left, int mid, int right)
{
int i, j, k;
int inv_count = 0;

i = left; /* i is index for left subarray*/
j = mid; /* j is index for right subarray*/
k = left; /* k is index for resultant merged subarray*/
while ((i <= mid - 1) && (j <= right))
{
    if (arr[i] <= arr[j])
    {
    temp[k++] = arr[i++];
    }
    else
    {
    temp[k++] = arr[j++];

    /*this is tricky -- see above explanation/diagram for merge()*/
    inv_count = inv_count + (mid - i);
    }
}

/* Copy the remaining elements of left subarray
(if there are any) to temp*/
while (i <= mid - 1)
    temp[k++] = arr[i++];

/* Copy the remaining elements of right subarray
(if there are any) to temp*/
while (j <= right)
    temp[k++] = arr[j++];

/*Copy back the merged elements to original array*/
for (i=left; i <= right; i++)
    arr[i] = temp[i];

return inv_count;
}
/*int sumOfDigits(int n){
    int sum=0;
    while(n>0){
        sum=sum+(n%10);
        n/=10;
    }
    return sum;
}*/
int deriveDigit(int n){
    // array to store binary number
    int base6Num[100];
 
    // counter for binary array
    int i = 0;
    while (n > 0) {
 
        // storing remainder in binary array
        base6Num[i] = n % 6;
        n = n / 6;
        i++;
    }
    int s=0;
    // sum of digits
    for (int j = i - 1; j >= 0; j--)
        s+=base6Num[j];
    return s;
}

//int main(int argv, char** args)
int main()
{
    int n;
    cin>>n;
    int arr[n];
    int x,i=0;
    char y;
    while(i<n-1){
        cin>>x>>y;
        arr[i]=x;
        i++;
    }
    cin>>arr[i];
    
    for(int j=0;j<n;j++)
        arr[j]=deriveDigit(arr[j]);
        
    cout<<mergeSort(arr, n)<<endl;
    //getchar();
    return 0;
}

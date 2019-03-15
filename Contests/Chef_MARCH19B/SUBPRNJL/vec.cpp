  #include <bits/stdc++.h>
  using namespace std;

  void insertionSort (vector<int>& data, int n) 
  {
  int i, j, tmp;

    for (i=1; i<n; i++)
    {
        j=i;
        tmp=data[i];
        while (j>0 && tmp<data[j-1])
        {
          data[j]=data[j-1];
          j--;
        }
        data[j]=tmp;
    }
  }

  int bisect_left(const vector<int>& sorted_vec, int key) {
     size_t mid, left = 0 ;
     size_t right = sorted_vec.size(); // one position passed the right end
     if(sorted_vec.size()==0)
      return 0;
     while (left < right) {
        mid = int((left + right)/2);
        if(sorted_vec[mid] < key){
          left = mid + 1;
        }
        else{
          right = mid;
        }
      }
     return left;      
  }

  bool binary_search(const vector<int>& sorted_vec, int key) {
     size_t mid, left = 0 ;
     size_t right = sorted_vec.size(); // one position passed the right end
     while (left < right) {
        mid = left + (right - left)/2;
        if (key > sorted_vec[mid]){
            left = mid+1;
        }
        else if (key < sorted_vec[mid]){                                        
          right = mid;
        }
        else {                                                                  
          return true;
       }                                  
     }
     return false;      
  }

  int main() {
    int tc;
    cin >> tc;
    while(tc--)
    {
      int n,i,j,m;
      double k;
      cin >> n >> k;
      vector<int> arr;
      for(i=0; i<n; i++)
      {
        int input;
        cin >> input;
        arr.push_back(input);
      }
      // cout << bisect_left(arr,2)<<endl;
      /*
      // Difficult method to print a vector
      cout << "Array Inserted Is\n";
      for(vector<int>::iterator itr=arr.begin(); itr!=arr.end();itr++)
      {
        cout<<*itr<<" ";
      }
      cout << endl;

      //Easier method
      for(auto x: arr)
        cout<<x<<" ";
      
      */
      // Core //
      
      int counter = 0;
      for(i=0; i<n; i++)
      {
        vector<int> sub;
        int* freq = new int[2001];
        for(j=i; j<n; j++)
        {
          m = ceil(k/((j-i)+1));
          
          int item = arr.at(j);
          freq[item] += 1;

          int pos = bisect_left(sub, item); //log n
          sub.insert(sub.begin()+pos, item);

          int temp = ceil(k/m);
          int X = sub.at(temp-1);
          int F = freq[X];
          /*
          for(vector<int>::iterator itr=sub.begin(); itr!=sub.end(); itr++)
          {
            if(*itr == X)
              F++;
          }
          */
          int flag = freq[F];
          /*
          for(vector<int>::iterator itr=sub.begin(); itr!=sub.end(); itr++)
          {
            if(*itr == F)
            if(binary_search(sub, F))
            {
              flag=1;
              break;
            }
          }
          */

          if(flag>0)
            counter++;
        }
      }
      cout << counter << endl;
    }
    return 0;
  }
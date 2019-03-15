  #include <bits/stdc++.h>
  using namespace std;


  int bisect_left(const vector<int>& sorted_vec, int key) {
     int mid, left = 0 ;
     int right = sorted_vec.size(); // one position passed the right end
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


  int main() {
    int tc;
    cin >> tc;
    while(tc--)
    {
      int n,i,j,m;
      double k;
      cin >> n >> k;
      int *arr = new int[n];
      for(i=0; i<n; i++)
      {
        cin >> arr[i];
      }

      // Core 

      int counter = 0;
      for(i=0; i<n; i++)
      {
        vector<int> sub;
        int freq[2001] = {0};
        memset(freq,0,2001);
        
        for(j=i; j<n; j++)
        {
          m = ceil(k/((j-i)+1)); //Multiplier
          
          int item = arr[j]; // New element for THIS subarray
          freq[item] += 1; //Counting it in

          int pos = bisect_left(sub, item);
          sub.insert(sub.begin()+pos, item);

          int temp = ceil(k/m);
          int X = sub[temp-1];
          int F = freq[X];
          
          int flag = freq[F];
          
          if(flag>0)
            counter++;
        }
        sub.clear();
        /*
        cout<<"FREQ\n";
        for(int bla=0; bla<5; bla++)
        	cout<<freq[bla]<<" ";
        cout<<"\n";
        */
        
      }
      cout << counter << "\n";
    }
    return 0;
  }
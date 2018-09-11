/*
Author : Amitrajit Bose
Problem : Fractional Knapsack Problem
Approach : Greedy Approach
*/

#include <bits/stdc++.h>
using namespace std;
struct item{
    int p,w;
    double pw; // stores the profit to weight ratio
};

bool comparer(item i, item j){
    return (i.pw > j.pw);
}

double fracs[50];
int point=0;

double knapsack(item items[],int n,int capacity){
    double totalProfit = 0.0;
    
    for(int i=0;i<n;i++)
		fracs[i] = 0.0;
    
    for(int i=0;i<n;i++){
        if(capacity==0){
            //cout << totalProfit <<endl;
			break;
        }
        else if(items[i].w <= capacity){
            capacity -= items[i].w; //deduct the full Weight
            fracs[point] = 1.0;
            totalProfit += items[i].p*fracs[point];
			//cout << totalProfit << endl;
            point++;
        }
        else{
			fracs[point] = (capacity*1.0)/items[i].w;
			totalProfit += items[i].p*fracs[point];
			point++;
			//cout <<totalProfit<<endl;
			capacity=0;
            break;
        }
    }
    return totalProfit;
}
int main()
{
    int i,n,bagmax;
    cout << "Enter Total Items: ";
    cin >> n;
    item items[n];
    
    for(i=0;i<n;i++){
        cout << "Enter Profit of Item "<<(i+1)<<" : ";
        cin >> items[i].p;
        cout << "Enter Weight of Item "<<(i+1)<<" : ";
        cin >> items[i].w;
        items[i].pw = items[i].p*1.0 / items[i].w;
    }
    cout << "Enter Maximum Capacity of knapsack: ";
    cin >> bagmax;
    sort(items,items+n,comparer);
    double t = knapsack(items, n, bagmax);
    cout << endl << endl;
    cout << "Profit\tWeight\tRatio\n";
    for(int i=0;i<n;i++){
        cout << items[i].p<<"\t"<<items[i].w<<"\t"<<fracs[i]<<endl;
    }
	cout << "Total Profit: " << t <<endl;
    return 0;
}

/*
INPUT:
3
25
18
24
15
15
10
20

OUTPUT:
Profit  Weight  Ratio
24  15  1
15  10  0.5
25  18  0
Total Profit: 31.5
*/

/*
Enter Total Items: 3
Enter Profit of Item 1 : 60
Enter Weight of Item 1 : 10
Enter Profit of Item 2 : 100
Enter Weight of Item 2 : 20
Enter Profit of Item 3 : 120
Enter Weight of Item 3 : 30
Enter Maximum Capacity of knapsack: 50


Profit  Weight  Ratio
60  10  1
100 20  1
120 30  0.666667
Total Profit: 240
*/

#include <iostream>
using namespace std;

void fun(int* a,int* b) {
    *a=(*a)*(*b);
}

int main() {
    int a,b;
    cin>>a>>b;
    fun(&a,&b);
    cout << a ;

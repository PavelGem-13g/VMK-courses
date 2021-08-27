#include <iostream>

using namespace std;

int main() {
    int temp,a,n, k = 0;
    cin>>n;
    cin>> a;
    for (int i = 0; i < n; ++i)
    {
        cin>>temp;
        if (temp==a)
        {
            k++;
            //break;
        }
    }
    if (k>0)
    {
        cout<<k;
    }
    else
    {
        cout<<"Таких чисел нет";
    }
}

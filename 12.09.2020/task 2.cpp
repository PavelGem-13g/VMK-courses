#include <iostream>

using namespace std;

int znak(int k)
{
    if(k>0)return 1;
    if(k<0) return -1;
    return 0;
}

int main() {
    int n, a, k = 0, S = 0;
    cin>>n;
    for (int i = 0; i < n; ++i)
    {
        cin>>a;
        if (znak(a)==-1)
        {
            k++;
            S+=a;
        }
    }
    if(k==0)cout<<"Нет отрицательных чисел";
    else
        {
            cout<<S/k;
        }
}

#include <iostream>

using namespace std;

int main() {
    int a,max = -1, n;
    cin>>n;
    for (int i = 0; i < n; ++i)
    {
        cin>>a;
        if (max<a and a%2==1)
        {
            max = a;
        }

    }
    if(n>1)
    {
        if(max==-1) cout<<"Таких чисел нет";
        else cout<<max;
    } else cout<<"Последовательность слишком короткая";
}
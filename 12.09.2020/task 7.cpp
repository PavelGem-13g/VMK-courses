#include <iostream>

using namespace std;

int main() {
    int a,min = 10,max = -1,n;
    cin>>n;
    for (int i = 0; i < n; ++i)
    {
        cin>>a;
        if (min>a)
        {
            min = a;
        }
        if (max<a)
        {
            max = a;
        }
    }
    if(n>1)
    {
        cout<<max-min;
    } else cout<<"Последовательность слишком короткая";
}
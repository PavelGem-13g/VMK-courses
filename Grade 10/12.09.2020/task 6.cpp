#include <iostream>

using namespace std;

int main() {
    int a,min = 10,minI = 0,maxI = 0,max = -1,n;
    cin>>n;
    for (int i = 0; i < n; ++i)
    {
        cin>>a;
        if (min>a)
        {
            minI = i;
            min = a;
        }
        if (max<a)
        {
            maxI = i;
            max = a;
        }
    }
    if(n>1)
    {
        if(minI<maxI)
        {
            cout<<"Yes";
        } else cout<<"No";
    } else cout<<"Последовательность слишком короткая";
}
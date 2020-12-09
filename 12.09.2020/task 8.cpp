#include <iostream>

using namespace std;

int main() {
    int a,max = -1, k = 0,n;
    cin>>n;
    for (int i = 0; i < n; ++i)
    {
        cin>>a;
        if (max<a)
        {
            max = a;
            k = 1;
        }
        else
        {
            if(max==a)
            {
                k++;
            }
        }
    }
    if(n>1)
    {
        cout<<k;
    } else cout<<"Последовательность слишком короткая";
}
#include <iostream>

using namespace std;

int main() {
    int a,min = 10,minI = 0,min2I = 10,min2 = -1,n;
    cin>>n;
    for (int i = 0; i < n; ++i)
    {
        cin>>a;
        if (min>a)
        {
            min2I = minI;
            minI = i;
            min2 = min;
            min = a;
        }
    }
    if(n>1)
    {
        cout<<minI + 1<<" "<<min2I + 1;
    } else cout<<"Последовательность слишком короткая";
}
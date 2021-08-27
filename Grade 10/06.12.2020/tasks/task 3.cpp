#include <iostream>

using namespace std;

bool soversh(int n)
{
    bool result = false;
    int s = 0;
    for (int i = 1; i < n; ++i)
    {
        if(n%i==0)
        {
            s+=i;
        }

    }
    if(s==n)
    {
        result = true;
    }
    return result;
}

int main() {
    int n;
    cin>>n;
    for (int i = 1; i <= n; ++i) {
        if(soversh(i))
        {
            cout<<i<<" ";
        }
    }
}

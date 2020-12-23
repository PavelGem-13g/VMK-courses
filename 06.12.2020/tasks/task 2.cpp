#include <iostream>

using namespace std;

bool IsSimple(int n)
{
    bool result = false;
    int k = 0;
    for (int i = 1; i <= n; ++i) {
        if(n%i==0)
        {
            k++;
        }
    }
    if (k<3)
    {
        result = true;
    }
    return result;
}

int main() {
    int n,k;
    cin>>n>>k;
    for (; n <= k; ++n)
    {
        if(!IsSimple(n))
        {
            cout<<n<<" ";
        }
    }
}

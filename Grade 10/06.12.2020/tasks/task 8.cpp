#include <iostream>
#include <cmath>

using namespace std;

int stepenMaxOf10(int n)
{
    int result = 0;
    while (n>0)
    {
        result++;
        n/=10;
    }
    return result;
}

int main() {
    int n, m;
    cin>>n>>m;
    n += pow(10,stepenMaxOf10(n))*m;
    cout<<n;
}

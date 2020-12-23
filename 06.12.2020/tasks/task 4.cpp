#include <iostream>

int amount(int n)
{
    int result = 0;
    for (int i = 1; i <= n; ++i) {
        if(n%i==0)
        {
            result++;
        }
    }
    return result;

}

using namespace std;

int main() {
    int n,m;
    cin>>m>>n;
    for (; m <= n; ++m) {
        if(amount(m)==4)
        {
            cout<<m<<" ";
        }
    }
}

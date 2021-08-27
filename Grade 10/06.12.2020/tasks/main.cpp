#include <iostream>
#include <cmath>

using namespace std;

int main() {
    int n;
    cin>>n;
    int k = 1;
    int result = 0;
    while (n>0)
    {
        int temp = n%10;
        result+=pow(10,k)*temp;
        k+=2;
        n/=10;
    }
    cout<<result;
}

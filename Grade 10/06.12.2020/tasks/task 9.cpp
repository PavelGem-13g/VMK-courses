#include <iostream>
#include <cmath>

using namespace std;

int main() {
    int n;
    cin>>n;
    int k = 0;
    int result = 0;
    while (n>0)
    {
        int temp = n%10;
        if(temp%2==0)
        {
            result+=pow(10,k)*temp;
        }
        k++;
        n/=10;
    }
    cout<<result;
}

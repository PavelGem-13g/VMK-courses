#include <iostream>

using namespace std;

int main() {
    int n;
    cin>>n;

    for (int x = 1; x < n/2+(n%2); ++x) {
        if(n%x==0)
        {
            cout<<x<<"*"<<n/x<<"\n";
        }
    }
}


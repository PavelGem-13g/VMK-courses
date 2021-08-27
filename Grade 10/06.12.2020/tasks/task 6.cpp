#include <iostream>
#include "math.h"

using namespace std;

int main() {
    int n;
    cin>>n;
    bool flag = false;
    for (int i = 1; i < n; ++i) {
        for (int j = 1; j < n; ++j) {
            if(pow(i+j,2)==n)
            {
                flag = true;
                break;
            }
        }
    }
    if (flag)
    {
        cout<<"Yes";
    } else
        {
        cout<<"No";
        }
}

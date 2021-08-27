#include <iostream>

using namespace std;

int main() {
    int temp,a,n;
    bool flag = false;
    cin>>n;
    cin>> a;
    for (int i = 0; i < n; ++i)
    {
        cin>>temp;
        if (temp==a)
        {
            flag = true;
            //break;
        }
    }
    if (flag)
    {
        cout<<"Yes";
    }
    else
        {
        cout<<"No";
        }
}

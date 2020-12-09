#include <iostream>

using namespace std;

int main() {
    int temp,temp2,n;
    bool flag = false;
    cin>>n;
    cin>> temp;
    for (int i = 0; i < n-1; ++i)
    {
        cin>>temp2;
        if (temp2 < temp)
        {
            flag = true;
        }
        temp = temp2;
    }
    if (flag)
    {
        cout<<"No";
    }
    else
    {
        cout<<"Yes";
    }
}

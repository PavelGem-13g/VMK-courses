#include <iostream>

using namespace std;

int znak(int k)
{
    if(k>0)return 1;
    if(k<0) return -1;
    return 0;
}

int main() {
    int temp,temp2,n;
    bool flag = false;
    cin>>n;
    cin>> temp;
    for (int i = 0; i < n-1; ++i)
    {
        cin>>temp2;
        if (znak(temp) != znak(temp2))
        {
            flag = true;
            //break;
        }
        temp = temp2;
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

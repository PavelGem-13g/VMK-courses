#include <iostream>

using namespace std;

int main()
{
int n;
float res = 0;
  cin>>n;
  res = 0;
    for (int i = 1; i <= n; ++i)
    {
        if (i%2==0)
        {
            res += float(i)/(i+2);
        }
        else
            {
                res -= float(i)/(i+2);
            }
    }
    cout<<res;
}

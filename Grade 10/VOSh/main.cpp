#include <iostream>
#include "math.h"
using namespace std;

long sum(long arr[])
{
    long result = 0;
    for (int i = 0; i < sizeof(arr); ++i) {
        result+=abs(arr[i]);
    }
    return result;
}

int main() {
    long n, m, i, j;
    cin>>n>>m;
    long plus[n], minus[m];
    for (j = 0; j < n; j++)
    {
        cin >> plus[j];
    }
    for (j = 0; j < m; j++)
    {
        cin >> minus[j];
    }
    long x1 = sum(plus) + sum(minus);
    for (j = 0; j < n; j++)
        plus[j]++;
    for (j = 0; j < m; j++)
        minus[j]--;
    long x2 = sum(plus) + sum(minus);
    for (i = 0; x1 > x2; i++)
    {
        for (j = 0; j < n; j++) plus[j]++;
        for (j = 0; j < m; j++) minus[j]--;
        x1 = x2;
        long x2 = sum(plus) + sum(minus);
    }
    cout<<i;
}

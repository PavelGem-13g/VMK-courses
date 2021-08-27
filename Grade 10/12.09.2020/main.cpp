#include <iostream>
#include <conio.h>

#include <stdio.h>
#include <iostream>
using namespace std;
int main (){
    for (int i = 0; i<999; i++) {
        int x = i;
        int a = 0, b = 1;
        while (x > 0){
            if (x % 3 > 0) a++;
            if(x % 3 > 1) b++;
            x /= 10;
        }
        if (a == 3 and b == 2) {
            cout<<i <<"  ";
        }
    }
}
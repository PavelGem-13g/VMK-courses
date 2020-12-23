#include <iostream>
#include "fstream"

using namespace std;

int main()
{
    string line;
ifstream in("C:\\Users\\pashe\\Downloads\\задание 1.txt");
if(in.is_open())
{
    while (getline(in, line))
    {
        cout<<line<<" ";

    }

}
in.close();
}

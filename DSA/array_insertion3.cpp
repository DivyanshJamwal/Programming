#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;
int main() {
    int n; cin>>n;
    char ele;
    if(n<0 || n>20) { cout<<"Invalid size of array";}
    else
    {
        while(cin>>ele){
            if('A' <= ele && ele <= 'Z') printf("%c %c ", ele, ele+32);
            else printf("%c ", ele);
        }
    }
    return 0;
}
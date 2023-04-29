#include<iostream>
using namespace std;

int main() {
int n,i,j,prime = 0, sum = 0;
cout<<"How many elements";
cin>>n;
int a[n];
cout<<"Enter array elements";
for( i = 0; i < n; i++ )
cin>>a[i];

for( i = 0; i < n; i++ )
{
for( j = 2; j < a[i]/2; j++ )
{
if ( a[i] % j == 0 )
{
prime = 0;
break;
}
else
{
prime = 1;
}
}
if(prime == 1) sum = sum + a[i];
}
cout<<"Sum of prime is: "<<sum;
}
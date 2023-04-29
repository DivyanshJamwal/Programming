#include <iostream>
using namespace std;

int main()
{
    int n; 
 cin>>n;
 if(n<2)
 {
 cout<<"Invalid Input";
 return 0;
 }
 string s[n];
 for(int i= 0; i<n; i++)
 {
 cin>>s[i];
 if(s[i].length()==0){
 
 cout<<"Invalid Input";
 break;
 }
 }
 
 for(int i=0; i<n; i++)
 {
 int c=0;
 for(int j=0; j<=i; j++)
 {
 if(s[i]==s[j] && i!=j)
 {
 c= c+1;
 }
 
 
 }
 if(c>0)
 { 
 continue;
 
 }
 else
 {
 
 cout<<s[i]<<" ";
 }
 
 }
    return 0;
}
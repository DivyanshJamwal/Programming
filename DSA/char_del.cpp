#include <iostream>
using namespace std;

int main()
{
    int i,j;
    char st[100],c;
    int count = 0;
    cout<<"Enter a string: ";
    cin>>st;

    cout<<"Enter the character to be removed: ";
    cin>>c;

    for(i=0;st[i]!='\0';i++){
        if(st[i]==c){
            for(j=i;st[j]!='\0';j++){
                st[j]=st[j+1];
            }
            i--;
        }
        
    }
    cout<<st<<endl;
    
}
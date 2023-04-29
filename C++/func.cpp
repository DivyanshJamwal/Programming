//No returning value and no parameters
#include <iostream>
using namespace std;
void add();//Function declaration
int main()
{
    add();//Function calling
    return 0;
}
//Function definition
void add()//Function header
{
    //Function body
    int a,b,sum;
    cout<<"\nEnter values of a and b:";
    cin>>a>>b;
    sum=a+b;
    cout<<"\nSum is:"<<sum;
}


//Returning value and no parameters
/*#include <iostream>
using namespace std;
int add();//Function declaration
int main()
{
    cout<<add();//Function calling
    return 0;
}
//Function definition
int add()//Function header
{
    //Function body
    int a,b,sum;
    cout<<"\nEnter values of a and b:";
    cin>>a>>b;
    sum=a+b;
    return sum;
}

//No returning value but taking parameters
#include <iostream>
using namespace std;
void add(int,int);//Function declaration
int main()
{
    int a,b;
    cout<<"\nEnter values of a and b:";
    cin>>a>>b;
    add(a,b);//Actual arguments
    return 0;
}
//Function definition
void add(int x,int y)//Function header(Formal arguments)
{
    //Function body
    int sum;
    sum=x+y;
    cout<<"\nSum is:"<<sum;
}

//Returning value and taking parameters
#include <iostream>
using namespace std;
int add(int,int);//Function declaration
int main()
{
    int a,b;
    cout<<"\nEnter values of a and b:";
    cin>>a>>b;
    cout<<"\nSum is:"<<add(a,b);//Actual arguments
    return 0;
}
//Function definition
int add(int x,int y)//Function header(Formal arguments)
{
    //Function body
    int sum;
    sum=x+y;
    return sum;
}*/

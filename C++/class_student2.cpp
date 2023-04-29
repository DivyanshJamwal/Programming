#include <iostream>
using namespace std;
class student
{
    int reg_no;
    public:
    char name[100];
    int roll_no;
    void input()
    {
        cout<<"\nEnter name:";
        cin>>name;
        cout<<"\nEnter reg. no:";
        cin>>reg_no;
        cout<<"\nEnter roll no:";
        cin>>roll_no;
    }
    void display()
    {
        cout<<"\nStudent information is:";
        cout<<endl<<"Name:"<<name<<" "<<"Registration number is:"<<reg_no<<" "<<"Roll number is:"<<roll_no;
    }
};
int main()
{
    student obj[3];
    int max,index,i;
    for(int i=0;i<3;i++)
    {
    obj[i].input();
    obj[i].display();
    }
    max=obj[0].roll_no;
    for(i=1;i<3;i++)
    {
        if(obj[i].roll_no>max)
        {
            max=obj[i].roll_no;
            index=i;
        }
    }
    cout<<"\nStudent name with highest roll number is:"<<obj[index].name<<"and it's roll number is:"<<max;
    return 0;
}


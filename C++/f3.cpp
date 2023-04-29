#include<iostream>
using namespace std;
class test
{
        int a, b, c;
        public:
                void input()
                {
                    cout<<"Enter the Numbers: ";
                    cin>>a>>b>>c;
                }
                friend void find(test);
};
void find(test t)
{
        if(t.a>t.b&&t.a>t.c){
            cout<<"largest no. is "<<t.a;
        }else if(t.b>t.c){
            cout<<"largest no. is "<<t.b;
        }else{
            cout<<"largest no. is "<<t.c;
        }
}
int main()
{
        test t;
        t.input();
        find(t);
        return 0;

}
#include<iostream>
using namespace std;

int stack[50];
int top = -1;
void insert(int item) {
if(top == 49) cout<<"Overflow";
else {
top++;
stack[top] = item;
}
}
void pop(int item) {
if(top == -1) cout<<"Underflow";
else {
cout<<stack[top]<<"deleted";
top--;
}
}
void display() {
    int i = top;
    for(i = top;i>=0;i--)
    cout<<stack[i]<<" ";
}
int main() {

int ch,x;
do {
cout<<"press 1 to insert and 2 to display and 0 to exit";
cin>>ch;
if(ch==1){
cout<<"Enter element";
cin>>x;
insert(x);
}
else if(ch==2){
    display()
}
else if(ch==3){
    pop()
}
}while(ch!=0);
}
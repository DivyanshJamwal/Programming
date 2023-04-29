#include <iostream>
using namespace std;

int main()
{
    int stack[10];
    int top = -1;
    int ch,item;
    cout<<"1) Push into stack"<<endl;
    cout<<"2) Pop from stack"<<endl;
    cout<<"3) Display stack"<<endl;
    cout<<"4) Exit"<<endl;
    do{
        cout<<"Enter your choice: "<<endl;
        cin>>ch;
        switch(ch){
            case 1:{
                cout<<"Enter value to be pushed: "
            }
        }
    }
}

void push(int item){
    if(top >= 9){
        cout<<"STACK OVERFLOW"<<endl;
    }
    else{
        top++;
        stack[top]=item;
    }
}

void pop(int item){
    if(top==-1){
        cout<<"STACK UNDERFLOW"<<endl;
    }
    else{
        item = stack[top];
        top--;
    }
}

void display(){
    if(top>=0){
        cout<<"Stack elements are: ";
        for(int i=top;i>=0;i--)
        cout<<stack[i]<<" ";
        cout<<endl;
    }
    else{
        cout<<"Stack is empty";
    }
}

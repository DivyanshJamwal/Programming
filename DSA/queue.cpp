#include <iostream>
using namespace std;

int queue[50];
int front = -1;
int rear = -1;

void insert(int item){
    if(front==0 && rear=49){
        cout<<"Overflow";
    }
    return;
    else if(front==rear+1){
        cout<<"Overflow"
    }
    return;
    else if(front==0){
        front=1;
        rear=1;
    }
    else if(rear==49){
        rear=1;
    }
    else{
        rear=rear+1;
    }
    queue[rear]=item;
}

void display(){
    if(front<=rear){
        for(int i = front;i<=rear;i++){
            cout<<queue[i]<<" ";
        }
    }
    else{
        for(int i = front;i<10;i++){
            cout<<queue[i]<<" ";
        }
        for(int i = 0;i<=rear;i++){
            cout<<queue[i]<<" ";
        }
    }
}

void delque(){
    if(front==-1){
        cout<<"Underflow";
        item = queue[front];
    }
    else {
        if(front == rear){
            front = 0;
            rear = 0;
        }
        else if(front = ){
            front = 0;
        }
        else{
            front = front+1
        }
    }
}


int main()
{
    
}
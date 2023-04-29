#include <iostream>
using namespace std;

class Node{
    public:
    int data;
    Node* next;
};
Node* head = NULL;
void push(int item){
    Node* n = new Node;
    n->data = item;
    n->next = head;
    head = n;
}
void pop(){
    if(head==NULL){
        cout<<"Underflow";
    }
    else{
        Node *ptr = head; 
        head = head->next;
        free(ptr);  //free memory
    }
}
void display(){
    Node* ptr = head;
    while(ptr != NULL){
        cout<<ptr->data;
        ptr = ptr->next;
    }
}

int main()
{
    
}


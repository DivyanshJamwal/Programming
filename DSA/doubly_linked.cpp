#include <iostream>
using namespace std;

class Node{
    public:
    int data;
    Node* next;
    Node* previous;
};

Node* head = NULL;
Node* tail = NULL;

void insert(int d){
    Node *n = new Node;
    n->data =d;

    if (head == NULL){
        head = n;
        tail = n;
        n->previous = NULL;
        n->next = NULL;
    }
    else{
        n->previous = tail;
        n->next = NULL;
        tail->next = n;
        tail = n;
    }
}
void traverse(){
    Node *ptr = head;
    cout<<"Traversing in forward";
    while(ptr != NULL){
        cout<<ptr->data<<" ";
        ptr = ptr->next;
    }
    ptr = tail;
    cout<<"Traversing in backward direction";
    while(ptr != NULL){
        cout<<ptr->data<<" ";
        ptr = ptr->previous;
    }
}
void insertAfterElement(int x,int d){
    Node *n = new Node;
    n->data = d;
    Node* ptr = head;
    while (ptr!=NULL){
        if(ptr->data == x){
            if(ptr->next != NULL){
                n->previous = ptr;
                n->next = ptr->next;
                ptr->next = n;
                (n->next)->previous = n;
            }
            else{
                insert(d);
            }
        }
    }
}
void deleteFirstNode(){
    if(head == NULL) {
        cout<<"Underflow";
    }
    else if(head == tail){
        head = NULL;
        tail = NULL;
    }
    else {
        head = head->next;
        head->previous = NULL;
    }
}

int main()
{
    int n,x;
    cout<<"Enter the no. of elements"<<endl;
    cin>>n;
    cout<<"Enter the elements to be inserted"<<endl;
    for(int i=0;i<n;i++){
        cin>>x;
        insert(x);
    }
    cout<<"List of Elements"<<endl;
    deleteFirstNode();
    cout<<endl;
    
}
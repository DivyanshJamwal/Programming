#include<iostream>
using namespace std;

class Node {
public:
int data;
Node* next;
};
Node* head = NULL;
void insert(int d) {
Node* ptr;
Node* prevptr;
Node* n = new Node;
n->data = d;
n->next = NULL;
if(head == NULL) {
head = n;
}
else {
ptr = head;
while (ptr->next != NULL) {
ptr = ptr->next;
}
ptr->next = n;
}
}
void traverse() {
Node* ptr;
ptr = head;
while (ptr != NULL) {
cout<<ptr->data<<" ";
ptr = ptr->next;
}
}
void deletefirstNode() {
if(head == NULL) {
cout<<"Linked list is empty";
}
else {
head = head->next;
}
}
void insertAtLocation(int l, d){
    Node* ptr = head;
    int i = 1;
    if(l == 1){
        insertBeg(d);
    }
    else{
        Node* n = new Node;
        n->data =d;
        for(int i = 1;i<l - 1;i++){
            ptr = ptr->next;
        }
        n->next = ptr->next;
        ptr->next = n;
    }
}
void insertAfterNode(){
    Node* n = new Node;
    n->data = d;
    n->next = NULL;

    if(head == NULL){
        head = n;
    }
    else{
        Node *ptr =head;
        while(ptr != NULL){
            if(ptr->data ==loc){
                n->next = ptr->next;
                ptr->next = n;
            }
            ptr = ptr->next;
        }
    }
}
void deleteAllOccurences(){
if(head == NULL){
cout<<"Linked list is empty";
}
else{
    while(head->data == d){
        head = head->next;
    }
    ptr = head;
    prevptr = head;
    while(ptr != NULL){
        if(ptr->data == d){
            prevptr->next = ptr->next;
        }
        else{
            prevptr = ptr;
        }
        ptr = ptr->next;
        cout<<"all occurences deleted"
    }
}
}
void insertAfterNode(int x, int d) {
Node* n = new Node;
n->data = d;

Node *ptr;
ptr = head;
while (ptr != NULL) {
if(ptr->data == x) {
n->next = ptr->next;
ptr->next = n;
}
ptr = ptr->next;
}
}

void deleteAllOccurennces(int d) {

while (head->data == d) {
head = head->next;
}
Node *ptr = head;

while (ptr!=NULL) {
if((ptr->next)->data == d) {
ptr->next = (ptr->next)->next;
}
ptr = ptr->next;
}

}
void deleteLastNode() {
if(head == NULL) {
cout<<"Linked list is empty";
}
else if(head->next == NULL) {
head = NULL;
}
else {
Node* ptr = head;
while((ptr->next)->next != NULL)
ptr = ptr->next;
ptr->next = NULL;
cout<<"last node deleted";
}
}
int main() {
int ch = 1,i,x;
while (ch != 0) {
cout<<"\nPress:\n1. to inssert new node.\n2. To delete first node.\n3. To delete last node.\n4. To traverse. \n0. to exit.";
cin>>ch;
if(ch == 1) {
cout<<"Enter data to insert";
cin>>x;
insert(x);
}
else if(ch == 2) {
deletefirstNode();
}
else if(ch == 3){
deleteLastNode();
}
else if(ch == 4) {
traverse();
}
}
}


#include<iostream>
using namespace std;

class Node {
public:
int data;
Node* next;
};
Node* head = NULL;

void insert(int d) {
Node* n = new Node;
n->data = d;

if(head == NULL) {
n->next = head;
head = n;
}
else {
Node* ptr = head;
while (ptr->next != head) {
ptr = ptr->next;
}
n->next = head;
ptr->next = n;
}
}
void traverse() {
Node* ptr;
ptr = head;
cout<<head->data<<" ";
ptr = ptr->next;
while (ptr != head) {
cout<<ptr->data<<" ";
ptr = ptr->next;
}
}
void insertAtBeginning(int d) {
Node* n = new Node;
n->data = d;
if(head == NULL){
    head = n;
    n->next = head;
}
n->next = head;

}
int main() {
int x;
cout<<"Enter 10 numbers";
for(int i = 0; i < 10; i++) {
cin>>x;
insert(x);
}
}
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
int main() {
int n,i,x;
cout<<"How many nodes";
cin>>n;
for(i = 0; i< n; i++){
cin>>x;
insert(x);
}
traverse();
}
#include <iostream>
using namespace std;
class Node {
    public:
    int data;
    Node* next;
};
Node* front = NULL;
Node* rear = NULL;

void enqueue(int item) {
    Node* n = new Node;
    n->data = item;
    n->next = NULL;
    if(front == NULL){
        front = rear = n;
    }
    else{
        rear->next = n;
        rear = n;
    }
}
void dequeue(){
    if(front == NULL){
        cout<<"No node to delete";
    }
    else{
        Node* temp = front;
        front = front->next;
        free(temp);
    }
}
int main()
{
    
    return 0;
}
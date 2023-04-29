#include<iostream>
using namespace std;
class Node{
public:
int data;
Node*left;
Node*right;
};

void PrintInorder(Node*node){
if(node!=NULL)
PrintInorder(node->left);
cout<<node->data<<" ";
PrintInorder(node->right);
}

void PrintPreorder(Node*node){
if(node!=NULL)
cout<<node->data<<" ";
PrintInorder(node->left);
PrintInorder(node->right);
}

void PrintPostorder(Node*node){
if(node!=NULL)
PrintInorder(node->left);
PrintInorder(node->right);
cout<<node->data<<" ";
}

Node* create(){
int ch;
cout<<"Enter data or -1 for no data :";
cin>>ch;
if(ch==-1){
return 0;
}
else {
Node*n= new Node;
n->data=ch;
n->left=NULL;
n->right=NULL;
cout<<"Enter data for left :";
n->left=create();
cout<<"Enter data for right :";
n->right=create();
return n;

}
}



int main(){

Node*root=NULL;
root=create();
PrintInorder(root);
PrintPreorder(root);
PrintPostorder(root);
return 0;
}
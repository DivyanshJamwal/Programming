#include<iostream>
using namespace std;

void TowerofHanoi(int n,char beg, char end ,char aux){
    if(n==0){
        return;
    }
    else{
        TowerofHanoi(n-1,beg,aux,end);
        cout<<"Move disk "<<n<<" from "<<beg <<" to "<< end<<endl;
        TowerofHanoi(n-1,aux,end,beg);
    }
}

int main(){
  int N;
  cout<<"Enter the number: ";
  cin>>N;
  TowerofHanoi(N,'A','C','B');
  return 0;

}
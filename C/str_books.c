//create a book structure containing bookid,bname and bprice.enter the detail
//for 5 books
#include<stdio.h>
struct book
{
int bookid;
char bname[20];
float bprice;
};
int main()
{
struct book b1[5];//array of struct book array b1[0] to b1[4]
printf("enter the data in array");
int i;
for(i=0;i<5;i++)
{
scanf("%d",&b1[i].bookid);
scanf("%s",b1[i].bname);//& operator is required or not
scanf("%f",&b1[i].bprice);

}
printf("you have entered this data");
for(i=0;i<5;i++)
{
printf("%d\t",b1[i].bookid);
printf("%s\t",b1[i].bname);
printf("%f\n",b1[i].bprice);

}


}

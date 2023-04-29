//create a book structure containing bookid,bname and bprice.enter the detail
//for 5 books.find the detail of book with highest price
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
int i,j=-8;
for(i=0;i<5;i++)
{
scanf("%d",&b1[i].bookid);
scanf("%s",b1[i].bname);//& operator is required or not
scanf("%f",&b1[i].bprice);

}
float hprice;
hprice=b1[0].bprice;//asumption

for(i=1;i<5;i++)
{
if(b1[i].bprice>hprice)
{
j=i;
}
}
printf("book with highest cost is=\n");
printf("%d\n",b1[j].bookid);
printf("%s\n",b1[j].bname);
printf("%f\n",b1[j].bprice);

}

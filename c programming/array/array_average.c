#include <stdio.h>
int main()
{
    int i, sum=0,num[]={10,20,30,40,50};

for (i=0; i<5; i++) {
    sum=sum+num[i];
}
printf("sum = %d\n",sum);
printf("average = %.2f\n",(float)sum/5);
}
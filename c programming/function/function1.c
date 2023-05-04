#include "stdio.h"
int  sum(int a,int b){
    return a+b;
}
int main()
{
    int n1,n2;
    printf("Enter 2 numbers : ");
    scanf("%d %d",&n1,&n2);
    printf("The sum of two numbers is %d\n",sum(n1,n2));
}

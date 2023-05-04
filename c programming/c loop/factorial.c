#include<stdio.h>
int main()
{
    int fact=1,i,n;
    printf("Enter any Number : ");
    scanf("%d",&n);
    for (i=1; i<=n; i++) {
    fact=fact*i;
    }
    printf("the factorial of your number is %d\n",fact);
}
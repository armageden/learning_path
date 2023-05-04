#include <stdio.h>
int main()
{
    int i, sum=0,n;
    printf("Enter the last number of the series : ");
    scanf("%d",&n);
    printf("1+2+3+...+%d",n);
    for (i=1; i<=n; i++) {
    sum=sum+i;
    }
    printf("=%d\n",sum);
}
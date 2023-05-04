#include <stdio.h>
int main()
{
    int fact,i,rem,num,sum=0,temp;
    printf("Enter A Integgar to check if it is a strong number : ");
    scanf("%d",&num);
    temp=num;
    while (temp!=0) {
    rem=temp%10;

    fact=1;
    for (i=1;i<=rem ; i++) {
    fact=fact*i;
    }
    sum=sum+fact;
    temp=temp/10;

    }
    if (sum==num) {
    printf("It is a strong number\n");
    }
    
else 
    printf("It is not a strong number\n");
}
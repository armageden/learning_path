#include <stdio.h>
int main ()
{
    int num,sum=0,temp,rem;
    printf("Enter a Integer : ");
    scanf("%d",&num);
    temp=num;
    while (temp!=0) {
    rem=temp%10;
    sum=sum*10+rem;
    temp=temp/10;
    }
    if (num==sum) {
    printf("This is a Palindrome number\n");
    
    }
    else {
    printf("It is not a Palindrome number\n");
    }
}
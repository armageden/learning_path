#include <stdio.h>
#include <math.h>
int main ()
{
    int num,sum=0,rem,temp;
    printf("Enter the numbers : ");
    scanf("%d",&num);
    temp=num;
    while (temp!=0) {
    rem=temp%10;
    sum=sum+pow(rem,3);
    temp=temp/10;
    }
    if (num==sum) {
    printf("This is a armsrong number\n");
    }
    else {
    printf("This is not a armsrong number\n");

    }
}
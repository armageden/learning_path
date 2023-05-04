#include <stdio.h>
int main()
{
    int count=1,i,num;
    printf("Enter any integer to see if it is a prime : ");
    scanf("%d",&num);
    for (i=2; i<=num; i++) {
    if ((num%i)==0) {
    count=0;
       }
    }
    if(count==1) {
    printf("This is  a prime\n");
    }
    else {
    printf("This is not a prime\n");
    }
    
}
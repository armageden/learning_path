#include<stdio.h>
int main()
{
    int n1,n2,large;
    printf("Enter two numbers and find out the largest number ");
    scanf("%d %d",&n1,&n2);


    large=(n1>n2) ? n1:n2;
     /*    ^^^^^^^ this is the logic/ condition..
     which is that the largest int will get inside 'large' */
     printf("The largest number is %d\n",large);

}
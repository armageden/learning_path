#include<stdio.h>
int main()
{
    int num1=10,num2=5;

    num1=num1-num2; //here num1 becomes 5
    num2=num1+num2;//here num2 becomes 10
    num1=num2-num1;//here num1 becomes 5

    printf("num1 is : %d\n",num1);
    printf("num2 is : %d\n",num2);

}
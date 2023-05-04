#include<stdio.h>
int main()
{
    int num1,num2;
    printf("Enter your first number : ");
    scanf("%d",&num1);
    printf("Enter your second number : ");
    scanf("%d",&num2);
    if (num1>num2) {
    printf("Large number is : %d\n",num1);
    }
    else if (num1<num2) {
    printf("Larger number is : %d\n",num2);
    }
    else {
    printf("They are the same!!\n");
    }
    return 0;
}
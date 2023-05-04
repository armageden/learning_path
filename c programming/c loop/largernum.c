#include <stdio.h>
int main()
{
    float num1,num2,num3;
    printf("Enter any three numbers : ");
    scanf("%f %f %f",&num1,&num2,&num3);
    if (num1>num2&&num1>num3) {
    printf("Large num is %.3f\n",num1);
    }
    else if (num1<num2&&num2>num3) {
    printf("the largest num is %.3f\n",num2);
    }
    else if (num3>num1&&num3>num2) {
    printf("largest num is %.3f\n",num3);
    }
    else printf("The numbers are the same!!!\n");
    return 0;
}
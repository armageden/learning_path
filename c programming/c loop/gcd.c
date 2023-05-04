#include <stdio.h>
int main()
{   int num1,num2,n1,n2,rem,GCD,LMC;
    printf("Enter two numbers to figure out their GCD& LMC : ");
    scanf("%d %d",&num1,&num2);
    n1=num1,n2=num2;
    while (n2!=0) {
    rem=n1%n2;
    n1=n2;
    n2=rem;
    }
    GCD=n1;
    LMC=(num1*num2)/GCD;
    printf("GCD = %d & LMC = %d\n",GCD,LMC);
}
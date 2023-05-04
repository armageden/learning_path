#include <stdio.h>
#include <math.h> // becuse of sqrt
int main()
{
    double a,b,c,d,x1,x2;
    printf("Enter the equation numbers : ");
    scanf("%lf %lf %lf",&a,&b,&c);
    d=sqrt (b*b-4*a*c);

    x1=(-b+d/2*a);
    x2=(-b-d/2*a);
    printf("x1 = %lf\n",x1);
    printf("x2 = %lf\n",x2);
} // compile with -lm includeed in the command like gcc equation.c -o equation -lm
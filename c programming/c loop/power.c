#include <math.h>
#include <stdio.h>

int main()
{
    double x,y,result;
    printf(" Value of X : ");
    scanf("%lf",&x);
    printf(" Value of Y : ");
    scanf("%lf",&y);
    result=pow(x, y);
    printf("the value is : %.4lf\n",result);
}
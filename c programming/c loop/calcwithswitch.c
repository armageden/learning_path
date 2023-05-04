#include<stdio.h>
int main()
{   char op;
double res,n1,n2;
    printf("which mode will u choose ?\n (+ - * /) : ");
    scanf("%c",&op);
printf("Enter the two oparator on which the oparator would be used :");
scanf("%lf %lf",&n1,&n2);
switch (op) {
case '+':res=n1+n2;
printf("The result is %lf\n",res);
break;
case '-':res=n1-n2;
printf("The result is %lf\n",res);
break;
case '*':res=n1*n2;
printf("The result is %lf\n",res);
break;
case '/':res=n1/n2;
printf("The result is %lf\n",res);
break;
default: printf("It's not a valid input!!!!\n");

}
return 0;




}